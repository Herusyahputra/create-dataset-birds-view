from .additional_function import show_image_to_label


class ShowToUi:
    def __init__(self, main_view):
        super(ShowToUi, self).__init__()
        self.main_view = main_view

    def show_to_window(self):
        current_index = self.main_view.main_ui.stackedWidget.currentIndex()
        mode = self.main_view.main_controller.mode
        if mode == "original":
            image = self.main_view.main_model.image_original

        elif mode == "calibration_wide_view":
            index = self.main_view.main_ui.comboBox_image_wide.currentIndex()
            self.main_view.main_controller.current_image_calib = index
            image = self.main_view.main_model.list_image_wide_view[index]

        elif mode == "front_wide":
            image = self.main_view.main_model.list_image_wide_view[0]
        elif mode == "left_wide":
            image = self.main_view.main_model.list_image_wide_view[1]
        elif mode == "rear_wide":
            image = self.main_view.main_model.list_image_wide_view[3]
        elif mode == "right_wide":
            image = self.main_view.main_model.list_image_wide_view[2]

        elif mode == "front_bird_view":
            image = self.main_view.main_model.image_bird_view_cropping
        elif mode == "left_right_bird_view":
            image = self.main_view.main_model.image_bird_view_cropping
        elif mode == "rear_bird_view":
            image = self.main_view.main_model.image_bird_view_cropping

        elif mode == "calibration_surrounding_view":
            index = self.main_view.main_ui.comboBox_image_calib_surrounding_view.currentIndex()
            self.main_view.main_controller.current_image_calib = index
            image = self.main_view.main_model.list_image_surrounding[index]

        elif mode == "surrounding_view":
            image = self.main_view.main_model.image_surrounding
        elif mode == "front_surrounding_view":
            image = self.main_view.main_model.list_image_surrounding[0]
        elif mode == "left_right_surrounding_view":
            image = self.main_view.main_model.image_surrounding
        elif mode == "rear_surrounding_view":
            image = self.main_view.main_model.list_image_surrounding[3]

        elif mode == "calibration_side_view":
            index = self.main_view.main_ui.comboBox_image_side.currentIndex()
            self.main_view.main_controller.current_image_calib = index
            if index == 1 or index == 2:
                image = self.main_view.main_model.image_side_view
            else:
                image = self.main_view.main_model.list_image_side_view[index]

        elif mode == "side_left_right_view":
            image = self.main_view.main_model.image_side_view

        else:
            image = self.main_view.main_model.image_original[0]

        if current_index == 0:
            for i in range(len(image)):
                if image[i] is not None:
                    show_image_to_label(self.main_view.label[i], image[i], 320)
                else:
                    self.main_view.label[i].setText("No Available")

        elif current_index == 1:
            if image is None:
                self.main_view.main_ui.image_view.setText("No Available")
            elif image is not None:
                show_image_to_label(self.main_view.main_ui.image_view, image, 696)

            image_bird = self.main_view.main_model.image_bird_view
            if image_bird is not None:
                show_image_to_label(self.main_view.main_ui.show_bird_views, image_bird, 300)

        elif current_index == 3:  # calibration bird view
            image_bird_view = self.main_view.main_model.image_bird_view
            image_bird_view_overlay = self.main_view.main_model.image_bird_view_overlay
            if image_bird_view is not None and image_bird_view_overlay is not None:
                show_image_to_label(self.main_view.main_ui.birds_view_bird, image_bird_view, 400)
                show_image_to_label(self.main_view.main_ui.overlay_image_bird, image_bird_view_overlay, 400)

        elif current_index == 4 or mode == "calibration_surrounding_view":  # calibration surrounding view
            if image is not None:
                show_image_to_label(self.main_view.main_ui.overlay_image_calib_surrounding_view, image, 696)

        elif current_index == 5 or mode == "calibration_wide_view":  # calibration wide view
            if image is not None:
                show_image_to_label(self.main_view.main_ui.overlay_image_wide, image,
                                    696)

        elif current_index == 6:  # calibration side view
            if image is not None:
                show_image_to_label(self.main_view.main_ui.overlay_image_side, image,
                                    696)
