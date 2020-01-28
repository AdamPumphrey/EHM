# Written by Adam Pumphrey
# EHM Assistant CSV parser for player stats
# Opens and retrieves data from csv exported from EHM

# the following variables are to be input during the importing process thru the GUI eventually
filename = 'teststats2.csv'
teamname = 'Canucks'

# TODO: clean this up a bit if possible


def parse_statfile(filename, teamname):
    """
    This function formats and parses a stat .csv file exported from EHM, and writes the corresponding stat data
    to their correct file.
    Function first extracts the year/season (eg. 2020) and adds it as a header, as well as a value in each row.
    Function then parses the file for regular season skater and goalie stat data and creates the files
    'regseason_statimport.csv' and 'regseason_goalstatimport.csv'. Function then checks to see if playoff data exists.
    If playoff data exists, the function parses the file and creates the files 'playoff_statimport.csv' and 
    'playoff_goalstatimport.csv'.
    :param filename: string, the file to be parsed, exported from EHM
    :param teamname: string, the team to grab data for - can be different depending on db eg) 'Edmonton' vs. 'Oilers'
    :return: 
    """
    stats = open(filename, 'r', encoding='cp1252')
    data = stats.readlines()
    stats.close()
    
    # extract year for season
    year = int(data[0][41:43]) * 100
    year2 = int(data[0][46:48])
    if year2 == 0:
        year += 1000
    else:
        year += year2
    year = str(year) + ','
    
    # function removes unnecessary lines of csv from dataset as it moves through the file
    del data[0:4]
    
    # adding year to headers/rows
    for i in range(len(data)):
        header = False
        # designation to add header version or row version
        if 'Name,Team,Pos' in data[i]:
            header = True
        for x in range(len(data[i])):
            if data[i][x] == ',':
                if header:
                    # header version
                    data[i] = data[i][:x + 1] + 'Year,' + data[i][x + 1:]
                else:
                    # row version - year = numerical value (string)
                    data[i] = data[i][:x + 1] + year + data[i][x + 1:]
                break

    regseason_skaterdata = [data[0]]
    data.append(data[0])
    del data[0]
    # extract and write regular season skater stat data to regseason_statimport.csv
    data, regseason_skaterdata = parsedata(teamname, data, regseason_skaterdata)
    create_datafile('regseason_statimport.csv', regseason_skaterdata)

    regseason_goaldata = [data[0]]
    del data[0]
    # extract and write regular season goalie stat data to regseason_goalstatimport.csv
    data, regseason_goaldata = parsedata(teamname, data, regseason_goaldata)
    create_datafile('regseason_goalstatimport.csv', regseason_goaldata)
    
    # checking for playoff data - len(data) > 5 because unnecessary lines exist in the csv before playoff data
    if 'Playoffs' in data[0] and (len(data) > 5):
        del data[0:2]
        playoff_skaterdata = [data[0]]
        del data[0]
        # extract and write playoff skater stat data to playoff_statimport.csv
        data, playoff_skaterdata = parsedata(teamname, data, playoff_skaterdata)
        create_datafile('playoff_statimport.csv', playoff_skaterdata)

        playoff_goaldata = [data[0]]
        del data[0]
        # extract and write playoff goalie stat data to playoff_goalestatimport.csv
        data, playoff_goaldata = parsedata(teamname, data, playoff_goaldata)
        create_datafile('playoff_goalstatimport.csv', playoff_goaldata)


def parsedata(identifier, dataset, new_dataset):
    """
    This function moves rows of data from a stat .csv file to a new dataset.
    Function iterates through a stat csv, and adds the current row to the new dataset if the
    specified identifier (eg. teamname) is present in that row.
    :param identifier: string, the item to be used to identify rows to be moved (usually teamname)
    :param dataset: list, the data to be parsed
    :param new_dataset: list, the new dataset made up of rows removed from the original dataset
    :return: dataset (list), new_dataset (list)
    """
    # loop being True = continue searching
    loop = True
    while loop:
        if identifier in dataset[0]:
            # identifier present so move current row to new dataset
            new_dataset.append(dataset[0])
            del dataset[0]
        # a header row has been reached = searching should stop
        elif 'Name,Year,Team,Pos,' in dataset[0] or 'Playoffs' in dataset[0]:
            loop = False
        else:
            # remove unused data from dataset
            del dataset[0]
    return dataset, new_dataset


def create_datafile(file_name, dataset):
    """
    Function writes the provided data to the specified file.
    A utility function.
    :param file_name: string, the file to be created/written to
    :param dataset: list, the data to be written
    :return:
    """
    datafile = open(file_name, 'w', encoding='cp1252')
    datafile.writelines(dataset)
    datafile.close()


def main():
    parse_statfile(filename, teamname)


if __name__ == '__main__':
    main()
