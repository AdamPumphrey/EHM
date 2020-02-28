# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose_team.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_choose_team_dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.team_id = None

    def setupUi(self, choose_team_dialog):
        choose_team_dialog.setObjectName("choose_team_dialog")
        choose_team_dialog.resize(388, 91)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(choose_team_dialog.sizePolicy().hasHeightForWidth())
        choose_team_dialog.setSizePolicy(sizePolicy)
        choose_team_dialog.setMinimumSize(QtCore.QSize(388, 91))
        choose_team_dialog.setMaximumSize(QtCore.QSize(388, 91))
        choose_team_dialog.setWindowIcon(QtGui.QIcon('ehmtracking.ico'))
        self.verticalLayout = QtWidgets.QVBoxLayout(choose_team_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.choose_team_label = QtWidgets.QLabel(choose_team_dialog)
        self.choose_team_label.setObjectName("choose_team_label")
        self.verticalLayout.addWidget(self.choose_team_label, 0, QtCore.Qt.AlignBottom)
        self.choose_team_combobox = QtWidgets.QComboBox(choose_team_dialog)
        self.choose_team_combobox.setMaxVisibleItems(10)
        self.choose_team_combobox.setObjectName("choose_team_combobox")
        self.verticalLayout.addWidget(self.choose_team_combobox)
        self.choose_team_buttonbox = QtWidgets.QDialogButtonBox(choose_team_dialog)
        self.choose_team_buttonbox.setOrientation(QtCore.Qt.Horizontal)
        self.choose_team_buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.choose_team_buttonbox.setCenterButtons(True)
        self.choose_team_buttonbox.setObjectName("choose_team_buttonbox")
        self.verticalLayout.addWidget(self.choose_team_buttonbox)

        self.retranslateUi(choose_team_dialog)
        # self.choose_team_buttonbox.accepted.connect(lambda: self.process(choose_team_dialog))
        self.choose_team_buttonbox.accepted.connect(choose_team_dialog.accept)
        self.choose_team_buttonbox.rejected.connect(choose_team_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(choose_team_dialog)

    # def process(self, choose_team_dialog):
    #     self.team_id = self.choose_team_combobox.currentText()
    #     choose_team_dialog.accept()

    def retranslateUi(self, choose_team_dialog):
        _translate = QtCore.QCoreApplication.translate
        choose_team_dialog.setWindowTitle(_translate("choose_team_dialog", "Choose Import Team"))
        self.choose_team_label.setText(_translate("choose_team_dialog", "Choose team:"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     choose_team_dialog = QtWidgets.QDialog()
#     ui = Ui_choose_team_dialog()
#     ui.setupUi(choose_team_dialog)
#     choose_team_dialog.show()
#     sys.exit(app.exec_())
