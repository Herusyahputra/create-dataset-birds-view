class WideViewConfiguration:
    def __init__(self, main_view):
        self.view = main_view
        self.connect()

    def connect(self):
        self.view.main_ui.comboBox_image_wide.currentIndexChanged.connect(self.load_config_to_ui)
        self.view.main_ui.alpha_wide.valueChanged.connect(self.change_properties_anypoint)
        self.view.main_ui.beta_wide.valueChanged.connect(self.change_properties_anypoint)
        self.view.main_ui.zoom_wide.valueChanged.connect(self.change_properties_anypoint)
        self.view.main_ui.rotate_wide.valueChanged.connect(self.change_properties_anypoint)
        self.view.main_ui.btn_close_wide.clicked.connect(self.view.onclick_close)
        self.view.main_ui.btn_save_wide.clicked.connect(self.view.main_controller.save_config)

    def change_properties_anypoint(self):
        """
        The change_properties_anypoint_image_1 function will be used control zoom & rotate
        each acton of the part image 1 in the user interface frame
        """
        index = self.view.main_ui.comboBox_image_wide.currentIndex()
        keys = list(self.view.main_model.properties_image)
        self.view.main_model.properties_image[keys[index]]["wide_view"]["icx"] = self.view.main_ui.alpha_wide.value()
        self.view.main_model.properties_image[keys[index]]["wide_view"]["icy"] = self.view.main_ui.beta_wide.value()
        self.view.main_model.properties_image[keys[index]]["wide_view"]["rotate"] = self.view.main_ui.rotate_wide.value()
        self.view.main_model.properties_image[keys[index]]["wide_view"]["zoom"] = self.view.main_ui.zoom_wide.value()
        self.view.main_controller.wide_view.create_maps(index)

    def load_config_to_ui(self):
        index = self.view.main_ui.comboBox_image_wide.currentIndex()
        keys = list(self.view.main_model.properties_image)
        self.block_signal()
        self.view.main_ui.alpha_wide.setValue(self.view.main_model.properties_image[keys[index]]["wide_view"]["icx"])
        self.view.main_ui.beta_wide.setValue(self.view.main_model.properties_image[keys[index]]["wide_view"]["icy"])
        self.view.main_ui.zoom_wide.setValue(self.view.main_model.properties_image[keys[index]]["wide_view"]["zoom"])
        self.view.main_ui.rotate_wide.setValue(self.view.main_model.properties_image[keys[index]]["wide_view"]["rotate"])
        self.unblock_signal()

    def block_signal(self):
        self.view.main_ui.alpha_wide.blockSignals(True)
        self.view.main_ui.beta_wide.blockSignals(True)
        self.view.main_ui.zoom_wide.blockSignals(True)
        self.view.main_ui.rotate_wide.blockSignals(True)

    def unblock_signal(self):
        self.view.main_ui.alpha_wide.blockSignals(False)
        self.view.main_ui.beta_wide.blockSignals(False)
        self.view.main_ui.zoom_wide.blockSignals(False)
        self.view.main_ui.rotate_wide.blockSignals(False)
