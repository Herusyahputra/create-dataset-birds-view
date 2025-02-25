import cv2
from PyQt5.QtWidgets import QMessageBox, QLabel
from PyQt5 import QtCore
from .additional_function import show_image_to_label, draw_list_point_with_text, init_ori_ratio, calculate_height


class SelectCoordinate:
    def __init__(self, main_view):
        super(SelectCoordinate, self).__init__()
        self.main_view = main_view
        self.keys_properties = 0
        self.i = 0
        self.number_of_point = 0

        self.list_point_image = {"front_left": {}, "front_right": {}, "left_front": {}, "left_rear": {},
                                 "right_front": {}, "right_rear": {}, "rear_left": {}, "rear_right": {}}

        self.keys_image = list(self.list_point_image)
        self.list_point_image["front_left"] = []
        self.image = None
        self.width = 800

        self.add_label_for_zoom()
        self.main_view.main_ui.comboBox_image_bird.currentIndexChanged.connect(self.change_image)
        self.main_view.main_ui.label_image_selected_point.mousePressEvent = self.mouse_event
        self.main_view.main_ui.label_image_selected_point.mouseMoveEvent = self.mouse_moved_event

    def set_data_image(self):
        self.image = self.main_view.main_model.list_data_selected_point[0]
        self.show_image()

    def change_image(self):
        index = self.main_view.main_ui.comboBox_image_bird.currentIndex()
        self.image = self.main_view.main_model.list_data_selected_point[index]
        self.show_image()

    def add_label_for_zoom(self):
        self.addition_label = QLabel(self.main_view.main_ui.label_image_selected_point)
        self.addition_label.setGeometry(QtCore.QRect(5, 5, 100, 100))
        self.addition_label.setFrameShape(QLabel.Shape.Box)
        self.addition_label.setFrameShadow(QLabel.Shadow.Raised)
        self.addition_label.hide()

    def mouse_moved_event(self, e):
        pos_x = round(e.x())
        pos_y = round(e.y())
        ratio_x, ratio_y = init_ori_ratio(self.main_view.main_ui.label_image_selected_point, self.image)
        X = round(pos_x * ratio_x)
        Y = round(pos_y * ratio_y)
        if X > 70 and Y > 70:
            self.addition_label.show()
            self.addition_label.setGeometry(QtCore.QRect(pos_x + 15, pos_y - 15, 100, 100))
            if self.main_view.main_ui.label_image_selected_point.height() - pos_y < 200:
                self.addition_label.setGeometry(QtCore.QRect(pos_x + 15, pos_y - 150, 100, 100))

            if self.main_view.main_ui.label_image_selected_point.width() - pos_x < 200:
                self.addition_label.setGeometry(QtCore.QRect(pos_x - 150, pos_y + 15, 100, 100))

            if self.main_view.main_ui.label_image_selected_point.height() - pos_y < 200 and \
                    self.main_view.main_ui.label_image_selected_point.width() - pos_x < 200:
                self.addition_label.setGeometry(QtCore.QRect(pos_x - 150, pos_y - 150, 100, 100))

            if self.main_view.main_ui.label_image_selected_point.height() - pos_y < 20 and \
                    self.main_view.main_ui.label_image_selected_point.width() - pos_x < 20:
                self.addition_label.hide()
            image_ = cv2.circle(self.image.copy(), (X, Y), 2, (200, 5, 200), -1)
            image = image_[Y - 70: (Y - 70) + 140, X - 70:(X - 70) + 140]
            show_image_to_label(self.addition_label, image, 140)

        else:
            self.addition_label.hide()

    def mouse_event(self, e):
        if e.button() == QtCore.Qt.MouseButton.LeftButton:
            pos_x = round(e.x())
            pos_y = round(e.y())
            if self.number_of_point == 4:
                self.number_of_point = 0

            self.number_of_point += 1
            self.config_coordinate(pos_x, pos_y)

    def config_coordinate(self, pos_x=None, pos_y=None):
        if pos_x is not None and pos_y is not None:
            ratio_x, ratio_y = init_ori_ratio(self.main_view.main_ui.label_image_selected_point, self.image)
            X = round(pos_x * ratio_x)
            Y = round(pos_y * ratio_y)
            self.point_selection(X, Y)

    def point_selection(self, X=None, Y=None):
        key_image = list(self.main_view.main_model.properties_image)
        if self.number_of_point == 0:
            self.main_view.main_ui.label_status_bar_bird.setText(self.keys_image[self.i] + " select point 1")
        elif self.number_of_point == 1:
            self.list_point_image[self.keys_image[self.i]].append([X, Y])
            self.main_view.main_ui.label_status_bar_bird.setText(self.keys_image[self.i] + " select point 2")
        elif self.number_of_point == 2:
            self.list_point_image[self.keys_image[self.i]].append([X, Y])
            self.main_view.main_ui.label_status_bar_bird.setText(self.keys_image[self.i] + " select point 3")
        elif self.number_of_point == 3:
            self.list_point_image[self.keys_image[self.i]].append([X, Y])
            self.main_view.main_ui.label_status_bar_bird.setText(self.keys_image[self.i] + " select point 4")
        elif self.number_of_point == 4:
            if self.i < 7:
                self.list_point_image[self.keys_image[self.i]].append([X, Y])
                self.main_view.main_ui.label_status_bar_bird.setText(self.keys_image[self.i + 1] + " select point 1")
                self.show_image()
                self.list_point_image[self.keys_image[self.i + 1]] = []
                self.i += 1

                if self.i == 0 or self.i == 1:
                    # self.width = 800
                    self.image = self.main_view.main_model.list_data_selected_point[0]
                    self.keys_properties = 0

                elif self.i == 2 or self.i == 3:
                    # self.width = 800
                    self.image = self.main_view.main_model.list_data_selected_point[1]
                    self.keys_properties = 1

                elif self.i == 4 or self.i == 5:
                    # self.width = 800
                    self.image = self.main_view.main_model.list_data_selected_point[2]
                    self.keys_properties = 2

                elif self.i == 6 or self.i == 7:
                    # self.width = 800
                    self.image = self.main_view.main_model.list_data_selected_point[3]
                    self.keys_properties = 3

                else:
                    self.width = None
                    self.image = None

            else:
                self.list_point_image[self.keys_image[self.i]].append([X, Y])
                QMessageBox.information(None, "Info", "Finish !!!")
                self.main_view.main_model.properties_image[key_image[self.keys_properties]][self.keys_image[self.i]] = \
                    self.list_point_image[self.keys_image[self.i]]
                self.main_view.main_ui.label_status_bar_bird.setText("Select Point Finish")
                self.show_image()
                self.main_view.main_ui.scroll_area_select_point.hide()
                self.main_view.main_ui.frame_calib_birds_view.show()
                self.combine_with_properties()
                self.main_view.main_controller.control_perspective.fill_data_src()
                print(self.list_point_image)
                self.main_view.timer.start()
                self.main_view.main_ui.label_status_bar_bird.setText("Calibration Birds view")

        self.main_view.main_model.properties_image[key_image[self.keys_properties]][self.keys_image[self.i]] = \
            self.list_point_image[self.keys_image[self.i]]
        self.show_image()

    def show_image(self):
        image = draw_list_point_with_text(self.image, self.list_point_image[self.keys_image[self.i]], 5)
        show_image_to_label(self.main_view.main_ui.label_image_selected_point, image, self.width)

    def combine_with_properties(self):
        self.main_view.main_model.properties_image["Image_1"]["bird_view"]["src"] = [
            self.list_point_image["front_left"][0],
            self.list_point_image["front_right"][1],
            self.list_point_image["front_right"][2],
            self.list_point_image["front_left"][3]]

        self.main_view.main_model.properties_image["Image_2"]["bird_view"]["src"] = [
            self.list_point_image["left_front"][0],
            self.list_point_image["left_front"][1],
            self.list_point_image["left_rear"][2],
            self.list_point_image["left_rear"][3]]

        self.main_view.main_model.properties_image["Image_3"]["bird_view"]["src"] = [
            self.list_point_image["right_front"][0],
            self.list_point_image["right_front"][1],
            self.list_point_image["right_rear"][2],
            self.list_point_image["right_rear"][3]]

        self.main_view.main_model.properties_image["Image_4"]["bird_view"]["src"] = [
            self.list_point_image["rear_left"][0],
            self.list_point_image["rear_right"][1],
            self.list_point_image["rear_right"][2],
            self.list_point_image["rear_left"][3]]
