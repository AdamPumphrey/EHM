# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'initial_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import ehmtracker as ehm
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from create_db_window import Ui_dbname_input_dialog as Form


class Ui_MainWindow(object):
    def __init__(self):
        self.conn_status = None
        self.conn = None
        self.db_name = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(849, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.skaterstats_button = QtWidgets.QPushButton(self.centralwidget)
        self.skaterstats_button.setMinimumSize(QtCore.QSize(150, 75))
        self.skaterstats_button.setMaximumSize(QtCore.QSize(150, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.skaterstats_button.setFont(font)
        self.skaterstats_button.setObjectName("skaterstats_button")
        self.gridLayout.addWidget(self.skaterstats_button, 0, 3, 1, 1)
        self.players_button = QtWidgets.QPushButton(self.centralwidget)
        self.players_button.setMinimumSize(QtCore.QSize(150, 75))
        self.players_button.setMaximumSize(QtCore.QSize(150, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.players_button.setFont(font)
        self.players_button.setObjectName("players_button")
        self.gridLayout.addWidget(self.players_button, 0, 1, 1, 1)
        self.import_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_button.setMinimumSize(QtCore.QSize(150, 75))
        self.import_button.setMaximumSize(QtCore.QSize(150, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.import_button.setFont(font)
        self.import_button.setObjectName("import_button")
        self.gridLayout.addWidget(self.import_button, 0, 0, 1, 1)
        self.attributes_button = QtWidgets.QPushButton(self.centralwidget)
        self.attributes_button.setMinimumSize(QtCore.QSize(150, 75))
        self.attributes_button.setMaximumSize(QtCore.QSize(150, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.attributes_button.setFont(font)
        self.attributes_button.setObjectName("attributes_button")
        self.gridLayout.addWidget(self.attributes_button, 0, 2, 1, 1)
        self.goaliestats_button = QtWidgets.QPushButton(self.centralwidget)
        self.goaliestats_button.setMinimumSize(QtCore.QSize(150, 75))
        self.goaliestats_button.setMaximumSize(QtCore.QSize(150, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.goaliestats_button.setFont(font)
        self.goaliestats_button.setObjectName("goaliestats_button")
        self.gridLayout.addWidget(self.goaliestats_button, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.database_display = QtWidgets.QTableWidget(self.centralwidget)
        self.database_display.setObjectName("database_display")
        self.database_display.setColumnCount(0)
        self.database_display.setRowCount(0)
        self.verticalLayout.addWidget(self.database_display)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuGraph = QtWidgets.QMenu(self.menubar)
        self.menuGraph.setObjectName("menuGraph")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate_db = QtWidgets.QAction(MainWindow)
        self.actionCreate_db.setObjectName("actionCreate_db")
        self.actionLoad_db = QtWidgets.QAction(MainWindow)
        self.actionLoad_db.setObjectName("actionLoad_db")
        self.actionExit_db = QtWidgets.QAction(MainWindow)
        self.actionExit_db.setObjectName("actionExit_db")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPlayers = QtWidgets.QAction(MainWindow)
        self.actionPlayers.setObjectName("actionPlayers")
        self.actionAttributes = QtWidgets.QAction(MainWindow)
        self.actionAttributes.setObjectName("actionAttributes")
        self.actionSkater_Stats = QtWidgets.QAction(MainWindow)
        self.actionSkater_Stats.setObjectName("actionSkater_Stats")
        self.actionGoalie_Stats = QtWidgets.QAction(MainWindow)
        self.actionGoalie_Stats.setObjectName("actionGoalie_Stats")
        self.actionGraph_Data = QtWidgets.QAction(MainWindow)
        self.actionGraph_Data.setObjectName("actionGraph_Data")
        self.actionEdit_Graph = QtWidgets.QAction(MainWindow)
        self.actionEdit_Graph.setObjectName("actionEdit_Graph")
        self.actionSave_Graph = QtWidgets.QAction(MainWindow)
        self.actionSave_Graph.setObjectName("actionSave_Graph")
        self.menuFile.addAction(self.actionCreate_db)
        self.menuFile.addAction(self.actionLoad_db)
        self.menuFile.addAction(self.actionExit_db)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionPlayers)
        self.menuView.addAction(self.actionAttributes)
        self.menuView.addAction(self.actionSkater_Stats)
        self.menuView.addAction(self.actionGoalie_Stats)
        self.menuGraph.addAction(self.actionGraph_Data)
        self.menuGraph.addAction(self.actionEdit_Graph)
        self.menuGraph.addAction(self.actionSave_Graph)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuGraph.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        db_name = 'ehmtracking.db'
        self.check_conn()
        self.actionCreate_db.triggered.connect(lambda: self.create_db())
        self.actionLoad_db.triggered.connect(lambda: self.load_db())
        self.actionExit_db.triggered.connect(lambda: self.exit_db())
        self.actionExit.triggered.connect(lambda: self.exit_app())

    def check_conn(self):
        if not self.conn_status:
            self.database_display.hide()
            self.actionCreate_db.setDisabled(False)
            self.actionExit_db.setDisabled(True)
            self.actionLoad_db.setDisabled(False)
        else:
            self.database_display.show()
            self.actionCreate_db.setDisabled(True)
            self.actionExit_db.setDisabled(False)
            self.actionLoad_db.setDisabled(True)

    def create_db(self):
        if self.conn_status:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Cannot create database - database currently running")
            msg.setInformativeText("Exit the current database and try again")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            i = msg.exec_()
        else:
            create_db_window = QtWidgets.QDialog()
            create_db_window.ui = Form()
            create_db_window.ui.setupUi(create_db_window)
            if create_db_window.exec_():
                if create_db_window.ui.create_dbname:
                    text = create_db_window.ui.create_dbname
                    if text[-1] != 'b' or text[-2] != 'd' or text[-3] != '.':
                        text += '.db'
                        print(text)
                        self.conn = ehm.connection(text)
                        if not self.conn:
                            print('Error connecting to database')
                        ehm.create_db(self.conn)
                        self.db_name = text
                    self.conn_status = True
                    self.check_conn()

    def load_db(self):
        if self.conn_status:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Cannot load database - database currently running")
            msg.setInformativeText("Exit the current database and try again")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            i = msg.exec_()
        else:
            self.conn_status = True
            self.check_conn()

    def exit_db(self):
        # if self.conn_status:
        if self.conn:
            self.conn.close()
        self.conn_status = False
        self.check_conn()
        # else:
        # msg = QtWidgets.QMessageBox()
        # msg.setWindowTitle("Error")
        # msg.setText("Cannot exit database - no database loaded")
        # msg.setInformativeText("Exit the current database and try again")
        # msg.setIcon(QtWidgets.QMessageBox.Warning)
        # msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        # msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
        # i = msg.exec_()

    def exit_app(self):
        sys.exit(app.exec_())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EHMtracker"))
        self.skaterstats_button.setStatusTip(_translate("MainWindow", "View skater stats"))
        self.skaterstats_button.setText(_translate("MainWindow", "Skater Stats"))
        self.players_button.setStatusTip(_translate("MainWindow", "View players"))
        self.players_button.setText(_translate("MainWindow", "Players"))
        self.import_button.setStatusTip(_translate("MainWindow", "Import data to the database"))
        self.import_button.setText(_translate("MainWindow", "Import"))
        self.attributes_button.setStatusTip(_translate("MainWindow", "View player attributes"))
        self.attributes_button.setText(_translate("MainWindow", "Attributes"))
        self.goaliestats_button.setStatusTip(_translate("MainWindow", "View goalie stats"))
        self.goaliestats_button.setText(_translate("MainWindow", "Goalie Stats"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuGraph.setTitle(_translate("MainWindow", "Graph"))
        self.actionCreate_db.setText(_translate("MainWindow", "Create Database"))
        self.actionCreate_db.setStatusTip(_translate("MainWindow", "Create a new database"))
        self.actionCreate_db.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionLoad_db.setText(_translate("MainWindow", "Load Database"))
        self.actionLoad_db.setStatusTip(_translate("MainWindow", "Load an existing database"))
        self.actionLoad_db.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionExit_db.setText(_translate("MainWindow", "Exit Database"))
        self.actionExit_db.setStatusTip(_translate("MainWindow", "Exit current database"))
        self.actionExit_db.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit the program"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPlayers.setText(_translate("MainWindow", "Players"))
        self.actionAttributes.setText(_translate("MainWindow", "Attributes"))
        self.actionSkater_Stats.setText(_translate("MainWindow", "Skater Stats"))
        self.actionGoalie_Stats.setText(_translate("MainWindow", "Goalie Stats"))
        self.actionGraph_Data.setText(_translate("MainWindow", "Create Graph"))
        self.actionEdit_Graph.setText(_translate("MainWindow", "Edit Graph"))
        self.actionSave_Graph.setText(_translate("MainWindow", "Save Graph"))


if __name__ == "__main__":
    # import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
