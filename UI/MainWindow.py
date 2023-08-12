from UI.Ui_MainWindow import Ui_MainWindow
from UI.Ui_TouristDialog import Ui_TouristDialog
from UI.Ui_BoatDialog import Ui_BoatDialog
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        