# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BoatDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BoatDialog(object):
    def setupUi(self, BoatDialog):
        BoatDialog.setObjectName("BoatDialog")
        BoatDialog.resize(345, 394)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        BoatDialog.setFont(font)
        BoatDialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        BoatDialog.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.vlay = QtWidgets.QVBoxLayout(BoatDialog)
        self.vlay.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.vlay.setObjectName("vlay")
        self.flay_info = QtWidgets.QFormLayout()
        self.flay_info.setObjectName("flay_info")
        self.lbl_boat_id = QtWidgets.QLabel(BoatDialog)
        self.lbl_boat_id.setObjectName("lbl_boat_id")
        self.flay_info.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_boat_id)
        self.lbl_boat_color = QtWidgets.QLabel(BoatDialog)
        self.lbl_boat_color.setObjectName("lbl_boat_color")
        self.flay_info.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_boat_color)
        self.lbl_boat_owner_id = QtWidgets.QLabel(BoatDialog)
        self.lbl_boat_owner_id.setObjectName("lbl_boat_owner_id")
        self.flay_info.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_boat_owner_id)
        self.lbl_boat_passenger_count = QtWidgets.QLabel(BoatDialog)
        self.lbl_boat_passenger_count.setObjectName("lbl_boat_passenger_count")
        self.flay_info.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_boat_passenger_count)
        self.lbl_boat_body_status = QtWidgets.QLabel(BoatDialog)
        self.lbl_boat_body_status.setObjectName("lbl_boat_body_status")
        self.flay_info.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_boat_body_status)
        self.lbl_boat_full_fuel = QtWidgets.QLabel(BoatDialog)
        self.lbl_boat_full_fuel.setObjectName("lbl_boat_full_fuel")
        self.flay_info.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lbl_boat_full_fuel)
        self.lbl_boat_pedal_status = QtWidgets.QLabel(BoatDialog)
        self.lbl_boat_pedal_status.setObjectName("lbl_boat_pedal_status")
        self.flay_info.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lbl_boat_pedal_status)
        self.lbl_boat_paddle_count = QtWidgets.QLabel(BoatDialog)
        self.lbl_boat_paddle_count.setObjectName("lbl_boat_paddle_count")
        self.flay_info.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.lbl_boat_paddle_count)
        self.cmb_boat_id = QtWidgets.QComboBox(BoatDialog)
        self.cmb_boat_id.setObjectName("cmb_boat_id")
        self.flay_info.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmb_boat_id)
        self.txt_color = QtWidgets.QLineEdit(BoatDialog)
        self.txt_color.setObjectName("txt_color")
        self.flay_info.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_color)
        self.txt_owner_id = QtWidgets.QLineEdit(BoatDialog)
        self.txt_owner_id.setObjectName("txt_owner_id")
        self.flay_info.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_owner_id)
        self.spn_passenger_count = QtWidgets.QSpinBox(BoatDialog)
        self.spn_passenger_count.setMinimum(1)
        self.spn_passenger_count.setMaximum(20)
        self.spn_passenger_count.setObjectName("spn_passenger_count")
        self.flay_info.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spn_passenger_count)
        self.chb_body_status = QtWidgets.QCheckBox(BoatDialog)
        self.chb_body_status.setObjectName("chb_body_status")
        self.flay_info.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.chb_body_status)
        self.chb_full_fuel = QtWidgets.QCheckBox(BoatDialog)
        self.chb_full_fuel.setObjectName("chb_full_fuel")
        self.flay_info.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.chb_full_fuel)
        self.chb_pedal_status = QtWidgets.QCheckBox(BoatDialog)
        self.chb_pedal_status.setObjectName("chb_pedal_status")
        self.flay_info.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.chb_pedal_status)
        self.spn_paddle_count = QtWidgets.QSpinBox(BoatDialog)
        self.spn_paddle_count.setMaximum(20)
        self.spn_paddle_count.setObjectName("spn_paddle_count")
        self.flay_info.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.spn_paddle_count)
        self.lbl_boat_type = QtWidgets.QLabel(BoatDialog)
        self.lbl_boat_type.setObjectName("lbl_boat_type")
        self.flay_info.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_boat_type)
        self.cmb_boat_type = QtWidgets.QComboBox(BoatDialog)
        self.cmb_boat_type.setObjectName("cmb_boat_type")
        self.cmb_boat_type.addItem("")
        self.cmb_boat_type.addItem("")
        self.cmb_boat_type.addItem("")
        self.flay_info.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cmb_boat_type)
        self.vlay.addLayout(self.flay_info)
        self.hlay_buttons = QtWidgets.QHBoxLayout()
        self.hlay_buttons.setObjectName("hlay_buttons")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlay_buttons.addItem(spacerItem)
        self.btn_add_boat = QtWidgets.QPushButton(BoatDialog)
        self.btn_add_boat.setObjectName("btn_add_boat")
        self.hlay_buttons.addWidget(self.btn_add_boat)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlay_buttons.addItem(spacerItem1)
        self.btn_delete_boat = QtWidgets.QPushButton(BoatDialog)
        self.btn_delete_boat.setObjectName("btn_delete_boat")
        self.hlay_buttons.addWidget(self.btn_delete_boat)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlay_buttons.addItem(spacerItem2)
        self.btn_return = QtWidgets.QPushButton(BoatDialog)
        self.btn_return.setObjectName("btn_return")
        self.hlay_buttons.addWidget(self.btn_return)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlay_buttons.addItem(spacerItem3)
        self.vlay.addLayout(self.hlay_buttons)

        self.retranslateUi(BoatDialog)
        QtCore.QMetaObject.connectSlotsByName(BoatDialog)

    def retranslateUi(self, BoatDialog):
        _translate = QtCore.QCoreApplication.translate
        BoatDialog.setWindowTitle(_translate("BoatDialog", "قایق"))
        self.lbl_boat_id.setText(_translate("BoatDialog", "کد قایق"))
        self.lbl_boat_color.setText(_translate("BoatDialog", "رنگ"))
        self.lbl_boat_owner_id.setText(_translate("BoatDialog", "کد مالک"))
        self.lbl_boat_passenger_count.setText(_translate("BoatDialog", "تعداد سرنشین"))
        self.lbl_boat_body_status.setText(_translate("BoatDialog", "وضعیت بدنه"))
        self.lbl_boat_full_fuel.setText(_translate("BoatDialog", "میزان سوخت"))
        self.lbl_boat_pedal_status.setText(_translate("BoatDialog", "وضعیت پدال"))
        self.lbl_boat_paddle_count.setText(_translate("BoatDialog", "تعداد پارو"))
        self.chb_body_status.setText(_translate("BoatDialog", "سالم"))
        self.chb_full_fuel.setText(_translate("BoatDialog", "پر"))
        self.chb_pedal_status.setText(_translate("BoatDialog", "سالم"))
        self.lbl_boat_type.setText(_translate("BoatDialog", "نوع قایق"))
        self.cmb_boat_type.setItemText(0, _translate("BoatDialog", "موتوری"))
        self.cmb_boat_type.setItemText(1, _translate("BoatDialog", "پدالی"))
        self.cmb_boat_type.setItemText(2, _translate("BoatDialog", "پارویی"))
        self.btn_add_boat.setText(_translate("BoatDialog", "ایجاد قایق"))
        self.btn_delete_boat.setText(_translate("BoatDialog", "حذف قایق"))
        self.btn_return.setText(_translate("BoatDialog", "بازگشت"))
