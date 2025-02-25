import cv2
import numpy as np
from os import path
from .Moildev import Moildev
from .multitrading import Multithreading
from .additional_function import remap_image, cropping_image
from .merge_surrounding_image import merge_surrounding_image, merge_image_left_right_surrounding_view
from .merge_side_view import merge_image_side_view
from .process_bird_view_4_cam_center_perspective import merge_image_4_camera_center_perspective
from .surrounding_function import SurroundingImage
from .bird_view_function import BirdView
from .wide_view_function import WideView
from .side_view_function import SideView
from .perspective_process import PerspectiveView
import yaml


class MainController:
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.surrounding_function = SurroundingImage(self)
        self.bird_view = BirdView(self)
        self.wide_view = WideView(self)
        self.side_view = SideView(self)
        self.control_perspective = PerspectiveView(self)
        self.cap_cam = [None] * 4
        self.moildev = [None] * 4
        self.maps = [[None, None]] * 4

        self.mode = "original"
        self.current_image_calib = 0  # this is for specify which camera will calibration (single camera)

    def run_video(self):
        keys = list(self.model.properties_image)
        total_cam = self.model.properties_image["camera_used"]
        self.mode = "original"
        for i in range(total_cam):
            self.moildev[i] = Moildev.Moildev(self.model.properties_image[keys[i]]["camera_parameter"])
            self.cap_cam[i] = Multithreading(self.model.properties_image[keys[i]]["camera_source"])
            if not path.exists("../data_config/maps/map_x_anypoint_image_" + str(i) + ".npy"):
                self.bird_view.create_maps(i)
                self.wide_view.create_maps(i)
                self.side_view.create_maps(i)
                self.surrounding_function.create_maps(i)

    def next_frame(self):
        keys = list(self.model.properties_image)
        if not None in self.cap_cam:
            for i in range(self.model.properties_image["camera_used"]):
                self.model.image_original[i] = self.cap_cam[i].get_frame()
                if self.mode == "original":
                    pass

                elif self.mode == "calibration_bird_view" or self.mode == "front_bird_view" or \
                        self.mode == "rear_bird_view":
                    self.create_list_anypoint_image(i)

                elif self.mode == "calibration_wide_view":
                    self.model.list_image_wide_view[self.current_image_calib] = self.remap_additional(
                        self.model.image_original[self.current_image_calib], self.current_image_calib, "wide_view",
                        "map_x_anypoint", "map_y_anypoint")

                elif self.mode == "calibration_side_view":
                    self.model.list_image_side_view[self.current_image_calib] = self.remap_additional(
                        self.model.image_original[self.current_image_calib], self.current_image_calib, "side_view",
                        "map_x_anypoint", "map_y_anypoint")

                elif self.mode == "calibration_surrounding_view":
                    self.model.list_image_surrounding[self.current_image_calib] = self.remap_additional(
                        self.model.image_original[self.current_image_calib], self.current_image_calib,
                        "surrounding_view", "map_x_panorama_rotation", "map_y_panorama_rotation")
                    self.model.list_image_surrounding[self.current_image_calib] = self.crop_surrounding_image_view(
                        self.model.list_image_surrounding[self.current_image_calib], self.current_image_calib)

                elif self.mode == "surrounding_view":
                    self.create_list_anypoint_image(i)
                    image = self.remap_additional(self.model.image_original[i], i, "surrounding_view",
                                                  "map_x_panorama_rotation",
                                                  "map_y_panorama_rotation")
                    self.model.list_image_surrounding[i] = self.crop_surrounding_image_view(image, i)

                elif self.mode == "front_surrounding_view":
                    self.create_list_anypoint_image(i)
                    image = self.model.image_original[0]
                    image = self.remap_additional(image, 0, "surrounding_view",
                                                  "map_x_panorama_rotation",
                                                  "map_y_panorama_rotation")
                    self.model.list_image_surrounding[0] = self.crop_surrounding_image_view(image, 0)

                elif self.mode == "left_right_surrounding_view":
                    self.create_list_anypoint_image(i)
                    if i == 1 or i == 2:
                        image = self.model.image_original[i]
                        image = self.remap_additional(image, 1, "surrounding_view", "map_x_panorama_rotation",
                                                      "map_y_panorama_rotation")
                        image = self.crop_surrounding_image_view(image, i)
                        self.model.list_image_surrounding[i] = cv2.rotate(image, cv2.ROTATE_180)

                elif self.mode == "rear_surrounding_view":
                    self.create_list_anypoint_image(i)
                    image = self.model.image_original[3]
                    image = self.remap_additional(image, 3, "surrounding_view", "map_x_panorama_rotation",
                                                  "map_y_panorama_rotation")
                    image = self.crop_surrounding_image_view(image, 3)
                    self.model.list_image_surrounding[3] = cv2.rotate(image, cv2.ROTATE_180)

                # ------------------------------------------ wide view -------------------------------------------
                elif self.mode == "front_wide":
                    self.create_list_anypoint_image(i)
                    image = self.model.image_original[0]
                    self.model.list_image_wide_view[0] = self.remap_additional(image, 0, "wide_view",
                                                                               "map_x_anypoint",
                                                                               "map_y_anypoint")

                elif self.mode == "left_wide":
                    self.create_list_anypoint_image(i)
                    image = self.model.image_original[1]
                    self.model.list_image_wide_view[1] = self.remap_additional(image, 1, "wide_view",
                                                                               "map_x_anypoint",
                                                                               "map_y_anypoint")

                elif self.mode == "right_wide":
                    self.create_list_anypoint_image(i)
                    image = self.model.image_original[2]
                    self.model.list_image_wide_view[2] = self.remap_additional(image, 2, "wide_view",
                                                                               "map_x_anypoint",
                                                                               "map_y_anypoint")

                elif self.mode == "rear_wide":
                    self.create_list_anypoint_image(i)
                    image = self.model.image_original[3]
                    self.model.list_image_wide_view[3] = self.remap_additional(image, 3, "wide_view",
                                                                               "map_x_anypoint",
                                                                               "map_y_anypoint")

                elif self.mode == "side_left_right_view":
                    self.create_list_anypoint_image(i)
                    if i == 1 or i == 2:
                        self.model.list_image_side_view[i] = remap_image(
                            self.model.image_original[i],
                            np.load(self.model.properties_image[keys[i]]["side_view"]["map_x_anypoint"]),
                            np.load(self.model.properties_image[keys[i]]["side_view"]["map_y_anypoint"]))
                else:
                    pass

            if self.mode == "calibration_wide_view" or self.mode == "calibration_surrounding_view" or self.mode == "original" or self.mode == "calibration_side_view":
                pass
            else:
                image_crop = self.control_perspective.process_perspective(self.model.list_image_anypoint)
                self.model.image_bird_view_overlay, self.model.image_bird_view = \
                    merge_image_4_camera_center_perspective(image_crop,
                                                            self.control_perspective.data_dst,
                                                            self.model.properties_image,
                                                            "O")

            if self.mode == "front_bird_view" or self.mode == "left_right_bird_view" or self.mode == "rear_bird_view":
                self.model.image_bird_view_cropping = self.bird_view.crop_image_view(self.mode,
                                                                                     self.model.image_bird_view)

            elif self.mode == "surrounding_view":
                self.model.image_surrounding = merge_surrounding_image(self.model.list_image_surrounding)

            elif self.mode == "left_right_surrounding_view":
                self.model.image_surrounding = merge_image_left_right_surrounding_view(
                    self.model.list_image_surrounding)

            elif self.mode == "calibration_side_view":
                if self.current_image_calib == 1 or self.current_image_calib == 2:
                    self.model.image_side_view = merge_image_side_view(self.model.list_image_side_view)

            elif self.mode == "side_left_right_view":
                self.model.image_side_view = merge_image_side_view(self.model.list_image_side_view)

    def set_data_for_calib(self):
        """
        This function is for set data for calibration birds view by clicking the point on the image
        Returns:

        """
        image_crop = []
        images = [None] * len(self.model.list_image_anypoint)
        images[0] = self.model.list_image_anypoint[0]
        images[1] = cv2.rotate(self.model.list_image_anypoint[1], cv2.ROTATE_90_COUNTERCLOCKWISE)
        images[2] = cv2.rotate(self.model.list_image_anypoint[2], cv2.ROTATE_90_CLOCKWISE)
        images[3] = cv2.rotate(self.model.list_image_anypoint[3], cv2.ROTATE_180)
        for i in range(len(self.model.list_image_anypoint)):
            image_crop.append(self.cropping_anypoint_image(images[i], i))
        self.model.list_data_selected_point = image_crop

    def change_mode(self, value):
        self.mode = value

    def load_config(self, config_path):
        with open(config_path, "r") as file:
            data_config = yaml.safe_load(file)
        self.model.properties_image = data_config
        print("load config success")

    def save_config(self):
        with open("../data_config/config.yaml", "w") as outfile:
            yaml.dump(self.model.properties_image, outfile, default_flow_style=False)
            print("save config success")

    def cropping_anypoint_image(self, image, i):
        keys = list(self.model.properties_image)
        top = self.model.properties_image[keys[i]]["bird_view"]["crop_top"]
        bottom = self.model.properties_image[keys[i]]["bird_view"]["crop_bottom"]
        left = self.model.properties_image[keys[i]]["bird_view"]["crop_left"]
        right = self.model.properties_image[keys[i]]["bird_view"]["crop_right"]
        return image[top:image.shape[0] - bottom, left: image.shape[1] - right]

    def remap_additional(self, image, i, main_mode, maps_x, maps_y):
        keys = list(self.model.properties_image)
        return remap_image(image,
                           np.load(self.model.properties_image[keys[i]][main_mode][maps_x]),
                           np.load(self.model.properties_image[keys[i]][main_mode][maps_y]))

    def create_list_anypoint_image(self, i):
        keys = list(self.model.properties_image)
        self.model.list_image_anypoint[i] = remap_image(
            self.model.image_original[i],
            np.load(self.model.properties_image[keys[i]]["bird_view"]["map_x_anypoint"]),
            np.load(self.model.properties_image[keys[i]]["bird_view"]["map_y_anypoint"]))

    def crop_surrounding_image_view(self, image, i):
        keys = list(self.model.properties_image)
        return cropping_image(image,
                              self.model.properties_image[keys[i]]["surrounding_view"][
                                  "crop_right"],
                              self.model.properties_image[keys[i]]["surrounding_view"][
                                  "crop_bottom"],
                              self.model.properties_image[keys[i]]["surrounding_view"][
                                  "crop_left"],
                              self.model.properties_image[keys[i]]["surrounding_view"][
                                  "crop_top"])
