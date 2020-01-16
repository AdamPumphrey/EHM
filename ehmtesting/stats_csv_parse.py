# Written by Adam Pumphrey
# CSV parser for player stat files generated from stats_csv_test.py
# Opens and retrieves data from stat csvs

import csv

regseason_filename = 'regseason_statimport.csv'
regseasongoalies_filename = 'regseason_goalstatimport.csv'
playoff_filename = 'playoff_statimport.csv'
playoffgoalies_filename = 'playoff_goalstatimport.csv'


def format_skaters(skaters_name):
    tempfile = open(skaters_name, 'r')
    tempdata = tempfile.readlines()

    tempdata[0] = tempdata[0][0:74] + '%' + tempdata[0][75:]
    tempdata[0] = tempdata[0][0:134] + tempdata[0][135:]
    print(tempdata)
    tempfile.close()

    tempfile = open(skaters_name, 'w')
    tempfile.writelines(tempdata)
    tempfile.close()


def format_goalies(goalies_name):
    tempfile = open(goalies_name, 'r')
    tempdata = tempfile.readlines()

    tempdata[0] = tempdata[0][0:36] + '%' + tempdata[0][36:]
    print(tempdata)
    tempfile.close()

    tempfile = open(goalies_name, 'w')
    tempfile.writelines(tempdata)
    tempfile.close()


def parse_skaters(skaters_name):
    skaters = open(skaters_name)
    playerstats = csv.DictReader(skaters, delimiter=',')
    playerstat_data = []
    for row in playerstats:
        playerstat_data.append(row)

    # testing
    for i in range(len(playerstat_data)):
        for item in playerstat_data[i]:
            print(item, playerstat_data[i][item])
    # /testing


def parse_goalies(goalies_name):
    goalies = open(goalies_name)
    goaliestats = csv.DictReader(goalies, delimiter=',')
    goaliestat_data = []
    for row in goaliestats:
        goaliestat_data.append(row)

    # testing
    for i in range(len(goaliestat_data)):
        for item in goaliestat_data[i]:
            print(item, goaliestat_data[i][item])
    # /testing


def main():
    parse_skaters(regseason_filename)
    parse_goalies(regseasongoalies_filename)
    parse_skaters(playoff_filename)
    parse_goalies(playoffgoalies_filename)


if __name__ == '__main__':
    main()
