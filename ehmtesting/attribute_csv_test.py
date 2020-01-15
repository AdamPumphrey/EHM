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
        # fix position formatting in output
        if ',' in row['Position(s)']:
            temp = row['Position(s)']
            newtemp = ''.join(temp.split())
            row['Position(s)'] = newtemp

        # backup condition for position formatting
        # if len(row['Position(s)']) > 2:
        #     print(True)

        playerdata.append(row)

    # testing
    for i in range(len(playerdata)):
        for item in playerdata[i]:
            print(item, playerdata[i][item])
    # /testing

    csvfile.close()


def main():
    parse_data(filename)


if __name__ == '__main__':
    main()
