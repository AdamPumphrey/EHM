# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose_import.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_import_type_dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.result = None

    def setupUi(self, import_type_dialog):
        import_type_dialog.setObjectName("import_type_dialog")
        import_type_dialog.resize(240, 119)
        import_type_dialog.setMinimumSize(QtCore.QSize(240, 119))
        import_type_dialog.setMaximumSize(QtCore.QSize(240, 119))
        import_type_dialog.setWindowIcon(QtGui.QIcon('ehmtracking.ico'))
        self.gridLayout = QtWidgets.QGridLayout(import_type_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.import_type_stats_radio = QtWidgets.QRadioButton(import_type_dialog)
        self.import_type_stats_radio.setMinimumSize(QtCore.QSize(209, 17))
        self.import_type_stats_radio.setMaximumSize(QtCore.QSize(209, 17))
        self.import_type_stats_radio.setObjectName("import_type_stats_radio")
        self.gridLayout.addWidget(self.import_type_stats_radio, 3, 0, 1, 1)
        self.import_type_label = QtWidgets.QLabel(import_type_dialog)
        self.import_type_label.setObjectName("import_type_label")
        self.gridLayout.addWidget(self.import_type_label, 0, 0, 1, 1)
        self.import_type_buttonbox = QtWidgets.QDialogButtonBox(import_type_dialog)
        self.import_type_buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.import_type_buttonbox.setCenterButtons(True)
        self.import_type_buttonbox.setObjectName("import_type_buttonbox")
        self.gridLayout.addWidget(self.import_type_buttonbox, 4, 0, 1, 1)
        self.import_type_player_radio = QtWidgets.QRadioButton(import_type_dialog)
        self.import_type_player_radio.setObjectName("import_type_player_radio")
        self.gridLayout.addWidget(self.import_type_player_radio, 2, 0, 1, 1)

        self.retranslateUi(import_type_dialog)
        self.import_type_buttonbox.accepted.connect(lambda: (self.process(import_type_dialog)))
        self.import_type_buttonbox.rejected.connect(import_type_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(import_type_dialog)

    def process(self, import_type_dialog):
        accept = False
        if self.import_type_player_radio.isChecked():
            self.result = 1
            accept = True
        elif self.import_type_stats_radio.isChecked():
            self.result = 2
            accept = True
        if accept:
            import_type_dialog.accept()
        else:
            import_type_dialog.reject()

    def retranslateUi(self, import_type_dialog):
        _translate = QtCore.QCoreApplication.translate
        import_type_dialog.setWindowTitle(_translate("import_type_dialog", "Choose Import Type"))
        self.import_type_stats_radio.setText(_translate("import_type_dialog", "Import Stats"))
        self.import_type_label.setText(_translate("import_type_dialog", "Type of data to import:"))
        self.import_type_player_radio.setText(_translate("import_type_dialog", "Import Players"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     import_type_dialog = QtWidgets.QDialog()
#     ui = Ui_import_type_dialog()
#     ui.setupUi(import_type_dialog)
#     import_type_dialog.show()
#     sys.exit(app.exec_())
