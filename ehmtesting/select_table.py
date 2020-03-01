# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_table.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_table_select_dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

    def setupUi(self, table_select_dialog):
        table_select_dialog.setObjectName("table_select_dialog")
        table_select_dialog.resize(316, 93)
        table_select_dialog.setMinimumSize(QtCore.QSize(316, 93))
        table_select_dialog.setMaximumSize(QtCore.QSize(316, 93))
        self.verticalLayout = QtWidgets.QVBoxLayout(table_select_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(table_select_dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(table_select_dialog)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(table_select_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(table_select_dialog)
        self.buttonBox.accepted.connect(table_select_dialog.accept)
        self.buttonBox.rejected.connect(table_select_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(table_select_dialog)

    def retranslateUi(self, table_select_dialog):
        _translate = QtCore.QCoreApplication.translate
        table_select_dialog.setWindowTitle(_translate("table_select_dialog", "Select Table"))
        self.label.setText(_translate("table_select_dialog", "Select table:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    table_select_dialog = QtWidgets.QDialog()
    ui = Ui_table_select_dialog()
    ui.setupUi(table_select_dialog)
    table_select_dialog.show()
    sys.exit(app.exec_())
