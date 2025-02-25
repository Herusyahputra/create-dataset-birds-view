class SurroundingViewConfiguration:
    def __init__(self, main_view):
        self.view = main_view
        self.connect()

    def connect(self):
        self.view.main_ui.comboBox_image_calib_surrounding_view.currentIndexChanged.connect(self.load_config_to_ui)

        self.view.main_ui.alpha_max_calib_surroounding_view.valueChanged.connect(self.change_properties_panorama)
        self.view.main_ui.alpha_calib_surroounding_view.valueChanged.connect(self.change_properties_panorama)
        self.view.main_ui.beta_calib_surrounding_view.valueChanged.connect(self.change_properties_panorama)
        self.view.main_ui.alpha_from_calib_surrounding_view.valueChanged.connect(self.change_properties_panorama)
        self.view.main_ui.alpha_end_calib_surrounding_view.valueChanged.connect(self.change_properties_panorama)

        self.view.main_ui.left_calib_surrouding_view.valueChanged.connect(self.change_properties_cropping)
        self.view.main_ui.top_calib_surrounding_view.valueChanged.connect(self.change_properties_cropping)
        self.view.main_ui.right_calib_surrounding_view.valueChanged.connect(self.change_properties_cropping)
        self.view.main_ui.buttom_calib_surrounding_view.valueChanged.connect(self.change_properties_cropping)

        self.view.main_ui.btn_close_calib_surrounding_view.clicked.connect(self.view.onclick_close)
        self.view.main_ui.btn_save_calib_surrounding_view.clicked.connect(self.view.main_controller.save_config)

    def change_properties_panorama(self):
        """
        The change_properties_anypoint_image_1 function will be used control zoom & rotate
        each acton of the part image 1 in the user interface frame
        """
        index = self.view.main_ui.comboBox_image_calib_surrounding_view.currentIndex()
        keys = list(self.view.main_model.properties_image)
        self.view.main_model.properties_image[keys[index]]["surrounding_view"]["alpha_max"] = self.view.main_ui.alpha_max_calib_surroounding_view.value()
        self.view.main_model.properties_image[keys[index]]["surrounding_view"]["iC_alpha_degree"] = self.view.main_ui.alpha_calib_surroounding_view.value()
        self.view.main_model.properties_image[keys[index]]["surrounding_view"]["iC_beta_degree"] = self.view.main_ui.beta_calib_surrounding_view.value()
        self.view.main_model.properties_image[keys[index]]["surrounding_view"]["p_alpha_from"] = self.view.main_ui.alpha_from_calib_surrounding_view.value()
        self.view.main_model.properties_image[keys[index]]["surrounding_view"]["p_alpha_end"] = self.view.main_ui.alpha_end_calib_surrounding_view.value()
        self.view.main_controller.surrounding_function.create_maps(index)

    def change_properties_cropping(self):
        """
        The change_properties_cropping_image_1 function will be used control crop_top, crop_bottom,
        crop_left & crop_right each acton of the part image 1 in the user interface frame
        """
        index = self.view.main_ui.comboBox_image_calib_surrounding_view.currentIndex()
        keys = list(self.view.main_model.properties_image)
        self.view.main_model.properties_image[keys[index]]["surrounding_view"]["crop_top"] = self.view.main_ui.top_calib_surrounding_view.value()
        self.view.main_model.properties_image[keys[index]]["surrounding_view"]["crop_bottom"] = self.view.main_ui.buttom_calib_surrounding_view.value()
        self.view.main_model.properties_image[keys[index]]["surrounding_view"]["crop_left"] = self.view.main_ui.left_calib_surrouding_view.value()
        self.view.main_model.properties_image[keys[index]]["surrounding_view"]["crop_right"] = self.view.main_ui.right_calib_surrounding_view.value()
        # self.view.main_controller.update_list_image_surrounding_view(index)

    def load_config_to_ui(self):
        index = self.view.main_ui.comboBox_image_calib_surrounding_view.currentIndex()
        keys = list(self.view.main_model.properties_image)
        self.block_signal()

        self.view.main_ui.alpha_max_calib_surroounding_view.setValue(self.view.main_model.properties_image[keys[index]]["surrounding_view"]["alpha_max"])
        self.view.main_ui.alpha_calib_surroounding_view.setValue(self.view.main_model.properties_image[keys[index]]["surrounding_view"]["iC_alpha_degree"])
        self.view.main_ui.beta_calib_surrounding_view.setValue(self.view.main_model.properties_image[keys[index]]["surrounding_view"]["iC_beta_degree"])
        self.view.main_ui.alpha_from_calib_surrounding_view.setValue(self.view.main_model.properties_image[keys[index]]["surrounding_view"]["p_alpha_from"])
        self.view.main_ui.alpha_end_calib_surrounding_view.setValue(self.view.main_model.properties_image[keys[index]]["surrounding_view"]["p_alpha_end"])

        self.view.main_ui.left_calib_surrouding_view.setValue(self.view.main_model.properties_image[keys[index]]["surrounding_view"]["crop_left"])
        self.view.main_ui.top_calib_surrounding_view.setValue(self.view.main_model.properties_image[keys[index]]["surrounding_view"]["crop_top"])
        self.view.main_ui.right_calib_surrounding_view.setValue(self.view.main_model.properties_image[keys[index]]["surrounding_view"]["crop_right"])
        self.view.main_ui.buttom_calib_surrounding_view.setValue(self.view.main_model.properties_image[keys[index]]["surrounding_view"]["crop_bottom"])

        self.unblock_signal()

    def block_signal(self):
        self.view.main_ui.alpha_max_calib_surroounding_view.blockSignals(True)
        self.view.main_ui.alpha_calib_surroounding_view.blockSignals(True)
        self.view.main_ui.beta_calib_surrounding_view.blockSignals(True)
        self.view.main_ui.left_calib_surrouding_view.blockSignals(True)
        self.view.main_ui.top_calib_surrounding_view.blockSignals(True)
        self.view.main_ui.buttom_calib_surrounding_view.blockSignals(True)
        self.view.main_ui.alpha_from_calib_surrounding_view.blockSignals(True)
        self.view.main_ui.alpha_end_calib_surrounding_view.blockSignals(True)
        self.view.main_ui.right_calib_surrounding_view.blockSignals(True)

    def unblock_signal(self):
        self.view.main_ui.alpha_max_calib_surroounding_view.blockSignals(False)
        self.view.main_ui.alpha_calib_surroounding_view.blockSignals(False)
        self.view.main_ui.beta_calib_surrounding_view.blockSignals(False)
        self.view.main_ui.left_calib_surrouding_view.blockSignals(False)
        self.view.main_ui.top_calib_surrounding_view.blockSignals(False)
        self.view.main_ui.buttom_calib_surrounding_view.blockSignals(False)
        self.view.main_ui.alpha_from_calib_surrounding_view.blockSignals(False)
        self.view.main_ui.alpha_end_calib_surrounding_view.blockSignals(False)
        self.view.main_ui.right_calib_surrounding_view.blockSignals(False)

