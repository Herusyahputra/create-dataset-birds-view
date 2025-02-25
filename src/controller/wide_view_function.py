import numpy as np


class WideView:
    def __init__(self, controller):
        self.controller = controller

    def create_maps(self, i):
        keys = list(self.controller.model.properties_image)
        alpha = self.controller.model.properties_image[keys[i]]["wide_view"]["icx"]
        beta = self.controller.model.properties_image[keys[i]]["wide_view"]["icy"]
        rotate = self.controller.model.properties_image[keys[i]]["wide_view"]["rotate"]
        zoom = self.controller.model.properties_image[keys[i]]["wide_view"]["zoom"]

        map_x_anypoint, map_y_anypoint = self.controller.moildev[i].maps_anypoint_car(alpha, beta, rotate, zoom)
        path_map_x_anypoint = "../data_config/maps/map_x_wide_anypoint_image_" + str(i) + ".npy"
        path_map_y_anypoint = "../data_config/maps/map_y_wide_anypoint_image_" + str(i) + ".npy"
        np.save(path_map_x_anypoint, map_x_anypoint)
        np.save(path_map_y_anypoint, map_y_anypoint)
        self.controller.model.properties_image[keys[i]]["wide_view"]["map_x_anypoint"] = path_map_x_anypoint
        self.controller.model.properties_image[keys[i]]["wide_view"]["map_y_anypoint"] = path_map_y_anypoint
