class SideViewConfiguration:
    def __init__(self, main_view):
        self.view = main_view
        self.connect()

    def connect(self):
        self.view.main_ui.comboBox_image_side.currentIndexChanged.connect(self.load_config_to_ui)
        self.view.main_ui.alpha_side.valueChanged.connect(self.change_properties_anypoint)
        self.view.main_ui.beta_side.valueChanged.connect(self.change_properties_anypoint)
        self.view.main_ui.zoom_side.valueChanged.connect(self.change_properties_anypoint)
        self.view.main_ui.rotate_side.valueChanged.connect(self.change_properties_anypoint)
        self.view.main_ui.btn_close_side.clicked.connect(self.view.onclick_close)
        self.view.main_ui.btn_save_side.clicked.connect(self.view.main_controller.save_config)
        self.view.main_ui.crop_top_side.valueChanged.connect(self.change_properties_cropping)
        self.view.main_ui.crop_bottom_side.valueChanged.connect(self.change_properties_cropping)
        self.view.main_ui.crop_left_side.valueChanged.connect(self.change_properties_cropping)
        self.view.main_ui.crop_right_side.valueChanged.connect(self.change_properties_cropping)

    def change_properties_anypoint(self):
        """
        The change_properties_anypoint_image_1 function will be used control zoom & rotate
        each acton of the part image 1 in the user interface frame
        """
        index = self.view.main_ui.comboBox_image_side.currentIndex()
        keys = list(self.view.main_model.properties_image)
        self.view.main_model.properties_image[keys[index]]["side_view"]["icx"] = self.view.main_ui.alpha_side.value()
        self.view.main_model.properties_image[keys[index]]["side_view"]["icy"] = self.view.main_ui.beta_side.value()
        self.view.main_model.properties_image[keys[index]]["side_view"]["rotate"] = self.view.main_ui.rotate_side.value()
        self.view.main_model.properties_image[keys[index]]["side_view"]["zoom"] = self.view.main_ui.zoom_side.value()
        self.view.main_controller.side_view.create_maps(index)

    def change_properties_cropping(self):
        """
        The change_properties_cropping_image_1 function will be used control crop_top, crop_bottom,
        crop_left & crop_right each acton of the part image 1 in the user interface frame
        """
        index = self.view.main_ui.comboBox_image_side.currentIndex()
        keys = list(self.view.main_model.properties_image)
        self.view.main_model.properties_image[keys[index]]["side_view"]["crop_top"] = self.view.main_ui.crop_top_side.value()
        self.view.main_model.properties_image[keys[index]]["side_view"]["crop_bottom"] = self.view.main_ui.crop_bottom_side.value()
        self.view.main_model.properties_image[keys[index]]["side_view"]["crop_left"] = self.view.main_ui.crop_left_side.value()
        self.view.main_model.properties_image[keys[index]]["side_view"]["crop_right"] = self.view.main_ui.crop_right_side.value()

    def load_config_to_ui(self):
        index = self.view.main_ui.comboBox_image_side.currentIndex()
        keys = list(self.view.main_model.properties_image)
        self.block_signal()
        self.view.main_ui.alpha_side.setValue(self.view.main_model.properties_image[keys[index]]["side_view"]["icx"])
        self.view.main_ui.beta_side.setValue(self.view.main_model.properties_image[keys[index]]["side_view"]["icy"])
        self.view.main_ui.zoom_side.setValue(self.view.main_model.properties_image[keys[index]]["side_view"]["zoom"])
        self.view.main_ui.rotate_side.setValue(self.view.main_model.properties_image[keys[index]]["side_view"]["rotate"])
        self.unblock_signal()

    def block_signal(self):
        self.view.main_ui.alpha_side.blockSignals(True)
        self.view.main_ui.beta_side.blockSignals(True)
        self.view.main_ui.zoom_side.blockSignals(True)
        self.view.main_ui.rotate_side.blockSignals(True)

    def unblock_signal(self):
        self.view.main_ui.alpha_side.blockSignals(False)
        self.view.main_ui.beta_side.blockSignals(False)
        self.view.main_ui.zoom_side.blockSignals(False)
        self.view.main_ui.rotate_side.blockSignals(False)
