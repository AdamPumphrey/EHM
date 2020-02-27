# Written by Adam Pumphrey
# CSV parser for player stat files generated from stats_csv_test.py
# Opens and retrieves data from stat csvs
# All files created by this program SHOULD have windows-1252 encoding to deal with umlauts and other characters

import csv

# the following filename variables are to be constant
regseason_filename = 'regseason_statimport.csv'
regseasongoalies_filename = 'regseason_goalstatimport.csv'
playoff_filename = 'playoff_statimport.csv'
playoffgoalies_filename = 'playoff_goalstatimport.csv'


def format_skaters(skaters_name):
    """
    This function performs minor formatting for skater stat import files - regseason_statimport.csv and
    playoff_statimport.csv.
    :param skaters_name: string, filename to be used - should either be regseason_statimport.csv or
    playoff_statimport.csv
    :return:
    """
    tempfile = open(skaters_name, 'r', encoding='cp1252')
    tempdata = tempfile.readlines()

    # minor header formatting
    tempdata[0] = tempdata[0][0:79] + '%' + tempdata[0][80:]
    tempdata[0] = tempdata[0][0:139] + tempdata[0][140:]
    # print(tempdata)
    tempfile.close()

    # re-write formatted data to same file
    tempfile = open(skaters_name, 'w', encoding='cp1252')
    tempfile.writelines(tempdata)
    tempfile.close()


def format_goalies(goalies_name):
    """
    This function performs minor formatting for goalie stat import files - regseason_goalstatimport.csv and
    playoff_goalstatimport.csv.
    :param goalies_name: string, filename to be used - should either be regseason_goalstatimport.csv or
    playoff_goalstatimport.csv
    :return:
    """
    tempfile = open(goalies_name, 'r', encoding='cp1252')
    tempdata = tempfile.readlines()

    # minor header formatting
    tempdata[0] = tempdata[0][0:41] + '%' + tempdata[0][41:]
    # print(tempdata)
    tempfile.close()

    # re-write formatted data to same file
    tempfile = open(goalies_name, 'w', encoding='cp1252')
    tempfile.writelines(tempdata)
    tempfile.close()


def parse_skaters(skaters_name):
    """
    This function parses and formats a skater stat import file for importing skater stat data.
    Function creates a csv dictionary, and appends each row of the dictionary to a list for importing.
    :param skaters_name: string, filename to be used - regseason_statimport.csv or playoff_statimport.csv
    :return: playerstat_data (list)
    """
    skaters = open(skaters_name, 'r', encoding='cp1252')
    playerstats = csv.DictReader(skaters, delimiter=',')
    playerstat_data = []
    for row in playerstats:
        # formatting
        del row['']
        # replace / with , to mirror player attribute position format
        row['Pos'] = row['Pos'].replace('/', ',')
        pos = row['Pos']
        newpos = []
        pos = pos.split(',')
        # Position order handling to coincide with player attribute position formatting
        # LD RD LW C RW
        if 'LD' in pos:
            newpos.append('LD')
        if 'RD' in pos:
            newpos.append('RD')
        if 'LW' in pos:
            newpos.append('LW')
        if 'C' in pos:
            newpos.append('C')
        if 'RW' in pos:
            newpos.append('RW')
        pos = ''
        for i in range(len(newpos)):
            if i == len(newpos) - 1:
                pos += newpos[i]
            else:
                pos += newpos[i] + ','

        if not is_float(row['Sh%']):
            row['Sh%'] = '0.0'

        if len(row['ATOI']) != 5:
            row['ATOI'] = '0' + row['ATOI']

        # print(pos)
        row['Pos'] = pos
        playerstat_data.append(row)

    # testing
    # for i in range(len(playerstat_data)):
    #     for item in playerstat_data[i]:
    #         print(item, playerstat_data[i][item])
    # /testing
    return playerstat_data


def is_float(val):
    try:
        num = float(val)
    except ValueError:
        return False
    return True


def parse_goalies(goalies_name):
    """
    This function parses a goalie stat import file for importing goalie stat data.
    Function creates a csv dictionary, and appends each row of the dictionary to a list for importing.
    :param goalies_name: string, filename to be used - regseason_goalstatimport.csv or playoff_goalstatimport.csv
    :return: goaliestat_data (list)
    """
    goalies = open(goalies_name, 'r', encoding='cp1252')
    goaliestats = csv.DictReader(goalies, delimiter=',')
    goaliestat_data = []
    for row in goaliestats:
        goaliestat_data.append(row)

    # testing
    # for i in range(len(goaliestat_data)):
    #     for item in goaliestat_data[i]:
    #         print(item, goaliestat_data[i][item])
    # /testing
    return goaliestat_data


def main():
    parse_skaters(regseason_filename)
    parse_goalies(regseasongoalies_filename)
    parse_skaters(playoff_filename)
    parse_goalies(playoffgoalies_filename)


if __name__ == '__main__':
    main()
