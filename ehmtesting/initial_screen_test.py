# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'initial_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import ehmtracker as ehm
import stats_csv as stats
import sys
import os
from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from create_db_window import Ui_dbname_input_dialog as cdb_Form
from choose_import import Ui_import_type_dialog as imp_Form
from choose_year import Ui_choose_year_dialog as year_Form
from choose_team import Ui_choose_team_dialog as team_Form
from filter import Ui_filter_dialog as filter_Form


def drop_views(conn):
    ehm.del_attview(conn)
    ehm.del_playertableview(conn)
    ehm.del_regbasicstatview(conn)
    ehm.del_regadvstatview(conn)
    ehm.del_poffbasicstatview(conn)
    ehm.del_poffadvstatview(conn)
    ehm.del_mentattdisplay(conn)
    ehm.del_physattdisplay(conn)
    ehm.del_techattdisplay(conn)
    ehm.del_reggoalstatdisplay(conn)
    ehm.del_poffgoaliestatdisplay(conn)


class Ui_MainWindow(object):
    def __init__(self):
        self.conn_status = None
        self.conn = None
        self.db_name = ''
        self.current_player = None
        self.player_headers = ['Name', 'Nation', 'Season', 'Age', 'Team Rights', 'Team Playing', 'League',
                               'Position(s)']
        self.att_headers = ['Year', 'Name', 'Team', 'League', 'Age', 'Position(s)', 'Determination', 'Aggression', 'Anticipation',
                            'Bravery', 'Flair', 'Influence', 'Teamwork', 'Creativity', 'Work Rate', 'Acceleration',
                            'Agility', 'Balance', 'Hitting', 'Speed', 'Stamina', 'Strength', 'Checking', 'Deflections',
                            'Deking', 'Faceoffs', 'Off The Puck', 'Passing', 'Pokecheck', 'Positioning', 'Slapshot',
                            'Stickhandling', 'Wristshot', 'Blocker', 'Glove', 'Rebound Control', 'Recovery', 'Reflexes']
        self.techatt_headers = ['Year', 'Name', 'Team', 'League', 'Age', 'Position(s)', 'Checking', 'Deflections', 'Deking',
                                'Faceoffs', 'Hitting', 'Off The Puck', 'Passing', 'Pokecheck', 'Positioning',
                                'Slapshot', 'Stickhandling', 'Wristshot']
        self.mentatt_headers = ['Year', 'Name', 'Team', 'League', 'Age', 'Position(s)', 'Aggression', 'Anticipation', 'Bravery',
                                'Creativity', 'Determination', 'Flair', 'Influence', 'Teamwork', 'Work Rate']
        self.physatt_headers = ['Year', 'Name', 'Team', 'League', 'Age', 'Position(s)', 'Acceleration', 'Agility', 'Balance', 'Speed',
                                'Stamina', 'Strength']
        self.playerbasicstat_headers = ['Year', 'Name', 'Team', 'League', 'Age', 'Position(s)', 'Games Played', 'G', 'A', 'P', '+/-',
                                        'PIM', 'SOG', 'Sh%', 'AvR', 'ATOI', 'HT']
        self.playeradvstat_headers = ['Year', 'Name', 'Team', 'League', 'Age', 'Position(s)', 'Games Played', 'PPG', 'PPA', 'PPP',
                                      'SHG', 'SHA', 'SHP', 'GWG', 'FG', 'GV', 'TK', 'FO%', 'SHB', 'APPT', 'APKT', '+',
                                      '-', 'FS']
        self.goaliestat_headers = ['Year', 'Name', 'Team', 'League', 'Age', 'GP', 'W', 'L', 'T', 'SHA', 'GA', 'GAA',
                                   'SV%', 'SO', 'MP']

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
        MainWindow.setWindowIcon(QtGui.QIcon('ehmtracking.ico'))
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
        self.database_display.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.verticalLayout.addWidget(self.database_display)
        MainWindow.setCentralWidget(self.centralwidget)
        # self.database_display.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # self.database_display.customContextMenuRequested.connect(self.genplayermenu)
        # self.database_display.viewport().installEventFilter(self.database_display)
        self.db_status_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.db_status_label.setFont(font)
        self.db_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.db_status_label.setObjectName("db_status_label")
        self.verticalLayout.addWidget(self.db_status_label)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuImport = QtWidgets.QMenu(self.menubar)
        self.menuImport.setObjectName("menuImport")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuRegular_Season = QtWidgets.QMenu(self.menuView)
        self.menuRegular_Season.setObjectName("menuRegular_Season")
        self.menuPlayoffs = QtWidgets.QMenu(self.menuView)
        self.menuPlayoffs.setObjectName("menuPlayoffs")
        self.menuAttributes = QtWidgets.QMenu(self.menuView)
        self.menuAttributes.setObjectName("menuAttributes")
        # self.menuSkater_Stats = QtWidgets.QMenu(self.menuView)
        # self.menuSkater_Stats.setObjectName("menuSkater_Stats")
        self.menuFilter = QtWidgets.QMenu(self.menubar)
        self.menuFilter.setObjectName("menuFilter")
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
        self.actionImport_Players = QtWidgets.QAction(MainWindow)
        self.actionImport_Players.setObjectName("actionImport_Players")
        self.actionImport_Stats = QtWidgets.QAction(MainWindow)
        self.actionImport_Stats.setObjectName("actionImport_Stats")
        self.actionPlayers = QtWidgets.QAction(MainWindow)
        self.actionPlayers.setObjectName("actionPlayers")
        self.actionAttributes = QtWidgets.QAction(MainWindow)
        self.actionAttributes.setObjectName("actionAttributes")
        self.actionSkater_Stats = QtWidgets.QAction(MainWindow)
        # self.actionSkater_Stats.setObjectName("actionSkater_Stats")
        # self.actionGoalie_Stats = QtWidgets.QAction(MainWindow)
        # self.actionGoalie_Stats.setObjectName("actionGoalie_Stats")
        self.actionGraph_Data = QtWidgets.QAction(MainWindow)
        self.actionGraph_Data.setObjectName("actionGraph_Data")
        self.actionEdit_Graph = QtWidgets.QAction(MainWindow)
        self.actionEdit_Graph.setObjectName("actionEdit_Graph")
        self.actionSave_Graph = QtWidgets.QAction(MainWindow)
        self.actionSave_Graph.setObjectName("actionSave_Graph")
        # self.actionBasic_Stats = QtWidgets.QAction(MainWindow)
        # self.actionBasic_Stats.setObjectName("actionBasic_Stats")
        # self.actionAdvanced_Stats = QtWidgets.QAction(MainWindow)
        # self.actionAdvanced_Stats.setObjectName("actionAdvanced_Stats")
        self.actionReg_Skater_Basic = QtWidgets.QAction(MainWindow)
        self.actionReg_Skater_Basic.setObjectName("actionReg_Skater_Basic")
        self.actionReg_Skater_Advanced = QtWidgets.QAction(MainWindow)
        self.actionReg_Skater_Advanced.setObjectName("actionReg_Skater_Advanced")
        self.actionReg_Goalie = QtWidgets.QAction(MainWindow)
        self.actionReg_Goalie.setObjectName("actionReg_Goalie")
        self.actionPoff_Skater_Basic = QtWidgets.QAction(MainWindow)
        self.actionPoff_Skater_Basic.setObjectName("actionPoff_Skater_Basic")
        self.actionPoff_Skater_Advanced = QtWidgets.QAction(MainWindow)
        self.actionPoff_Skater_Advanced.setObjectName("actionPoff_Skater_Advanced")
        self.actionPoff_Goalie = QtWidgets.QAction(MainWindow)
        self.actionPoff_Goalie.setObjectName("actionPoff_Goalie")
        self.actionTechnical = QtWidgets.QAction(MainWindow)
        self.actionTechnical.setObjectName("actionTechnical")
        self.actionMental = QtWidgets.QAction(MainWindow)
        self.actionMental.setObjectName("actionMental")
        self.actionPhysical = QtWidgets.QAction(MainWindow)
        self.actionPhysical.setObjectName("actionPhysical")
        self.actionSetFilter = QtWidgets.QAction(MainWindow)
        self.actionSetFilter.setObjectName("actionSetFilter")
        self.actionClearFilter = QtWidgets.QAction(MainWindow)
        self.actionClearFilter.setObjectName("actionClearFilter")
        self.menuFile.addAction(self.actionCreate_db)
        self.menuFile.addAction(self.actionLoad_db)
        self.menuFile.addAction(self.actionExit_db)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuImport.addAction(self.actionImport_Players)
        self.menuImport.addAction(self.actionImport_Stats)
        # self.menuSkater_Stats.addAction(self.actionBasic_Stats)
        # self.menuSkater_Stats.addAction(self.actionAdvanced_Stats)
        self.menuRegular_Season.addAction(self.actionReg_Skater_Basic)
        self.menuRegular_Season.addAction(self.actionReg_Skater_Advanced)
        self.menuRegular_Season.addAction(self.actionReg_Goalie)
        self.menuPlayoffs.addAction(self.actionPoff_Skater_Basic)
        self.menuPlayoffs.addAction(self.actionPoff_Skater_Advanced)
        self.menuPlayoffs.addAction(self.actionPoff_Goalie)
        self.menuAttributes.addAction(self.actionTechnical)
        self.menuAttributes.addAction(self.actionMental)
        self.menuAttributes.addAction(self.actionPhysical)
        self.menuView.addAction(self.actionPlayers)
        self.menuView.addAction(self.menuAttributes.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.menuRegular_Season.menuAction())
        self.menuView.addAction(self.menuPlayoffs.menuAction())
        # self.menuView.addAction(self.menuSkater_Stats.menuAction())
        # self.menuView.addAction(self.actionGoalie_Stats)
        self.menuGraph.addAction(self.actionGraph_Data)
        self.menuGraph.addAction(self.actionEdit_Graph)
        self.menuGraph.addAction(self.actionSave_Graph)
        self.menuFilter.addAction(self.actionSetFilter)
        self.menuFilter.addAction(self.actionClearFilter)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuImport.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())
        self.menubar.addAction(self.menuGraph.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.playermenu = QtWidgets.QMenu()
        # self.actionTest = QtWidgets.QAction(self.database_display)
        # self.actionTest.setObjectName("actionTest")
        # self.playermenu.addAction(self.actionTest)

        # db_name = 'ehmtracking.db'
        self.check_conn()
        self.actionCreate_db.triggered.connect(lambda: self.create_db())
        self.actionLoad_db.triggered.connect(lambda: self.load_db())
        self.actionExit_db.triggered.connect(lambda: self.exit_db())
        self.actionExit.triggered.connect(lambda: self.exit_app())
        self.import_button.clicked.connect(lambda: self.import_file())
        self.players_button.clicked.connect(lambda: self.show_playertable(self.conn))
        self.skaterstats_button.clicked.connect(lambda: self.show_regbasicstats(self.conn))
        self.actionPlayers.triggered.connect(lambda: self.show_playertable(self.conn))
        self.actionReg_Skater_Basic.triggered.connect(lambda: self.show_regbasicstats(self.conn))
        self.actionPoff_Skater_Basic.triggered.connect(lambda: self.show_poffbasicstats(self.conn))
        self.actionReg_Skater_Advanced.triggered.connect(lambda: self.show_regadvstats(self.conn))
        self.actionPoff_Skater_Advanced.triggered.connect(lambda: self.show_poffadvstats(self.conn))
        self.goaliestats_button.clicked.connect(lambda: self.show_reggoalstats(self.conn))
        self.actionReg_Goalie.triggered.connect(lambda: self.show_reggoalstats(self.conn))
        self.actionPoff_Goalie.triggered.connect(lambda: self.show_poffgoalstats(self.conn))
        self.attributes_button.clicked.connect(lambda: self.show_attributetable(self.conn))
        self.actionTechnical.triggered.connect(lambda: self.show_techattributetable(self.conn))
        self.actionMental.triggered.connect(lambda: self.show_mentattributetable(self.conn))
        self.actionPhysical.triggered.connect(lambda: self.show_physattributetable(self.conn))
        self.actionImport_Players.triggered.connect(lambda: self.import_file(mode=1))
        self.actionImport_Stats.triggered.connect(lambda: self.import_file(mode=2))

    def check_conn(self):
        if not self.conn_status:
            self.database_display.hide()
            self.db_status_label.show()
            self.actionCreate_db.setDisabled(False)
            self.actionExit_db.setDisabled(True)
            self.actionLoad_db.setDisabled(False)
            self.menuView.setDisabled(True)
            self.menuFilter.setDisabled(True)
            self.menuGraph.setDisabled(True)
        else:
            self.database_display.show()
            self.db_status_label.hide()
            self.actionCreate_db.setDisabled(True)
            self.actionExit_db.setDisabled(False)
            self.actionLoad_db.setDisabled(True)
            self.menuView.setDisabled(False)
            self.menuFilter.setDisabled(False)
            self.menuGraph.setDisabled(False)

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
            create_db_window.ui = cdb_Form()
            create_db_window.ui.setupUi(create_db_window)
            if create_db_window.exec_():
                if create_db_window.ui.create_dbname:
                    text = create_db_window.ui.create_dbname
                    if text[-1] != 'b' or text[-2] != 'd' or text[-3] != '.':
                        text += '.db'
                        # print(text)
                        self.conn = ehm.connection(text)
                        if not self.conn:
                            msg = QMessageBox()
                            msg.setWindowTitle("Error")
                            msg.setText("Error connecting to database")
                            # msg.setInformativeText("Exit the current database and try again")
                            msg.setIcon(QMessageBox.Warning)
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.setDefaultButton(QMessageBox.Ok)
                            i = msg.exec_()
                        ehm.create_db(self.conn)
                        self.db_name = text
                    else:
                        self.conn = ehm.connection(text)
                        if not self.conn:
                            msg = QMessageBox()
                            msg.setWindowTitle("Error")
                            msg.setText("Error connecting to database")
                            # msg.setInformativeText("Exit the current database and try again")
                            msg.setIcon(QMessageBox.Warning)
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.setDefaultButton(QMessageBox.Ok)
                            i = msg.exec_()
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
            filename = QFileDialog.getOpenFileName(MainWindow, 'Open File')
            if filename[0]:
                self.db_name = filename[0]
                self.conn = ehm.connection(filename[0])
                self.show_playertable(self.conn)
                self.conn_status = True
                self.check_conn()

    def import_file(self, mode=0):
        if not self.conn:
            filename = QFileDialog.getOpenFileName(MainWindow, 'Open Database')
            if filename[0]:
                self.db_name = filename[0]
                self.conn = ehm.connection(filename[0])
                # self.show_playertable(self.conn)
                self.conn_status = True
                # self.check_conn()
                drop_views(self.conn)
                self.conn.commit()
        if self.conn:
            if mode == 0:
                choose_import_window = QtWidgets.QDialog()
                choose_import_window.ui = imp_Form()
                choose_import_window.ui.setupUi(choose_import_window)
                if choose_import_window.exec_():
                    if choose_import_window.ui.result == 1:
                        # import player
                        self.import_player()
                    elif choose_import_window.ui.result == 2:
                        # import stats
                        self.import_stats()
            elif mode == 1:
                self.import_player()
            elif mode == 2:
                self.import_stats()

    def import_player(self):
        # import player
        playerfile = QFileDialog.getOpenFileName(MainWindow, 'Choose Player Import File')
        if playerfile[0]:
            choose_year_window = QtWidgets.QDialog()
            choose_year_window.ui = year_Form()
            choose_year_window.ui.setupUi(choose_year_window)
            if choose_year_window.exec_():
                year_val = str(choose_year_window.ui.choose_year_spinbox.value()) + ';'
                player_attlist = ehm.get_attimport_list(playerfile[0], 'playeratt_import.csv', year_val)
                ehm.import_player(self.conn, player_attlist)
                self.conn.commit()
                self.check_conn()
                self.show_playertable(self.conn)

    def import_stats(self):
        # import stats
        statfile = QFileDialog.getOpenFileName(MainWindow, 'Choose Stat Import File')
        if statfile[0]:
            team_id_list = stats.get_team_ids(statfile[0])
            choose_team_window = QtWidgets.QDialog()
            choose_team_window.ui = team_Form()
            choose_team_window.ui.setupUi(choose_team_window)
            choose_team_window.ui.choose_team_combobox.addItems(team_id_list)
            if choose_team_window.exec_():
                team_id = choose_team_window.ui.choose_team_combobox.currentText()
                ehm.get_statimport_files(statfile[0], team_id)
                reg_skaterstats = ehm.get_skaterstat_list('regseason_statimport.csv')
                reg_goaliestats = ehm.get_goaliestat_list('regseason_goalstatimport.csv')
                poff_skaterstats = ehm.get_skaterstat_list('playoff_statimport.csv')
                poff_goaliestats = ehm.get_goaliestat_list('playoff_goalstatimport.csv')
                fail_list = []
                if reg_skaterstats:
                    retval = ehm.import_skaterstats(self.conn, reg_skaterstats)
                    if retval is not None:
                        for i in retval:
                            fail_list.append(i)
                if poff_skaterstats:
                    retval = ehm.import_skaterstats(self.conn, poff_skaterstats, 1)
                    if retval is not None:
                        for i in retval:
                            fail_list.append(i)
                if reg_goaliestats:
                    retval = ehm.import_goaliestats(self.conn, reg_goaliestats)
                    if retval is not None:
                        for i in retval:
                            fail_list.append(i)
                if poff_goaliestats:
                    retval = ehm.import_goaliestats(self.conn, poff_goaliestats, 1)
                    if retval is not None:
                        for i in retval:
                            fail_list.append(i)
                if fail_list:
                    newstr = ''
                    for i in fail_list:
                        newstr += i + '\n'
                    msg = QMessageBox()
                    msg.setWindowTitle("Warning")
                    msg.setText("The following items could not be imported (no corresponding player in "
                                "database):")
                    msg.setInformativeText(newstr)
                    msg.setIcon(QMessageBox.Warning)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    i = msg.exec_()
                self.conn.commit()
                self.rm_import_files()
                self.check_conn()
                self.show_regbasicstats(self.conn)

    def rm_import_files(self):
        if Path('regseason_statimport.csv').is_file():
            os.remove('regseason_statimport.csv')
        if Path('regseason_goalstatimport.csv').is_file():
            os.remove('regseason_goalstatimport.csv')
        if Path('playoff_statimport.csv').is_file():
            os.remove('playoff_statimport.csv')
        if Path('playoff_goalstatimport.csv').is_file():
            os.remove('playoff_goalstatimport.csv')

    def setup_filter(self, conn):
        filter_window = QtWidgets.QDialog()
        filter_window.ui = filter_Form()
        filter_window.ui.setupUi(filter_window)
        # TODO: fill in combo boxes before exec
        # TODO: grab values from filter form
        # TODO: create dynamic queries and views
        # TODO: properly display filtered results

    def show_playertable(self, conn):
        if conn:
            result = ehm.select_playertable(conn)
            self.database_display.setRowCount(0)
            self.database_display.setColumnCount(len(self.player_headers))
            self.database_display.setHorizontalHeaderLabels(self.player_headers)
            self.database_display.setSortingEnabled(False)
            for row_number, row_data in enumerate(result):
                self.database_display.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.database_display.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.database_display.setSortingEnabled(True)

    def show_attributetable(self, conn):
        if conn:
            result = ehm.select_attributetable(conn)
            self.database_display.setRowCount(0)
            self.database_display.setColumnCount(len(self.att_headers))
            self.database_display.setHorizontalHeaderLabels(self.att_headers)
            self.database_display.setSortingEnabled(False)
            for row_number, row_data in enumerate(result):
                self.database_display.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number in (range(6, 38)) or column_number == 0 or column_number == 4:
                        self.database_display.setItem(row_number, column_number, QCustomTableWidgetItem(data))
                    else:
                        self.database_display.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.database_display.setSortingEnabled(True)

    def show_techattributetable(self, conn):
        if conn:
            result = ehm.select_techatts(conn)
            self.database_display.setRowCount(0)
            self.database_display.setColumnCount(len(self.techatt_headers))
            self.database_display.setHorizontalHeaderLabels(self.techatt_headers)
            self.database_display.setSortingEnabled(False)
            for row_number, row_data in enumerate(result):
                self.database_display.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number in (range(6, 18)) or column_number == 0 or column_number == 4:
                        self.database_display.setItem(row_number, column_number, QCustomTableWidgetItem(data))
                    else:
                        self.database_display.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.database_display.setSortingEnabled(True)

    def show_mentattributetable(self, conn):
        if conn:
            result = ehm.select_mentatts(conn)
            self.database_display.setRowCount(0)
            self.database_display.setColumnCount(len(self.mentatt_headers))
            self.database_display.setHorizontalHeaderLabels(self.mentatt_headers)
            self.database_display.setSortingEnabled(False)
            for row_number, row_data in enumerate(result):
                self.database_display.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number in (range(6, 15)) or column_number == 0 or column_number == 4:
                        self.database_display.setItem(row_number, column_number, QCustomTableWidgetItem(data))
                    else:
                        self.database_display.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.database_display.setSortingEnabled(True)

    def show_physattributetable(self, conn):
        if conn:
            result = ehm.select_physatts(conn)
            self.database_display.setRowCount(0)
            self.database_display.setColumnCount(len(self.physatt_headers))
            self.database_display.setHorizontalHeaderLabels(self.physatt_headers)
            self.database_display.setSortingEnabled(False)
            for row_number, row_data in enumerate(result):
                self.database_display.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number in (range(6, 12)) or column_number == 0 or column_number == 4:
                        self.database_display.setItem(row_number, column_number, QCustomTableWidgetItem(data))
                    else:
                        self.database_display.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.database_display.setSortingEnabled(True)

    def show_regbasicstats(self, conn):
        if conn:
            result = ehm.select_basic_regskaterstats(conn)
            self.database_display.setRowCount(0)
            self.database_display.setColumnCount(len(self.playerbasicstat_headers))
            self.database_display.setHorizontalHeaderLabels(self.playerbasicstat_headers)
            self.database_display.setSortingEnabled(False)
            for row_number, row_data in enumerate(result):
                self.database_display.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number in (0, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16):
                        self.database_display.setItem(row_number, column_number, QCustomTableWidgetItem(data))
                    else:
                        self.database_display.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.database_display.setSortingEnabled(True)

    def show_regadvstats(self, conn):
        if conn:
            result = ehm.select_adv_regskaterstats(conn)
            self.database_display.setRowCount(0)
            self.database_display.setColumnCount(len(self.playeradvstat_headers))
            self.database_display.setHorizontalHeaderLabels(self.playeradvstat_headers)
            self.database_display.setSortingEnabled(False)
            for row_number, row_data in enumerate(result):
                self.database_display.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number in (0, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 21, 22, 23):
                        self.database_display.setItem(row_number, column_number, QCustomTableWidgetItem(data))
                    else:
                        self.database_display.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.database_display.setSortingEnabled(True)

    def show_reggoalstats(self, conn):
        if conn:
            result = ehm.select_reggoaliestats(conn)
            self.database_display.setRowCount(0)
            self.database_display.setColumnCount(len(self.goaliestat_headers))
            self.database_display.setHorizontalHeaderLabels(self.goaliestat_headers)
            self.database_display.setSortingEnabled(False)
            for row_number, row_data in enumerate(result):
                self.database_display.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number in (range(4, 15)) or column_number == 0:
                        self.database_display.setItem(row_number, column_number, QCustomTableWidgetItem(data))
                    else:
                        self.database_display.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.database_display.setSortingEnabled(True)

    def show_poffbasicstats(self, conn):
        if conn:
            result = ehm.select_basic_poffskaterstats(conn)
            self.database_display.setRowCount(0)
            self.database_display.setColumnCount(len(self.playerbasicstat_headers))
            self.database_display.setHorizontalHeaderLabels(self.playerbasicstat_headers)
            self.database_display.setSortingEnabled(False)
            for row_number, row_data in enumerate(result):
                self.database_display.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number in (0, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16):
                        self.database_display.setItem(row_number, column_number, QCustomTableWidgetItem(data))
                    else:
                        self.database_display.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.database_display.setSortingEnabled(True)

    def show_poffadvstats(self, conn):
        if conn:
            result = ehm.select_adv_poffskaterstats(conn)
            self.database_display.setRowCount(0)
            self.database_display.setColumnCount(len(self.playeradvstat_headers))
            self.database_display.setHorizontalHeaderLabels(self.playeradvstat_headers)
            self.database_display.setSortingEnabled(False)
            for row_number, row_data in enumerate(result):
                self.database_display.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number in (0, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 21, 22, 23):
                        self.database_display.setItem(row_number, column_number, QCustomTableWidgetItem(data))
                    else:
                        self.database_display.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.database_display.setSortingEnabled(True)

    def show_poffgoalstats(self, conn):
        if conn:
            result = ehm.select_poffgoaliestats(conn)
            self.database_display.setRowCount(0)
            self.database_display.setColumnCount(len(self.goaliestat_headers))
            self.database_display.setHorizontalHeaderLabels(self.goaliestat_headers)
            self.database_display.setSortingEnabled(False)
            for row_number, row_data in enumerate(result):
                self.database_display.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number in (range(4, 15)) or column_number == 0:
                        self.database_display.setItem(row_number, column_number, QCustomTableWidgetItem(data))
                    else:
                        self.database_display.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.database_display.setSortingEnabled(True)

    def exit_db(self):
        # if self.conn_status:
        if self.conn:
            drop_views(self.conn)
            self.conn.commit()
            self.conn.close()
            self.conn = None
            self.conn_status = False
            self.check_conn()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Cannot exit database - no database loaded")
            msg.setInformativeText("Exit the current database and try again")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
            i = msg.exec_()

    def exit_app(self):
        if self.conn:
            drop_views(self.conn)
            self.conn.commit()
            self.conn.close()
            self.conn = None
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EHMtracker"))
        self.db_status_label.setText(_translate("MainWindow", "Database Not Loaded"))
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
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuRegular_Season.setTitle(_translate("MainWindow", "Regular Season Stats"))
        self.menuPlayoffs.setTitle(_translate("MainWindow", "Playoff Stats"))
        self.menuAttributes.setTitle(_translate("MainWindow", "Attributes"))
        # self.menuSkater_Stats.setTitle(_translate("MainWindow", "Skater Stats"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
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
        self.actionImport_Players.setText(_translate("MainWindow", "Import Players"))
        self.actionImport_Players.setStatusTip(_translate("MainWindow", "Import player data"))
        self.actionImport_Players.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionImport_Stats.setText(_translate("MainWindow", "Import Stats"))
        self.actionImport_Stats.setStatusTip(_translate("MainWindow", "Import season stats"))
        self.actionImport_Stats.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPlayers.setText(_translate("MainWindow", "Players"))
        self.actionPlayers.setStatusTip(_translate("MainWindow", "View players"))
        self.actionAttributes.setText(_translate("MainWindow", "Attributes"))
        self.actionAttributes.setStatusTip(_translate("MainWindow", "View player attributes"))
        self.actionSkater_Stats.setText(_translate("MainWindow", "Skater Stats"))
        self.actionSkater_Stats.setStatusTip(_translate("MainWindow", "View skater stats"))
        # self.actionGoalie_Stats.setText(_translate("MainWindow", "Goalie Stats"))
        # self.actionGoalie_Stats.setStatusTip(_translate("MainWindow", "View goalie stats"))
        self.actionSetFilter.setText(_translate("MainWindow", "Set Filter"))
        self.actionClearFilter.setText(_translate("MainWindow", "Clear Filter"))
        self.actionGraph_Data.setText(_translate("MainWindow", "Create Graph"))
        self.actionEdit_Graph.setText(_translate("MainWindow", "Edit Graph"))
        self.actionSave_Graph.setText(_translate("MainWindow", "Save Graph"))
        # self.actionBasic_Stats.setText(_translate("MainWindow", "Basic Stats"))
        # self.actionAdvanced_Stats.setText(_translate("MainWindow", "Advanced Stats"))
        self.actionReg_Skater_Basic.setStatusTip(_translate("MainWindow", "View basic skater regular season stats"))
        self.actionReg_Skater_Basic.setText(_translate("MainWindow", "Skater - Basic"))
        self.actionReg_Skater_Advanced.setStatusTip(_translate("MainWindow",
                                                               "View advanced skater regular season stats"))
        self.actionReg_Skater_Advanced.setText(_translate("MainWindow", "Skater - Advanced"))
        self.actionReg_Goalie.setStatusTip(_translate("MainWindow", "View goalie regular season stats"))
        self.actionReg_Goalie.setText(_translate("MainWindow", "Goalie"))
        self.actionPoff_Skater_Basic.setStatusTip(_translate("MainWindow", "View basic skater playoff stats"))
        self.actionPoff_Skater_Basic.setText(_translate("MainWindow", "Skater - Basic"))
        self.actionPoff_Skater_Advanced.setStatusTip(_translate("MainWindow", "View advanced skater playoff stats"))
        self.actionPoff_Skater_Advanced.setText(_translate("MainWindow", "Skater - Advanced"))
        self.actionPoff_Goalie.setStatusTip(_translate("MainWindow", "View goalie playoff stats"))
        self.actionPoff_Goalie.setText(_translate("MainWindow", "Goalie"))
        self.actionTechnical.setStatusTip(_translate("MainWindow", "View technical attributes"))
        self.actionTechnical.setText(_translate("MainWindow", "Technical"))
        self.actionMental.setStatusTip(_translate("MainWindow", "View mental attributes"))
        self.actionMental.setText(_translate("MainWindow", "Mental"))
        self.actionPhysical.setStatusTip(_translate("MainWindow", "View physical attributes"))
        self.actionPhysical.setText(_translate("MainWindow", "Physical"))


class QCustomTableWidgetItem(QtWidgets.QTableWidgetItem):
    # https://gis.stackexchange.com/questions/208881/qtableview-qtablewidget-alternative-for-floats
    def __init__(self, value):
        super(QCustomTableWidgetItem, self).__init__(str('%s' % value))

    def __lt__(self, other):
        if isinstance(other, QCustomTableWidgetItem):
            selfDataValue = float(self.data(QtCore.Qt.EditRole))
            otherDataValue = float(other.data(QtCore.Qt.EditRole))
            return selfDataValue < otherDataValue
        else:
            return QtWidgets.QTableWidgetItem.__lt__(self, other)


if __name__ == "__main__":
    # import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
