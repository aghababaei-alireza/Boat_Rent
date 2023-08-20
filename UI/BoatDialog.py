from UI.Ui_BoatDialog import Ui_BoatDialog
from PyQt5.QtWidgets import QDialog
from typing import Literal
from MotorBoat import MotorBoat
from PedalBoat import PedalBoat
from RowBoat import RowBoat
from Boat import Boat
from UI.MessageDialog import MessageDialog

class BoatDialog(Ui_BoatDialog, QDialog):
    def __init__(self, parent = None, mode: Literal['create', 'edit', 'delete'] = 'create', owner_id: int = None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.lbl_error.setVisible(False)
        self.btn_add_boat.setVisible(mode == 'create')
        self.btn_edit.setVisible(mode == 'edit')
        self.btn_delete_boat.setVisible(mode == 'delete')
        self.cmb_boat_id.setEnabled(mode != 'create')

        if owner_id is not None:
            self.txt_owner_id.setText(str(owner_id))

        self.btn_add_boat.clicked.connect(self.btn_add_boat_clicked)
        self.btn_edit.clicked.connect(self.btn_edit_boat_clicked)
        self.btn_delete_boat.clicked.connect(self.btn_delete_boat_clicked)
        self.btn_return.clicked.connect(self.reject)

        self.txt_color.textChanged.connect(lambda: self.lbl_error.setVisible(False))
        self.txt_owner_id.textChanged.connect(lambda: self.lbl_error.setVisible(False))
        self.spn_passenger_count.valueChanged.connect(lambda: self.lbl_error.setVisible(False))
        self.spn_paddle_count.valueChanged.connect(lambda: self.lbl_error.setVisible(False))
        self.chb_body_status.toggled.connect(lambda: self.lbl_error.setVisible(False))
        self.chb_full_fuel.toggled.connect(lambda: self.lbl_error.setVisible(False))
        self.chb_pedal_status.toggled.connect(lambda: self.lbl_error.setVisible(False))

        if mode != 'create':
            try:
                self.boats = Boat.get_all_boats()
                self.cmb_boat_id.clear()
                for boat in self.boats:
                    self.cmb_boat_id.addItem(str(boat.boat_id))
                self.cmb_boat_id_changed(self.cmb_boat_id.currentText())
            except Exception as e:
                print(e)
                MessageDialog(self, "ارتباط با پایگاه داده برقرار نشد.").exec()

        self.cmb_boat_id.currentTextChanged.connect(self.cmb_boat_id_changed)
        self.cmb_boat_id_changed(self.cmb_boat_id.currentText())
        
        self.cmb_boat_type.currentTextChanged.connect(self.cmb_boat_type_changed)
        self.cmb_boat_type_changed(self.cmb_boat_type.currentText())

        if mode == 'delete':
            self.cmb_boat_type.setEnabled(False)
            self.txt_color.setEnabled(False)
            self.txt_owner_id.setEnabled(False)
            self.spn_passenger_count.setEnabled(False)
            self.chb_body_status.setEnabled(False)
            self.chb_full_fuel.setEnabled(False)
            self.chb_pedal_status.setEnabled(False)
            self.spn_paddle_count.setEnabled(False)

    def show_error(self, message: str):
        self.lbl_error.setText(message)
        self.lbl_error.setVisible(True)
    
    def check_data(self) -> bool:
        if self.cmb_boat_id.isEnabled() and not self.cmb_boat_id.currentText():
            self.show_error("کد قایق نمی‌تواند خالی باشد")
            return False
        if not self.txt_color.text():
            self.show_error("رنگ قایق نمی‌تواند خالی باشد")
            return False
        if not self.txt_owner_id.text():
            self.show_error("کد مالک قایق نمی‌تواند خالی باشد")
            return False
        return True
    
    def cmb_boat_id_changed(self, current_id):
        self.lbl_error.setVisible(False)
        if not current_id:
            return
        current_id = int(current_id)
        try:
            boat = Boat.get_boat_by_id(current_id)
            self.txt_color.setText(boat.color)
            self.txt_owner_id.setText(str(boat.owner_id))
            self.spn_passenger_count.setValue(boat.passenger_count)
            self.chb_body_status.setChecked(boat.body_status)

            if isinstance(boat, MotorBoat):
                self.cmb_boat_type.setCurrentText('موتوری')
                self.chb_full_fuel.setChecked(boat.full_fuel)
            elif isinstance(boat, PedalBoat):
                self.cmb_boat_type.setCurrentText('پدالی')
                self.chb_pedal_status.setChecked(boat.pedal_status)
            elif isinstance(boat, RowBoat):
                self.cmb_boat_type.setCurrentText('پارویی')
                self.spn_paddle_count.setValue(boat.paddle_count)
            self.cmb_boat_type_changed(self.cmb_boat_type.currentText())
        except Exception as e:
            print(e)
            MessageDialog(self, "ارتباط با پایگاه داده برقرار نشد.").exec()

    def cmb_boat_type_changed(self, current_text):
        self.lbl_error.setVisible(False)
        self.chb_full_fuel.setVisible(current_text == 'موتوری')
        self.lbl_boat_full_fuel.setVisible(current_text == 'موتوری')

        self.chb_pedal_status.setVisible(current_text == 'پدالی')
        self.lbl_boat_pedal_status.setVisible(current_text == 'پدالی')

        self.spn_paddle_count.setVisible(current_text == 'پارویی')
        self.lbl_boat_paddle_count.setVisible(current_text == 'پارویی')

    def btn_add_boat_clicked(self):
        if not self.check_data():
            return
        color = self.txt_color.text()
        owner_id = int(self.txt_owner_id.text())
        passenger_count = self.spn_passenger_count.value()
        body_status = self.chb_body_status.isChecked()
        try:
            match self.cmb_boat_type.currentText():
                case 'موتوری':
                    full_fuel = self.chb_full_fuel.isChecked()
                    boat_id = MotorBoat.create_new_motor_boat(color, owner_id, passenger_count, body_status, full_fuel)
                case 'پدالی':
                    pedal_status = self.chb_pedal_status.isChecked()
                    boat_id = PedalBoat.create_new_pedal_boat(color, owner_id, passenger_count, body_status, pedal_status)
                case 'پارویی':
                    paddle_count = self.spn_paddle_count.value()
                    boat_id = RowBoat.create_new_row_boat(color, owner_id, passenger_count, body_status, paddle_count)
            MessageDialog(self, f"قایق با کد {boat_id} ایجاد شد.").exec()
            self.accept()
        except Exception as e:
            print(e)
            MessageDialog(self, "ارتباط با پایگاه داده برقرار نشد.").exec()

    def btn_edit_boat_clicked(self):
        if not self.check_data():
            return
        if MessageDialog(self, "آیا از ویرایش اطلاعات این قایق اطمینان دارید؟", True).exec() == MessageDialog.Rejected:
            return
        boat_id = int(self.cmb_boat_id.currentText())
        boat_type_name = self.cmb_boat_type.currentText()
        color = self.txt_color.text()
        owner_id = int(self.txt_owner_id.text())
        passenger_count = self.spn_passenger_count.value()
        body_status = self.chb_body_status.isChecked()
        try:
            match boat_type_name:
                case 'موتوری':
                    full_fuel = self.chb_full_fuel.isChecked()
                    MotorBoat.edit_motor_boat(boat_id, color, owner_id, passenger_count, body_status, full_fuel)
                case 'پدالی':
                    pedal_status = self.chb_pedal_status.isChecked()
                    PedalBoat.edit_pedal_boat(boat_id, color, owner_id, passenger_count, body_status, pedal_status)
                case 'پارویی':
                    paddle_count = self.spn_paddle_count.value()
                    RowBoat.edit_row_boat(boat_id, color, owner_id, passenger_count, body_status, paddle_count)
            MessageDialog(self, "اطلاعات قایق با موفقیت ویرایش شد.").exec()
        except Exception as e:
            print(e)
            MessageDialog(self, "ارتباط با پایگاه داده برقرار نشد.").exec()
    
    def btn_delete_boat_clicked(self):
        if not self.check_data():
            return
        boat_id = int(self.cmb_boat_id.currentText())
        if MessageDialog(self, "آیا از حذف این قایق اطمینان دارید؟", True).exec() == MessageDialog.Rejected:
            return
        try:
            Boat.delete_boat_by_id(boat_id)
            self.boats = Boat.get_all_boats()
            self.cmb_boat_id.clear()
            for boat in self.boats:
                self.cmb_boat_id.addItem(str(boat.boat_id))
            self.cmb_boat_id_changed(int(self.cmb_boat_id.currentText()))
        except Exception as e:
            print(e)
            MessageDialog(self, "ارتباط با پایگاه داده برقرار نشد.").exec()