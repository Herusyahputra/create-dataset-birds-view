import numpy as np


class SurroundingImage:
    def __init__(self, controller):
        self.controller = controller

    def create_maps(self, i):
        keys = list(self.controller.model.properties_image)
        alpha_max = self.controller.model.properties_image[keys[i]]["surrounding_view"]["alpha_max"]
        ic_alpha_degree = self.controller.model.properties_image[keys[i]]["surrounding_view"]["iC_alpha_degree"]
        ic_beta_degree = self.controller.model.properties_image[keys[i]]["surrounding_view"]["iC_beta_degree"]
        p_alpha_from = self.controller.model.properties_image[keys[i]]["surrounding_view"]["p_alpha_from"]
        p_alpha_end = self.controller.model.properties_image[keys[i]]["surrounding_view"]["p_alpha_end"]

        maps_x, maps_y = self.controller.moildev[i].maps_x_panorama_rotation(alpha_max, ic_alpha_degree,
                                                                             ic_beta_degree,
                                                                             p_alpha_from, p_alpha_end)
        path_x = "../data_config/maps/map_x_panorama_rotation_" + str(i) + ".npy"
        path_y = "../data_config/maps/map_y_panorama_rotation_" + str(i) + ".npy"
        np.save(path_x, maps_x)
        np.save(path_y, maps_y)
        self.controller.model.properties_image[keys[i]]["surrounding_view"]["map_x_panorama_rotation"] = path_x
        self.controller.model.properties_image[keys[i]]["surrounding_view"]["map_y_panorama_rotation"] = path_y
