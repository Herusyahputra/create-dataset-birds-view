import cv2
import numpy as np


class BirdView:
    def __init__(self, controller):
        self.controller = controller

    def create_maps(self, i):
        keys = list(self.controller.model.properties_image)
        rotate = self.controller.model.properties_image[keys[i]]["bird_view"]["rotate"]
        zoom = self.controller.model.properties_image[keys[i]]["bird_view"]["zoom"]
        alpha = self.controller.model.properties_image[keys[i]]["bird_view"]["icx"]
        beta = self.controller.model.properties_image[keys[i]]["bird_view"]["icy"]

        map_x_anypoint, map_y_anypoint = self.controller.moildev[i].maps_anypoint_car(alpha, beta, rotate, zoom)
        path_map_x_anypoint = "../data_config/maps/map_x_anypoint_image_" + str(i) + ".npy"
        path_map_y_anypoint = "../data_config/maps/map_y_anypoint_image_" + str(i) + ".npy"
        np.save(path_map_x_anypoint, map_x_anypoint)
        np.save(path_map_y_anypoint, map_y_anypoint)
        self.controller.model.properties_image[keys[i]]["bird_view"]["map_x_anypoint"] = path_map_x_anypoint
        self.controller.model.properties_image[keys[i]]["bird_view"]["map_y_anypoint"] = path_map_y_anypoint

    def crop_image_view(self, mode, merge_image):
        if mode == "front_bird_view":
            bottom = self.controller.model.properties_image["Image_1"]["bird_view"]["crop_bottom"]
            image = self.controller.model.list_image_anypoint[0]
            image = merge_image[0:image.shape[0] - bottom, 0: image.shape[1]]
        elif mode == "left_right_bird_view":
            image0 = cv2.rotate(self.controller.model.list_image_anypoint[1], cv2.ROTATE_90_COUNTERCLOCKWISE)
            image1 = cv2.rotate(self.controller.model.list_image_anypoint[2], cv2.ROTATE_90_CLOCKWISE)
            image = np.zeros([(max(image0.shape[0], image1.shape[0])), (image0.shape[1] + image1.shape[1]) + 50,
                              3], dtype=np.uint8)
            image[0:image0.shape[0], 0:image0.shape[1]] = image0
            image[0:image1.shape[0], image0.shape[1] + 50:image0.shape[1] + 50 + image1.shape[1]] = image1

        elif mode == "rear_bird_view":
            crop_top = self.controller.model.properties_image["Image_4"]["bird_view"]["crop_top"]
            image = self.controller.model.list_image_anypoint[3]
            image = merge_image[merge_image.shape[0] - image.shape[0] + crop_top:merge_image.shape[0],
                    0: image.shape[1]]
            image = cv2.rotate(image, cv2.ROTATE_180)
        else:
            image = None
        return image
