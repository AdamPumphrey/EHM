# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_filter_dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.nameval = None
        self.lw = False
        self.c = False
        self.rw = False
        self.ld = False
        self.rd = False
        self.g = False

    def setupUi(self, filter_dialog):
        filter_dialog.setObjectName("filter_dialog")
        filter_dialog.resize(418, 294)
        filter_dialog.setMinimumSize(QtCore.QSize(418, 294))
        filter_dialog.setMaximumSize(QtCore.QSize(418, 294))
        self.gridLayout = QtWidgets.QGridLayout(filter_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.filter_maxage_spinbox = QtWidgets.QSpinBox(filter_dialog)
        self.filter_maxage_spinbox.setMinimumSize(QtCore.QSize(75, 20))
        self.filter_maxage_spinbox.setMaximumSize(QtCore.QSize(75, 20))
        self.filter_maxage_spinbox.setObjectName("filter_maxage_spinbox")
        self.gridLayout.addWidget(self.filter_maxage_spinbox, 9, 1, 1, 1)
        self.filter_name_label = QtWidgets.QLabel(filter_dialog)
        self.filter_name_label.setMinimumSize(QtCore.QSize(75, 20))
        self.filter_name_label.setMaximumSize(QtCore.QSize(75, 20))
        self.filter_name_label.setObjectName("filter_name_label")
        self.gridLayout.addWidget(self.filter_name_label, 0, 0, 1, 1)
        self.filter_c_checkbox = QtWidgets.QCheckBox(filter_dialog)
        self.filter_c_checkbox.setMinimumSize(QtCore.QSize(30, 17))
        self.filter_c_checkbox.setMaximumSize(QtCore.QSize(30, 17))
        self.filter_c_checkbox.setObjectName("filter_c_checkbox")
        self.gridLayout.addWidget(self.filter_c_checkbox, 3, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.filter_teamrights_label = QtWidgets.QLabel(filter_dialog)
        self.filter_teamrights_label.setMinimumSize(QtCore.QSize(75, 20))
        self.filter_teamrights_label.setMaximumSize(QtCore.QSize(75, 20))
        self.filter_teamrights_label.setObjectName("filter_teamrights_label")
        self.gridLayout.addWidget(self.filter_teamrights_label, 10, 0, 1, 1)
        self.filter_maxage_label = QtWidgets.QLabel(filter_dialog)
        self.filter_maxage_label.setMinimumSize(QtCore.QSize(75, 20))
        self.filter_maxage_label.setMaximumSize(QtCore.QSize(75, 20))
        self.filter_maxage_label.setObjectName("filter_maxage_label")
        self.gridLayout.addWidget(self.filter_maxage_label, 9, 0, 1, 1)
        self.filter_lw_checkbox = QtWidgets.QCheckBox(filter_dialog)
        self.filter_lw_checkbox.setMinimumSize(QtCore.QSize(38, 17))
        self.filter_lw_checkbox.setMaximumSize(QtCore.QSize(38, 17))
        self.filter_lw_checkbox.setTristate(False)
        self.filter_lw_checkbox.setObjectName("filter_lw_checkbox")
        self.gridLayout.addWidget(self.filter_lw_checkbox, 3, 2, 1, 1)
        self.filter_rd_checkbox = QtWidgets.QCheckBox(filter_dialog)
        self.filter_rd_checkbox.setMinimumSize(QtCore.QSize(40, 17))
        self.filter_rd_checkbox.setMaximumSize(QtCore.QSize(40, 17))
        self.filter_rd_checkbox.setObjectName("filter_rd_checkbox")
        self.gridLayout.addWidget(self.filter_rd_checkbox, 4, 4, 1, 1)
        self.filter_nameimput_lineedit = QtWidgets.QLineEdit(filter_dialog)
        self.filter_nameimput_lineedit.setMinimumSize(QtCore.QSize(142, 20))
        self.filter_nameimput_lineedit.setMaximumSize(QtCore.QSize(142, 20))
        self.filter_nameimput_lineedit.setObjectName("filter_nameimput_linedit")
        self.gridLayout.addWidget(self.filter_nameimput_lineedit, 0, 1, 1, 1)
        self.filter_league_label = QtWidgets.QLabel(filter_dialog)
        self.filter_league_label.setMinimumSize(QtCore.QSize(75, 20))
        self.filter_league_label.setMaximumSize(QtCore.QSize(75, 20))
        self.filter_league_label.setObjectName("filter_league_label")
        self.gridLayout.addWidget(self.filter_league_label, 12, 0, 1, 1)
        self.filter_year_label = QtWidgets.QLabel(filter_dialog)
        self.filter_year_label.setMinimumSize(QtCore.QSize(75, 13))
        self.filter_year_label.setMaximumSize(QtCore.QSize(75, 13))
        self.filter_year_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.filter_year_label.setObjectName("filter_year_label")
        self.gridLayout.addWidget(self.filter_year_label, 2, 0, 1, 1)
        self.filter_maxyear_label = QtWidgets.QLabel(filter_dialog)
        self.filter_maxyear_label.setMinimumSize(QtCore.QSize(75, 20))
        self.filter_maxyear_label.setMaximumSize(QtCore.QSize(75, 20))
        self.filter_maxyear_label.setObjectName("filter_maxyear_label")
        self.gridLayout.addWidget(self.filter_maxyear_label, 4, 0, 1, 1)
        self.filter_league_combobox = QtWidgets.QComboBox(filter_dialog)
        self.filter_league_combobox.setMinimumSize(QtCore.QSize(142, 20))
        self.filter_league_combobox.setMaximumSize(QtCore.QSize(142, 20))
        self.filter_league_combobox.setObjectName("filter_league_combobox")
        self.gridLayout.addWidget(self.filter_league_combobox, 12, 1, 1, 1)
        self.filter_rw_checkbox = QtWidgets.QCheckBox(filter_dialog)
        self.filter_rw_checkbox.setMinimumSize(QtCore.QSize(40, 17))
        self.filter_rw_checkbox.setMaximumSize(QtCore.QSize(40, 17))
        self.filter_rw_checkbox.setObjectName("filter_rw_checkbox")
        self.gridLayout.addWidget(self.filter_rw_checkbox, 3, 4, 1, 1)
        self.filter_minage_spinbox = QtWidgets.QSpinBox(filter_dialog)
        self.filter_minage_spinbox.setMinimumSize(QtCore.QSize(75, 20))
        self.filter_minage_spinbox.setMaximumSize(QtCore.QSize(75, 20))
        self.filter_minage_spinbox.setObjectName("filter_minage_spinbox")
        self.gridLayout.addWidget(self.filter_minage_spinbox, 8, 1, 1, 1)
        self.filter_position_label = QtWidgets.QLabel(filter_dialog)
        self.filter_position_label.setMinimumSize(QtCore.QSize(54, 20))
        self.filter_position_label.setMaximumSize(QtCore.QSize(54, 20))
        self.filter_position_label.setObjectName("filter_position_label")
        self.gridLayout.addWidget(self.filter_position_label, 1, 2, 1, 4, QtCore.Qt.AlignHCenter)
        self.filter_nation_label = QtWidgets.QLabel(filter_dialog)
        self.filter_nation_label.setMinimumSize(QtCore.QSize(75, 20))
        self.filter_nation_label.setMaximumSize(QtCore.QSize(75, 20))
        self.filter_nation_label.setObjectName("filter_nation_label")
        self.gridLayout.addWidget(self.filter_nation_label, 1, 0, 1, 1)
        self.filter_team_combobox = QtWidgets.QComboBox(filter_dialog)
        self.filter_team_combobox.setMinimumSize(QtCore.QSize(142, 20))
        self.filter_team_combobox.setMaximumSize(QtCore.QSize(142, 20))
        self.filter_team_combobox.setObjectName("filter_team_combobox")
        self.gridLayout.addWidget(self.filter_team_combobox, 11, 1, 1, 1)
        self.filter_minyear_label = QtWidgets.QLabel(filter_dialog)
        self.filter_minyear_label.setMinimumSize(QtCore.QSize(75, 20))
        self.filter_minyear_label.setMaximumSize(QtCore.QSize(75, 20))
        self.filter_minyear_label.setObjectName("filter_minyear_label")
        self.gridLayout.addWidget(self.filter_minyear_label, 3, 0, 1, 1)
        self.filter_buttonbox = QtWidgets.QDialogButtonBox(filter_dialog)
        self.filter_buttonbox.setMinimumSize(QtCore.QSize(75, 52))
        self.filter_buttonbox.setMaximumSize(QtCore.QSize(75, 52))
        self.filter_buttonbox.setOrientation(QtCore.Qt.Vertical)
        self.filter_buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.filter_buttonbox.setObjectName("filter_buttonbox")
        self.gridLayout.addWidget(self.filter_buttonbox, 11, 3, 2, 1)
        self.filter_g_checkbox = QtWidgets.QCheckBox(filter_dialog)
        self.filter_g_checkbox.setMinimumSize(QtCore.QSize(30, 17))
        self.filter_g_checkbox.setMaximumSize(QtCore.QSize(30, 17))
        self.filter_g_checkbox.setObjectName("filter_g_checkbox")
        self.gridLayout.addWidget(self.filter_g_checkbox, 5, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.filter_maxyear_spinbox = QtWidgets.QSpinBox(filter_dialog)
        self.filter_maxyear_spinbox.setMinimumSize(QtCore.QSize(75, 20))
        self.filter_maxyear_spinbox.setMaximumSize(QtCore.QSize(75, 20))
        self.filter_maxyear_spinbox.setMaximum(3000)
        self.filter_maxyear_spinbox.setObjectName("filter_maxyear_spinbox")
        self.gridLayout.addWidget(self.filter_maxyear_spinbox, 4, 1, 1, 1)
        self.filter_teamplaying_label = QtWidgets.QLabel(filter_dialog)
        self.filter_teamplaying_label.setMinimumSize(QtCore.QSize(75, 20))
        self.filter_teamplaying_label.setMaximumSize(QtCore.QSize(75, 20))
        self.filter_teamplaying_label.setObjectName("filter_teamplaying_label")
        self.gridLayout.addWidget(self.filter_teamplaying_label, 11, 0, 1, 1)
        self.filter_minage_label = QtWidgets.QLabel(filter_dialog)
        self.filter_minage_label.setMinimumSize(QtCore.QSize(75, 20))
        self.filter_minage_label.setMaximumSize(QtCore.QSize(75, 20))
        self.filter_minage_label.setObjectName("filter_minage_label")
        self.gridLayout.addWidget(self.filter_minage_label, 8, 0, 1, 1)
        self.filter_teamrights_combobox = QtWidgets.QComboBox(filter_dialog)
        self.filter_teamrights_combobox.setMinimumSize(QtCore.QSize(142, 20))
        self.filter_teamrights_combobox.setMaximumSize(QtCore.QSize(142, 20))
        self.filter_teamrights_combobox.setObjectName("filter_teamrights_combobox")
        self.gridLayout.addWidget(self.filter_teamrights_combobox, 10, 1, 1, 1)
        self.filter_nation_combobox = QtWidgets.QComboBox(filter_dialog)
        self.filter_nation_combobox.setMinimumSize(QtCore.QSize(142, 20))
        self.filter_nation_combobox.setMaximumSize(QtCore.QSize(142, 20))
        self.filter_nation_combobox.setObjectName("filter_nation_combobox")
        self.gridLayout.addWidget(self.filter_nation_combobox, 1, 1, 1, 1)
        self.filter_ld_checkbox = QtWidgets.QCheckBox(filter_dialog)
        self.filter_ld_checkbox.setMinimumSize(QtCore.QSize(38, 17))
        self.filter_ld_checkbox.setMaximumSize(QtCore.QSize(38, 17))
        self.filter_ld_checkbox.setObjectName("filter_ld_checkbox")
        self.gridLayout.addWidget(self.filter_ld_checkbox, 4, 2, 1, 1)
        self.filter_minyear_spinbox = QtWidgets.QSpinBox(filter_dialog)
        self.filter_minyear_spinbox.setMinimumSize(QtCore.QSize(75, 20))
        self.filter_minyear_spinbox.setMaximumSize(QtCore.QSize(75, 20))
        self.filter_minyear_spinbox.setMinimum(0)
        self.filter_minyear_spinbox.setMaximum(3000)
        self.filter_minyear_spinbox.setObjectName("filter_minyear_spinbox")
        self.gridLayout.addWidget(self.filter_minyear_spinbox, 3, 1, 1, 1)
        self.filter_age_label = QtWidgets.QLabel(filter_dialog)
        self.filter_age_label.setMinimumSize(QtCore.QSize(75, 17))
        self.filter_age_label.setMaximumSize(QtCore.QSize(75, 17))
        self.filter_age_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.filter_age_label.setObjectName("filter_age_label")
        self.gridLayout.addWidget(self.filter_age_label, 5, 0, 1, 1)

        self.retranslateUi(filter_dialog)
        self.filter_buttonbox.accepted.connect(lambda: self.process(filter_dialog))
        self.filter_buttonbox.rejected.connect(filter_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(filter_dialog)

    def process(self, filter_dialog):
        userInput = self.filter_nameimput_lineedit.text()
        if userInput:
            self.nameval = userInput
        if self.filter_lw_checkbox.isChecked():
            self.lw = True
        if self.filter_c_checkbox.isChecked():
            self.c = True
        if self.filter_rw_checkbox.isChecked():
            self.rw = True
        if self.filter_ld_checkbox.isChecked():
            self.ld = True
        if self.filter_rd_checkbox.isChecked():
            self.rd = True
        if self.filter_g_checkbox.isChecked():
            self.g = True
        filter_dialog.accept()

    def retranslateUi(self, filter_dialog):
        _translate = QtCore.QCoreApplication.translate
        filter_dialog.setWindowTitle(_translate("filter_dialog", "Choose Filter Options"))
        self.filter_name_label.setText(_translate("filter_dialog", "Name:"))
        self.filter_c_checkbox.setText(_translate("filter_dialog", "C"))
        self.filter_teamrights_label.setText(_translate("filter_dialog", "Team Rights:"))
        self.filter_maxage_label.setText(_translate("filter_dialog", "Max:"))
        self.filter_lw_checkbox.setText(_translate("filter_dialog", "LW"))
        self.filter_rd_checkbox.setText(_translate("filter_dialog", "RD"))
        self.filter_league_label.setText(_translate("filter_dialog", "League:"))
        self.filter_year_label.setText(_translate("filter_dialog", "Year:"))
        self.filter_maxyear_label.setText(_translate("filter_dialog", "Max:"))
        self.filter_rw_checkbox.setText(_translate("filter_dialog", "RW"))
        self.filter_position_label.setText(_translate("filter_dialog", "Position(s):"))
        self.filter_nation_label.setText(_translate("filter_dialog", "Nation:"))
        self.filter_minyear_label.setText(_translate("filter_dialog", "Min:"))
        self.filter_g_checkbox.setText(_translate("filter_dialog", "G"))
        self.filter_teamplaying_label.setText(_translate("filter_dialog", "Team Playing:"))
        self.filter_minage_label.setText(_translate("filter_dialog", "Min:"))
        self.filter_ld_checkbox.setText(_translate("filter_dialog", "LD"))
        self.filter_age_label.setText(_translate("filter_dialog", "Age:"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     filter_dialog = QtWidgets.QDialog()
#     ui = Ui_filter_dialog()
#     ui.setupUi(filter_dialog)
#     filter_dialog.show()
#     sys.exit(app.exec_())
