from UI.Ui_StatDialog import Ui_StatDialog
from PyQt5.QtWidgets import QDialog

class StatDialog(Ui_StatDialog, QDialog):
    def __init__(self, parent = None, tourist_id: int = None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)