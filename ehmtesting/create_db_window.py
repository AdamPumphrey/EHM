# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_db.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dbname_input_dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.create_dbname = None

    def setupUi(self, dbname_input_dialog):
        dbname_input_dialog.setObjectName("dbname_input_dialog")
        dbname_input_dialog.resize(388, 91)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dbname_input_dialog.sizePolicy().hasHeightForWidth())
        dbname_input_dialog.setSizePolicy(sizePolicy)
        dbname_input_dialog.setMinimumSize(QtCore.QSize(388, 91))
        dbname_input_dialog.setMaximumSize(QtCore.QSize(388, 91))
        self.verticalLayout = QtWidgets.QVBoxLayout(dbname_input_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dbname_input_label = QtWidgets.QLabel(dbname_input_dialog)
        self.dbname_input_label.setObjectName("dbname_input_label")
        self.verticalLayout.addWidget(self.dbname_input_label, 0, QtCore.Qt.AlignBottom)
        self.dbname_input_text = QtWidgets.QLineEdit(dbname_input_dialog)
        self.dbname_input_text.setObjectName("dbname_input_text")
        self.verticalLayout.addWidget(self.dbname_input_text)
        self.dbname_input_buttonbox = QtWidgets.QDialogButtonBox(dbname_input_dialog)
        self.dbname_input_buttonbox.setOrientation(QtCore.Qt.Horizontal)
        self.dbname_input_buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dbname_input_buttonbox.setCenterButtons(True)
        self.dbname_input_buttonbox.setObjectName("dbname_input_buttonbox")
        self.verticalLayout.addWidget(self.dbname_input_buttonbox)

        self.retranslateUi(dbname_input_dialog)
        self.dbname_input_buttonbox.accepted.connect(lambda: (self.process(dbname_input_dialog)))
        self.dbname_input_buttonbox.rejected.connect(dbname_input_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dbname_input_dialog)
        self.dbname_input_text.returnPressed.connect(lambda: (self.process(dbname_input_dialog)))

    def process(self, dbname_input_dialog):
        userInput = self.dbname_input_text.text()
        if userInput:
            self.create_dbname = userInput
            #print(self.create_dbname)
            dbname_input_dialog.accept()
        else:
            dbname_input_dialog.reject()

    def retranslateUi(self, dbname_input_dialog):
        _translate = QtCore.QCoreApplication.translate
        dbname_input_dialog.setWindowTitle(_translate("dbname_input_dialog", "Enter Database Name"))
        self.dbname_input_label.setText(_translate("dbname_input_dialog", "Database name:"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     dbname_input_dialog = QtWidgets.QDialog()
#     ui = Ui_dbname_input_dialog()
#     ui.setupUi(dbname_input_dialog)
#     dbname_input_dialog.show()
#     sys.exit(app.exec_())
