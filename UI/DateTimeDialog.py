from UI.Ui_DateTimeDialog import Ui_DateTimeDialog
from PyQt5.QtWidgets import QDialog
from datetime import datetime
from UI.MessageDialog import MessageDialog

class DateTimeDialog(Ui_DateTimeDialog, QDialog):
    def __init__(self, parent) -> None:
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.set_now()
        self.btn_now.clicked.connect(self.set_now)
        self.btn_return.clicked.connect(self.reject)
        self.btn_confirm.clicked.connect(self.btn_confirm_clicked)

    def set_now(self):
        now = datetime.now()
        self.spn_year.setValue(now.year)
        self.spn_month.setValue(now.month)
        self.spn_day.setValue(now.day)
        self.spn_hour.setValue(now.hour)
        self.spn_minute.setValue(now.minute)

    def btn_confirm_clicked(self):
        year = self.spn_year.value()
        month = self.spn_month.value()
        day = self.spn_day.value()
        hour = self.spn_hour.value()
        minute = self.spn_minute.value()
        try:
            self.datetime = datetime(year, month, day, hour, minute)
            self.accept()
        except:
            MessageDialog(self, "تاریخ انتخاب شده نادرست است.").exec()
            return

    def exec(self):
        res = super().exec()
        if res == QDialog.Accepted:
            return (res, self.datetime)
        return (res, None)