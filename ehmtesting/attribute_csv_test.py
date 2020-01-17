# Written by Adam Pumphrey
# EHM Assistant CSV parser for player attributes
# Opens and retrieves data from csv exported from EHM Assistant

import csv
import sys

# the following variables are to be input during the importing process thru the GUI eventually
filename = 'testplayers.csv'
newfile = 'playeratt_import.csv'
year = '2020;'


def format_file(file):
    """
    This function formats a .csv file exported from EHM Assistant with the proper options selected.
    Function changes column headers, inserts year value for each row, and writes the modified data
    to playeratt_import.csv - the file to be used for importing player attributes.

    :param file: string, the filename of the .csv exported from EHM Assistant
    :return:
    """
    tempfile = open(file, 'r', encoding='cp1252')
    tempdata = tempfile.readlines()

    # format headers
    tempdata[0] = tempdata[0][:15] + 'Team' + tempdata[0][27:]

    tempdata[0] = tempdata[0][:20] + 'League' + tempdata[0][36:]

    tempdata[0] = tempdata[0][:27] + 'Team Rights' + tempdata[0][42:]

    tempdata[0] = tempdata[0][:39] + 'Position(s)' + tempdata[0][54:]

    tempdata[0] = tempdata[0][:51] + 'Year;' + tempdata[0][51:]

    # print(tempdata)

    # add year data to each row in proper spot
    for i in range(len(tempdata)):
        # ignore the first row (headers)
        if i == 0:
            pass
        else:
            count = 0
            for x in range(len(tempdata[i])):
                # each item is delimited by a semicolon
                if tempdata[i][x] == ';':
                    count += 1
                # insert row after the seventh semicolon delimiter
                if count == 7:
                    tempdata[i] = tempdata[i][:x + 1] + year + tempdata[i][x + 1:]
                    print(tempdata[i])
                    break

    tempfile.close()
    tempfile = open(newfile, 'w', encoding='cp1252')
    tempfile.writelines(tempdata)
    tempfile.close()


def parse_data(file):
    """
    This function parses a 'playeratt_import.csv' for importing player attribute data.
    Function creates a csv dictionary, formats each row correctly, and appends each row of the dictionary
    to a list for importing.
    :param file: string, the filename (playeratt_import.csv)
    :return: playerdata (list)
    """
    csvfile = open(file, 'r', encoding='cp1252')
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
    # for i in range(len(playerdata)):
    #     for item in playerdata[i]:
    #         print(item, playerdata[i][item])
    # /testing

    csvfile.close()
    return playerdata


def main():
    format_file(filename)
    playerdata = parse_data(newfile)


if __name__ == '__main__':
    main()
