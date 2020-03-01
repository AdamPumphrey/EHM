# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_rows.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_row_select_dialog(object):
    def setupUi(self, row_select_dialog):
        row_select_dialog.setObjectName("row_select_dialog")
        row_select_dialog.resize(358, 203)
        row_select_dialog.setMinimumSize(QtCore.QSize(242, 87))
        row_select_dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(row_select_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(row_select_dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.row_select_label = QtWidgets.QLabel(row_select_dialog)
        self.row_select_label.setObjectName("row_select_label")
        self.verticalLayout.addWidget(self.row_select_label)
        self.lineEdit = QtWidgets.QLineEdit(row_select_dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(row_select_dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(row_select_dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(row_select_dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(row_select_dialog)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(row_select_dialog)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.row_select_buttonbox = QtWidgets.QDialogButtonBox(row_select_dialog)
        self.row_select_buttonbox.setOrientation(QtCore.Qt.Horizontal)
        self.row_select_buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.row_select_buttonbox.setObjectName("row_select_buttonbox")
        self.verticalLayout.addWidget(self.row_select_buttonbox, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(row_select_dialog)
        self.row_select_buttonbox.accepted.connect(row_select_dialog.accept)
        self.row_select_buttonbox.rejected.connect(row_select_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(row_select_dialog)

    def retranslateUi(self, row_select_dialog):
        _translate = QtCore.QCoreApplication.translate
        row_select_dialog.setWindowTitle(_translate("row_select_dialog", "Select Rows"))
        self.label.setText(_translate("row_select_dialog", "Enter rows (eg. 1, 2, 3, etc) or choose range."))
        self.row_select_label.setText(_translate("row_select_dialog", "Enter rows:"))
        self.label_4.setText(_translate("row_select_dialog", "Max:"))
        self.label_2.setText(_translate("row_select_dialog", "Specify range:"))
        self.label_3.setText(_translate("row_select_dialog", "Min:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    row_select_dialog = QtWidgets.QDialog()
    ui = Ui_row_select_dialog()
    ui.setupUi(row_select_dialog)
    row_select_dialog.show()
    sys.exit(app.exec_())
