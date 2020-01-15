# Written by Adam Pumphrey
# EHM Assistant CSV parser for player attributes
# Opens and retrieves data from csv exported from EHM Assistant

import csv

filename = 'testplayers.csv'
csvfile = open(filename, 'r')
data = csvfile.readlines()
print(data)

data[0] = data[0][:15] + 'Team Rights' + data[0][30:]
print(data[0])

data[0] = data[0][:27] + 'Position(s)' + data[0][42:]
print(data[0])

print(data)
csvfile.close()
csvfile = open(filename, 'w')
csvfile.writelines(data)
csvfile.close()

csvfile = open(filename)
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
