import cv2
import numpy as np
import yaml


class PerspectiveView:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.data_dst = {"front": {}, "left": {}, "right": {}, "rear": {}}
        self.data_src = {"front": {}, "left": {}, "right": {}, "rear": {}}
        # self.data_dst["front"] = [[500, 500], [2000, 500], [2000, 800], [500, 800]]
        # self.data_dst["left"] = [[600, 350], [945, 300], [946, 2549], [600, 2549]]
        # self.data_dst["right"] = [[630, 350], [930, 350], [930, 2549], [630, 2549]]
        # self.data_dst["rear"] = [[500, 200], [2000, 200], [2000, 500], [500, 500]]
        # self.fill_data_src()

    def fill_data_src(self):
        keys = list(self.main_controller.model.properties_image)
        self.data_src["front"] = self.main_controller.model.properties_image[keys[0]]["bird_view"]["src"]
        self.data_src["left"] = self.main_controller.model.properties_image[keys[1]]["bird_view"]["src"]
        self.data_src["right"] = self.main_controller.model.properties_image[keys[2]]["bird_view"]["src"]
        self.data_src["rear"] = self.main_controller.model.properties_image[keys[3]]["bird_view"]["src"]

        self.data_dst["front"] = self.main_controller.model.properties_image[keys[0]]["bird_view"]["dst"]
        self.data_dst["left"] = self.main_controller.model.properties_image[keys[1]]["bird_view"]["dst"]
        self.data_dst["right"] = self.main_controller.model.properties_image[keys[2]]["bird_view"]["dst"]
        self.data_dst["rear"] = self.main_controller.model.properties_image[keys[3]]["bird_view"]["dst"]

        # self.data_src["front"] = [properties_image[keys[0]]["front_left"][0],
        #                           properties_image[keys[0]]["front_right"][1],
        #                           properties_image[keys[0]]["front_right"][2],
        #                           properties_image[keys[0]]["front_left"][3]]
        #
        # self.data_src["left"] = [properties_image[keys[1]]["left_front"][0],
        #                          properties_image[keys[1]]["left_front"][1],
        #                          properties_image[keys[1]]["left_rear"][2],
        #                          properties_image[keys[1]]["left_rear"][3]]
        #
        # self.data_src["right"] = [properties_image[keys[2]]["right_front"][0],
        #                           properties_image[keys[2]]["right_front"][1],
        #                           properties_image[keys[2]]["right_rear"][2],
        #                           properties_image[keys[2]]["right_rear"][3]]
        #
        # self.data_src["rear"] = [properties_image[keys[3]]["rear_left"][0],
        #                          properties_image[keys[3]]["rear_right"][1],
        #                          properties_image[keys[3]]["rear_right"][2],
        #                          properties_image[keys[3]]["rear_left"][3]]

        # with open("../data_config/config_position.yaml", "r") as file:
        #     data_config = yaml.safe_load(file)
        # self.data_src["front"] = data_config["src"]["front"]
        # self.data_src["left"] = data_config["src"]["left"]
        # self.data_src["right"] = data_config["src"]["right"]
        # self.data_src["rear"] = data_config["src"]["rear"]
        # self.data_dst["front"] = data_config["dst"]["front"]
        # self.data_dst["left"] = data_config["dst"]["left"]
        # self.data_dst["right"] = data_config["dst"]["right"]
        # self.data_dst["rear"] = data_config["dst"]["rear"]

    def process_perspective(self, image):
        image_crop = []
        images = [None] * len(image)
        images[0] = image[0]
        images[1] = cv2.rotate(image[1], cv2.ROTATE_90_COUNTERCLOCKWISE)
        images[2] = cv2.rotate(image[2], cv2.ROTATE_90_CLOCKWISE)
        images[3] = cv2.rotate(image[3], cv2.ROTATE_180)
        for i, img in enumerate(images):
            if i == 0:
                dst = self.data_dst["front"]
                src = self.data_src["front"]
            elif i == 1:
                dst = self.data_dst["left"]
                src = self.data_src["left"]
            elif i == 2:
                dst = self.data_dst["right"]
                src = self.data_src["right"]
            elif i == 3:
                dst = self.data_dst["rear"]
                src = self.data_src["rear"]
            src = np.float32(src)
            dst = np.float32(dst)
            image_perspective = self.perspective(img, src, dst)
            # self.draw_image_4_point(image_perspective, dst)
            image_crop.append(self.main_controller.cropping_anypoint_image(image_perspective, i))
        return image_crop

    @classmethod
    def perspective(cls, image, src, dst):
        matrix = cv2.getPerspectiveTransform(src, dst)
        return cv2.warpPerspective(image,
                                   matrix, (image.shape[1],
                                            image.shape[0]))

    @classmethod
    def draw_image_4_point(cls, image, list_point):
        pts = np.array(list_point, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 255), 10)
