from UI.Ui_BoatDialog import Ui_BoatDialog
from PyQt5.QtWidgets import QDialog
from typing import Literal

class BoatDialog(Ui_BoatDialog, QDialog):
    def __init__(self, parent = None, mode: Literal['create', 'edit', 'delete'] = 'create'):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)

        self.btn_add_boat.setVisible(mode == 'create')
        self.btn_edit.setVisible(mode == 'edit')
        self.btn_delete_boat.setVisible(mode == 'delete')
        self.cmb_boat_id.setEnabled(mode != 'create')
        
        self.cmb_boat_type.currentTextChanged.connect(self.cmb_boat_type_changed)

    def cmb_boat_type_changed(self, current_text):
        self.chb_full_fuel.setVisible(current_text == 'موتوری')
        self.lbl_boat_full_fuel.setVisible(current_text == 'موتوری')

        self.chb_pedal_status.setVisible(current_text == 'پدالی')
        self.lbl_boat_pedal_status.setVisible(current_text == 'پدالی')

        self.spn_paddle_count.setVisible(current_text == 'پارویی')
        self.lbl_boat_paddle_count.setVisible(current_text == 'پارویی')