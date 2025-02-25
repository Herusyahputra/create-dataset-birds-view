from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow, QShortcut
from .ui_py.ui_main import Ui_MainWindow
from .show_to_ui import ShowToUi
from .ui_bird_view_controller import BirdViewConfiguration
from .ui_wide_controller import WideViewConfiguration
from .ui_side_controller import SideViewConfiguration
from .ui_surrounding_view_controller import SurroundingViewConfiguration
from .theme import *
from .resource_icon import *
from .set_icon_to_ui import SetIconToUi
from .status_bar import SetStatus
from .ui_show_selected_point import SelectCoordinate
from .ui_anypoint_controller import AnypointConfiguration


class MainView(QMainWindow):
    def __init__(self, model, controller):
        super().__init__()
        self.main_controller = controller
        self.main_model = model
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        status = SetStatus(self.main_ui)
        icon = SetIconToUi(self.main_ui)

        self.main_ui.centralwidget.setStyleSheet(Theme)

        self.show_to_window = ShowToUi(self)
        self.bird_view_config = BirdViewConfiguration(self)
        self.wide_view_config = WideViewConfiguration(self)
        self.side_view_config = SideViewConfiguration(self)
        self.surrounding_view_config = SurroundingViewConfiguration(self)

        self.label = [self.main_ui.original_image_front, self.main_ui.original_image_left,
                      self.main_ui.original_image_right, self.main_ui.original_image_Rear]

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_to_user_interface)
        self.timer.start()
        self.main_ui.stackedWidget.setCurrentIndex(0)
        self.main_controller.load_config("../data_config/config.yaml")
        self.bird_view_config.load_config_to_ui()
        self.wide_view_config.load_config_to_ui()
        self.side_view_config.load_config_to_ui()
        self.surrounding_view_config.load_config_to_ui()
        self.main_controller.control_perspective.fill_data_src()
        self.connect()

    def connect(self):
        self.shortcut = QShortcut(QKeySequence("Ctrl+R"), self)
        self.shortcut.activated.connect(self.restart_camera)

        self.main_ui.btn_home.clicked.connect(lambda: self.onclick_additional_option("front_original"))
        # self.main_ui.btn_original_view.clicked.connect(self.onclick_original)

        self.main_ui.btn_wide_view_front.clicked.connect(lambda: self.onclick_additional_option("front_wide"))
        self.main_ui.btn_wide_view_left.clicked.connect(lambda: self.onclick_additional_option("left_wide"))
        self.main_ui.btn_wide_view_rear.clicked.connect(lambda: self.onclick_additional_option("rear_wide"))
        self.main_ui.btn_wide_view_right.clicked.connect(lambda: self.onclick_additional_option("right_wide"))

        self.main_ui.btn_front_bird_view.clicked.connect(lambda: self.onclick_additional_option("front_bird_view"))
        self.main_ui.btn_left_right_bird_view.clicked.connect(lambda: self.onclick_additional_option("left_right_bird_view"))
        self.main_ui.btn_rear_bird_view.clicked.connect(lambda: self.onclick_additional_option("rear_bird_view"))

        self.main_ui.btn_full_original.clicked.connect(lambda: self.onclick_additional_option("surrounding_view"))
        self.main_ui.btn_front_original.clicked.connect(lambda: self.onclick_additional_option("front_surrounding_view"))
        self.main_ui.btn_left_right_original.clicked.connect(lambda: self.onclick_additional_option("left_right_surrounding_view"))
        self.main_ui.btn_rear_original.clicked.connect(lambda: self.onclick_additional_option("rear_surrounding_view"))

        self.main_ui.btn_side_left_right.clicked.connect(lambda: self.onclick_additional_option("side_left_right_view"))

        self.main_ui.btn_setting.clicked.connect(self.onclick_setting_option)
        self.main_ui.btn_calib_bird_view.clicked.connect(self.onclick_btn_calib_bird_view)

        self.main_ui.btn_calibration_wide_view.clicked.connect(self.onclick_btn_calib_wide_view)
        self.main_ui.btn_calib_surrounding_view.clicked.connect(self.onclick_btn_calib_surrounding_view)

        self.main_ui.btn_calibration_side_view.clicked.connect(self.onclick_btn_calib_side_view)

    def onclick_btn_calib_bird_view(self):
        self.main_ui.stackedWidget.setCurrentIndex(3)
        self.main_controller.change_mode("calibration_bird_view")
        self.control_clicking_point = SelectCoordinate(self)

    def update_to_user_interface(self):
        self.main_controller.next_frame()
        self.show_to_window.show_to_window()

    def restart_camera(self):
        self.main_controller.change_mode("original")
        self.main_ui.stackedWidget.setCurrentIndex(0)
        self.main_controller.run_video()

    def onclick_home_option(self):
        self.main_ui.stackedWidget.setCurrentIndex(0)
        self.main_controller.change_mode("original")

    def onclick_btn_calib_surrounding_view(self):
        self.main_ui.stackedWidget.setCurrentIndex(4)
        self.main_controller.change_mode("calibration_surrounding_view")

    def onclick_btn_calib_wide_view(self):
        self.main_ui.stackedWidget.setCurrentIndex(5)
        self.main_controller.change_mode("calibration_wide_view")

    def onclick_btn_calib_side_view(self):
        self.main_ui.stackedWidget.setCurrentIndex(6)
        self.main_controller.change_mode("calibration_side_view")

    def onclick_original(self):
        self.main_ui.stackedWidget.setCurrentIndex(0)
        self.main_controller.change_mode("original")

    def onclick_additional_option(self, value):
        self.main_ui.stackedWidget.setCurrentIndex(1)
        self.main_controller.change_mode(value)

    def onclick_close(self):
        self.main_ui.stackedWidget.setCurrentIndex(2)
        self.main_controller.change_mode("original")

    def onclick_setting_option(self):
        self.main_ui.stackedWidget.setCurrentIndex(2)
