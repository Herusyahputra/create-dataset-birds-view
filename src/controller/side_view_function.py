import numpy as np


class SideView:
    def __init__(self, controller):
        self.controller = controller

    def create_maps(self, i):
        keys = list(self.controller.model.properties_image)
        alpha = self.controller.model.properties_image[keys[i]]["side_view"]["icx"]
        beta = self.controller.model.properties_image[keys[i]]["side_view"]["icy"]
        rotate = self.controller.model.properties_image[keys[i]]["side_view"]["rotate"]
        zoom = self.controller.model.properties_image[keys[i]]["side_view"]["zoom"]

        map_x_anypoint, map_y_anypoint = self.controller.moildev[i].maps_anypoint_car(alpha, beta, rotate, zoom)
        path_map_x_anypoint = "../data_config/maps/map_x_side_anypoint_image_" + str(i) + ".npy"
        path_map_y_anypoint = "../data_config/maps/map_y_side_anypoint_image_" + str(i) + ".npy"
        np.save(path_map_x_anypoint, map_x_anypoint)
        np.save(path_map_y_anypoint, map_y_anypoint)
        self.controller.model.properties_image[keys[i]]["side_view"]["side_x_anypoint"] = path_map_x_anypoint
        self.controller.model.properties_image[keys[i]]["side_view"]["side_y_anypoint"] = path_map_y_anypoint
