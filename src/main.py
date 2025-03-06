import sys
from PyQt5.QtWidgets import QApplication
from model import Model
from controller import MainController
from view import MainView


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_ctrl = MainController(self.model)
        self.main_view = MainView(self.model, self.main_ctrl)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.esxec_())
