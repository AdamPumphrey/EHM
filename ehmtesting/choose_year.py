# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose_year.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_choose_year_dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

    def setupUi(self, choose_year_dialog):
        choose_year_dialog.setObjectName("choose_year_dialog")
        choose_year_dialog.resize(263, 102)
        choose_year_dialog.setMinimumSize(QtCore.QSize(263, 102))
        choose_year_dialog.setMaximumSize(QtCore.QSize(263, 102))
        choose_year_dialog.setWindowIcon(QtGui.QIcon('ehmtracking.ico'))
        self.verticalLayout = QtWidgets.QVBoxLayout(choose_year_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.choose_year_label = QtWidgets.QLabel(choose_year_dialog)
        self.choose_year_label.setObjectName("choose_year_label")
        self.verticalLayout.addWidget(self.choose_year_label)
        self.choose_year_spinbox = QtWidgets.QSpinBox(choose_year_dialog)
        self.choose_year_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.choose_year_spinbox.setMinimum(1900)
        self.choose_year_spinbox.setMaximum(3000)
        self.choose_year_spinbox.setProperty("value", 2020)
        self.choose_year_spinbox.setObjectName("choose_year_spinbox")
        self.verticalLayout.addWidget(self.choose_year_spinbox)
        self.choose_year_buttonbox = QtWidgets.QDialogButtonBox(choose_year_dialog)
        self.choose_year_buttonbox.setOrientation(QtCore.Qt.Horizontal)
        self.choose_year_buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.choose_year_buttonbox.setCenterButtons(True)
        self.choose_year_buttonbox.setObjectName("choose_year_buttonbox")
        self.verticalLayout.addWidget(self.choose_year_buttonbox)

        self.retranslateUi(choose_year_dialog)
        self.choose_year_buttonbox.accepted.connect(choose_year_dialog.accept)
        self.choose_year_buttonbox.rejected.connect(choose_year_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(choose_year_dialog)

    def retranslateUi(self, choose_year_dialog):
        _translate = QtCore.QCoreApplication.translate
        choose_year_dialog.setWindowTitle(_translate("choose_year_dialog", "Choose Import Year"))
        self.choose_year_label.setText(_translate("choose_year_dialog", "Choose year:"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     choose_year_dialog = QtWidgets.QDialog()
#     ui = Ui_choose_year_dialog()
#     ui.setupUi(choose_year_dialog)
#     choose_year_dialog.show()
#     sys.exit(app.exec_())
