# Written by Adam Pumphrey
# EHM Assistant CSV parser for player stats
# Opens and retrieves data from csv exported from EHM

filename = 'teststats.csv'
teamname = 'Edmonton'


def parsedata(identifier, dataset, new_dataset):
    loop = True
    while loop:
        if identifier in dataset[0]:
            new_dataset.append(dataset[0])
            del dataset[0]
        elif 'Name,Team,Pos,' in dataset[0] or 'Playoffs' in dataset[0]:
            loop = False
        else:
            del dataset[0]
    return dataset, new_dataset


def create_datafile(file_name, dataset):
    datafile = open(file_name, 'w')
    datafile.writelines(dataset)
    datafile.close()


def main():
    stats = open(filename, 'r')
    data = stats.readlines()
    stats.close()

    # TODO: extract and insert year field for each stat row

    del data[0:4]
    regseason_skaterdata = [data[0]]
    data.append(data[0])
    del data[0]
    data, regseason_skaterdata = parsedata(teamname, data, regseason_skaterdata)
    create_datafile('regseason_statimport.csv', regseason_skaterdata)

    regseason_goaldata = [data[0]]
    del data[0]
    data, regseason_goaldata = parsedata(teamname, data, regseason_goaldata)
    create_datafile('regseason_goalstatimport.csv', regseason_goaldata)

    if 'Playoffs' in data[0] and (len(data) > 5):
        del data[0:2]
        playoff_skaterdata = [data[0]]
        del data[0]
        data, playoff_skaterdata = parsedata(teamname, data, playoff_skaterdata)
        create_datafile('playoff_statimport.csv', playoff_skaterdata)

        playoff_goaldata = [data[0]]
        del data[0]
        data, playoff_goaldata = parsedata(teamname, data, playoff_goaldata)
        create_datafile('playoff_goalstatimport.csv', playoff_goaldata)


if __name__ == '__main__':
    main()
