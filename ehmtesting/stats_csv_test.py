# Written by Adam Pumphrey
# EHM Assistant CSV parser for player stats
# Opens and retrieves data from csv exported from EHM

filename = 'teststats2.csv'
teamname = 'Canucks'


def parse_statfile(filename, teamname):
    stats = open(filename, 'r', encoding='cp1252')
    data = stats.readlines()
    stats.close()

    year = int(data[0][41:43]) * 100
    year2 = int(data[0][46:48])
    if year2 == 0:
        year += 1000
    else:
        year += year2
    year = str(year) + ','

    del data[0:4]

    for i in range(len(data)):
        header = False
        if 'Name,Team,Pos' in data[i]:
            header = True
        for x in range(len(data[i])):
            if data[i][x] == ',':
                if header:
                    data[i] = data[i][:x + 1] + 'Year,' + data[i][x + 1:]
                else:
                    data[i] = data[i][:x + 1] + year + data[i][x + 1:]
                break

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


def parsedata(identifier, dataset, new_dataset):
    loop = True
    while loop:
        if identifier in dataset[0]:
            new_dataset.append(dataset[0])
            del dataset[0]
        elif 'Name,Year,Team,Pos,' in dataset[0] or 'Playoffs' in dataset[0]:
            loop = False
        else:
            del dataset[0]
    return dataset, new_dataset


def create_datafile(file_name, dataset):
    datafile = open(file_name, 'w', encoding='cp1252')
    datafile.writelines(dataset)
    datafile.close()


def set_filename(newname):
    filename = newname
    return filename


def set_teamname(newname):
    teamname = newname
    return teamname


def main():
    parse_statfile(filename, teamname)


if __name__ == '__main__':
    main()
