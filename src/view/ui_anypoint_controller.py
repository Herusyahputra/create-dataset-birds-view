class AnypointConfiguration:
    def __init__(self, main_view):
        self.view = main_view
        self.connect()

    def connect(self):
        # page_calibration_bird_view
        self.view.main_ui.comboBox_image_bird.currentIndexChanged.connect(self.load_config_to_ui)
        self.view.main_ui.alpha_bird.valueChanged.connect(self.change_properties_anypoint)
        self.view.main_ui.beta_bird.valueChanged.connect(self.change_properties_anypoint)
        self.view.main_ui.zoom_bird.valueChanged.connect(self.change_properties_anypoint)
        self.view.main_ui.rotate_bird.valueChanged.connect(self.change_properties_anypoint)
        self.view.main_ui.x_axis_bird.valueChanged.connect(self.change_properties_overlay)
        self.view.main_ui.y_axis_bird.valueChanged.connect(self.change_properties_overlay)
        self.view.main_ui.crop_top_bird.valueChanged.connect(self.change_properties_cropping)
        self.view.main_ui.crop_bottom_bird.valueChanged.connect(self.change_properties_cropping)
        self.view.main_ui.crop_left_bird.valueChanged.connect(self.change_properties_cropping)
        self.view.main_ui.crop_right_bird.valueChanged.connect(self.change_properties_cropping)

        # page_calibration_surrounding_view
        self.view.main_ui.comboBox_image_calib_surrounding_view.currentIndexChanged.connect(self.load_config_to_ui)
        self.view.main_ui.alpha_max_calib_surroounding_view.valueChanged.connect(self.change_properties_anypoint)
        self.view.main_ui.alpha_calib_surroounding_view.valueChanged.connect(self.change_properties_anypoint)
        self.view.main_ui.beta_calib_surrounding_view.valueChanged.connect(self.change_properties_anypoint)

    def change_properties_anypoint(self):
        """
        The change_properties_anypoint_image_1 function will be used control zoom & rotate
        each acton of the part image 1 in the user interface frame
        """
        index = self.view.main_ui.comboBox_image.currentIndex()
        keys = list(self.view.main_model.properties_image)
        self.view.main_model.properties_image[keys[index]]["bird_view"]["icx"] = self.view.main_ui.spinBox_icx.value()
        self.view.main_model.properties_image[keys[index]]["bird_view"]["icy"] = self.view.main_ui.spinBox_icy.value()
        self.view.main_model.properties_image[keys[index]]["bird_view"]["rotate"] = self.view.main_ui.doubleSpinBox_rotate.value()
        self.view.main_model.properties_image[keys[index]]["bird_view"]["zoom"] = self.view.main_ui.doubleSpinBox_zoom.value()
        self.view.main_controller.bird_view.create_maps(index)

    def change_properties_overlay(self):
        """
        The change_properties_overlay_image_1 function will be used control shift_x & shift_y
        each acton of the part image 1 in the user interface frame
        """
        index = self.view.main_ui.comboBox_image.currentIndex()
        keys = list(self.view.main_model.properties_image)
        self.view.main_model.properties_image[keys[index]]["bird_view"]["shift_x"] = self.view.main_ui.spinBox_x_axis.value()
        self.view.main_model.properties_image[keys[index]]["bird_view"]["shift_y"] = self.view.main_ui.spinBox_y_axis.value()

    def change_properties_cropping(self):
        """
        The change_properties_cropping_image_1 function will be used control crop_top, crop_bottom,
        crop_left & crop_right each acton of the part image 1 in the user interface frame
        """
        index = self.view.main_ui.comboBox_image.currentIndex()
        keys = list(self.view.main_model.properties_image)
        self.view.main_model.properties_image[keys[index]]["bird_view"]["crop_top"] = self.view.main_ui.spinBox_crop_top.value()
        self.view.main_model.properties_image[keys[index]]["bird_view"]["crop_bottom"] = self.view.main_ui.spinBox_crop_bottom.value()
        self.view.main_model.properties_image[keys[index]]["bird_view"]["crop_left"] = self.view.main_ui.spinBox_crop_left.value()
        self.view.main_model.properties_image[keys[index]]["bird_view"]["crop_right"] = self.view.main_ui.spinBox_crop_right.value()

        # self.view_controller.show_to_window.show_overlay_and_birds_view()

    def load_config_to_ui(self):
        index = self.view.main_ui.comboBox_image_bird.currentIndex()
        keys = list(self.view.main_model.properties_image)
        self.block_signal()
        self.view.main_ui.alpha_bird.setValue(self.view.main_model.properties_image[keys[index]]["bird_view"]["icx"])
        self.view.main_ui.beta_bird.setValue(self.view.main_model.properties_image[keys[index]]["bird_view"]["icy"])
        self.view.main_ui.zoom_bird.setValue(self.view.main_model.properties_image[keys[index]]["bird_view"]["zoom"])
        self.view.main_ui.rotate_bird.setValue(self.view.main_model.properties_image[keys[index]]["bird_view"]["rotate"])
        self.view.main_ui.x_axis_bird.setValue(self.view.main_model.properties_image[keys[index]]["bird_view"]["shift_x"])
        self.view.main_ui.y_axis_bird.setValue(self.view.main_model.properties_image[keys[index]]["bird_view"]["shift_y"])
        self.view.main_ui.crop_top_bird.setValue(self.view.main_model.properties_image[keys[index]]["bird_view"]["crop_top"])
        self.view.main_ui.crop_bottom_bird.setValue(self.view.main_model.properties_image[keys[index]]["bird_view"]["crop_bottom"])
        self.view.main_ui.crop_left_bird.setValue(self.view.main_model.properties_image[keys[index]]["bird_view"]["crop_left"])
        self.view.main_ui.crop_right_bird.setValue(self.view.main_model.properties_image[keys[index]]["bird_view"]["crop_right"])
        self.unblock_signal()

    def block_signal(self):
        self.view.main_ui.alpha_bird.blockSignals(True)
        self.view.main_ui.beta_bird.blockSignals(True)
        self.view.main_ui.zoom_bird.blockSignals(True)
        self.view.main_ui.rotate_bird.blockSignals(True)
        self.view.main_ui.x_axis_bird.blockSignals(True)
        self.view.main_ui.y_axis_bird.blockSignals(True)
        self.view.main_ui.crop_top_bird.blockSignals(True)
        self.view.main_ui.crop_bottom_bird.blockSignals(True)
        self.view.main_ui.crop_left_bird.blockSignals(True)
        self.view.main_ui.crop_right_bird.blockSignals(True)

    def unblock_signal(self):
        self.view.main_ui.alpha_bird.blockSignals(False)
        self.view.main_ui.beta_bird.blockSignals(False)
        self.view.main_ui.zoom_bird.blockSignals(False)
        self.view.main_ui.rotate_bird.blockSignals(False)
        self.view.main_ui.x_axis_bird.blockSignals(False)
        self.view.main_ui.y_axis_bird.blockSignals(False)
        self.view.main_ui.crop_top_bird.blockSignals(False)
        self.view.main_ui.crop_bottom_bird.blockSignals(False)
        self.view.main_ui.crop_left_bird.blockSignals(False)
        self.view.main_ui.crop_right_bird.blockSignals(False)
