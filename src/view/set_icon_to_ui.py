from PyQt5 import QtGui, QtCore


class SetIconToUi:
    def __init__(self, main_ui):
        super(SetIconToUi, self).__init__()
        self.ui = main_ui
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:home.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_home.setIcon(icon)

        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("icons:page-2.png"), QtGui.QIcon.Mode.Normal,
        #                QtGui.QIcon.State.Off)
        # self.ui.btn_original_view.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-17.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_side_left_right.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-12.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_wide_view_front.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-13.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_wide_view_rear.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-16.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_wide_view_left.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-15.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_wide_view_right.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-9.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_front_bird_view.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-10.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_rear_bird_view.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-7.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_left_right_bird_view.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-1.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_full_original.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-3.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_rear_original.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-18.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_front_original.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-4.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_left_right_original.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:settings-solid.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_setting.setIcon(icon)

        # This icon for calibration system setting
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-7.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_calib_bird_view.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.ui.btn_calib_bird_view.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-1.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_calib_surrounding_view.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.ui.btn_calib_surrounding_view.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-11.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_calibration_wide_view.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.ui.btn_calibration_wide_view.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:page-17.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.ui.btn_calibration_side_view.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.ui.btn_calibration_side_view.setIcon(icon)


