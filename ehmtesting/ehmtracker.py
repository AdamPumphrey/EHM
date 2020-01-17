# Written by Adam Pumphrey
# EHM Tracker file

import stats_csv_test as statformat
import stats_csv_parse as statparse
import attribute_csv_test as attparse


def get_statimport_files(statfile, teamid):
    statformat.parse_statfile(statfile, teamid)


def get_attimport_list(attfile, playeratts):
    attparse.format_file(attfile)
    return attparse.parse_data(playeratts)


def get_skaterstat_list(skaterfile):
    statparse.format_skaters(skaterfile)
    return statparse.parse_skaters(skaterfile)


def get_goaliestat_list(goaliefile):
    statparse.format_goalies(goaliefile)
    return statparse.parse_goalies(goaliefile)


def main():
    attfile = 'testplayers.csv'
    statfile = 'teststats2.csv'
    teamid = 'Canucks'
    playeratts = 'playeratt_import.csv'
    regskaters = 'regseason_statimport.csv'
    reggoalies = 'regseason_goalstatimport.csv'
    poffskaters = 'playoff_statimport.csv'
    poffgoalies = 'playoff_goalstatimport.csv'





