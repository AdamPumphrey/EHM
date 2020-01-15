# Written by Adam Pumphrey
# EHM Assistant CSV parser for player attributes
# Opens and retrieves data from csv exported from EHM Assistant

import csv

filename = 'testplayers.csv'
csvfile = open(filename)
players = csv.DictReader(csvfile, delimiter=';')
playerdata = []
for row in players:
    # delete blank pair at end
    del row['']
    playerdata.append(row)
    # print(row)
for item in playerdata[0]:
    print(item, playerdata[0][item])
