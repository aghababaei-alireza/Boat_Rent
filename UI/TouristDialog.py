from UI.Ui_TouristDialog import Ui_TouristDialog
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from Tourist import Tourist
from UI.MessageDialog import MessageDialog
from MotorBoat import MotorBoat
from PedalBoat import PedalBoat
from RowBoat import RowBoat
from UI.BoatDialog import BoatDialog

class TouristDialog(Ui_TouristDialog, QDialog):
    def __init__(self, parent = None, edit_mode: bool = False, tourist_id: int = None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.btn_edit.setVisible(edit_mode)
        self.btn_add_tourist.setVisible(not edit_mode)
        self.cmb_tourist_id.setEnabled(edit_mode)
        self.grp_boats.setEnabled(edit_mode)

        if edit_mode:
            self.tourists_id = Tourist.get_all_tourists_id()
            self.cmb_tourist_id.clear()
            i = 0
            for id in self.tourists_id:
                self.cmb_tourist_id.insertItem(i, str(id))
                i += 1
            self.cmb_tourist_id_changed(int(self.cmb_tourist_id.currentText()))

        self.btn_add_tourist.clicked.connect(self.btn_add_tourist_clicked)
        self.btn_edit.clicked.connect(self.btn_edit_tourist_clicked)
        self.btn_return.clicked.connect(self.reject)
        self.cmb_tourist_id.currentTextChanged.connect(lambda current_text: self.cmb_tourist_id_changed(int(current_text)))
        self.btn_new_boat.clicked.connect(self.btn_new_boat_clicked)

        if tourist_id:
            self.cmb_tourist_id.setCurrentText(str(tourist_id))

    def btn_add_tourist_clicked(self):
        name = self.txt_tourist_name.text()
        family = self.txt_tourist_family.text()
        mobile = self.txt_tourist_mobile.text()
        id = Tourist.create_new_tourist(name, family, mobile)
        self.cmb_tourist_id.clear()
        self.cmb_tourist_id.setCurrentText(str(id))
        MessageDialog(self, "گردشگر جدید با موفقیت ثبت شد.").exec()
        self.btn_add_tourist.setEnabled(False)
        self.grp_boats.setEnabled(True)

    def btn_edit_tourist_clicked(self):
        if MessageDialog(self, "آیا از ویرایش اطلاعات این گردشگر اطمینان دارید؟", True).exec() == MessageDialog.Rejected:
            return
        tourist_id = int(self.cmb_tourist_id.currentText())
        name = self.txt_tourist_name.text()
        family = self.txt_tourist_family.text()
        mobile = self.txt_tourist_mobile.text()
        Tourist.edit_tourist_info(tourist_id, name, family, mobile)
        MessageDialog(self, "اطلاعات گردشگر با موفقیت ویرایش شد.").exec()

    def cmb_tourist_id_changed(self, tourist_id):
        tourist = Tourist.get_tourist_by_id(tourist_id)
        self.txt_tourist_name.setText(tourist.name)
        self.txt_tourist_family.setText(tourist.family)
        self.txt_tourist_mobile.setText(tourist.mobile)
        self.tbl_tourist_boats.setRowCount(0)

        i = 0
        for boat in tourist.boat_list:
            self.tbl_tourist_boats.insertRow(i)
            self.tbl_tourist_boats.setItem(i, 0, QTableWidgetItem(str(boat.boat_id)))
            if isinstance(boat, MotorBoat):
                self.tbl_tourist_boats.setItem(i, 1, QTableWidgetItem('موتوری'))
            elif isinstance(boat, PedalBoat):
                self.tbl_tourist_boats.setItem(i, 1, QTableWidgetItem('پدالی'))
            elif isinstance(boat, RowBoat):
                self.tbl_tourist_boats.setItem(i, 1, QTableWidgetItem('پارویی'))
            i += 1

    def btn_new_boat_clicked(self):
        BoatDialog(self, 'create', int(self.cmb_tourist_id.currentText())).exec()
        self.cmb_tourist_id_changed(int(self.cmb_tourist_id.currentText()))