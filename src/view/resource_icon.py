import os
from PyQt5.QtCore import QDir

CURRENT_DIRECTORY = os.path.abspath(os.getcwd())
QDir.addSearchPath("icons", CURRENT_DIRECTORY + "/view/icons")
