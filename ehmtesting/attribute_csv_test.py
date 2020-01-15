# Written by Adam Pumphrey
# EHM Assistant CSV parser for player attributes
# Opens and retrieves data from csv exported from EHM Assistant

import csv

filename = 'testplayers.csv'


def format_file(file):
    tempfile = open(file, 'r')
    tempdata = tempfile.readlines()
    print(tempdata)

    tempdata[0] = tempdata[0][:15] + 'Team Rights' + tempdata[0][30:]
    print(tempdata[0])

    tempdata[0] = tempdata[0][:27] + 'Position(s)' + tempdata[0][42:]
    print(tempdata[0])

    print(tempdata)
    tempfile.close()
    tempfile = open(file, 'w')
    tempfile.writelines(tempdata)
    tempfile.close()


def parse_data(file):
    csvfile = open(file)
    players = csv.DictReader(csvfile, delimiter=';')
    playerdata = []
    for row in players:
        # delete blank pair at end
        del row['']
        playerdata.append(row)
        print(row)
    for item in playerdata[0]:
        print(item, playerdata[0][item])

    csvfile.close()
