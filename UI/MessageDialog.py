from UI import *

class MessageDialog(Ui_MessageDialog, QDialog):
    def __init__(self, parent = None, message: str = "", question_mode: bool = False):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.lbl_message.setText(message)
        self.wgt_question_buttons.setVisible(question_mode)
        self.wgt_message_buttons.setVisible(not question_mode)
        self.btn_confirm.clicked.connect(self.accept)
        self.btn_yes.clicked.connect(self.accept)
        self.btn_no.clicked.connect(self.reject)