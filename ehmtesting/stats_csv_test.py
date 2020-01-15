# Written by Adam Pumphrey
# EHM exported player stat parser - per team only, not entire league
# Properly formats text file exported from EHM

filename = 'teststats.txt'


def format_stats(file):
    tempstats = open(file, 'r')
    data = tempstats.readlines()
    tempstats.close()
    del data[0:9]
    del data[1]
    del data[-3:]
    newdata = []
    count = 0
    for value in data:
        value = value.split()
        if count > 0:
            value[1] = value[1][:-1]
            value[2] += ' '
            value[1] = value[2] + value[1]
            del value[2]
        else:
            value[6] = '+/-'
            value[10] = value[10] + value[11]
            del value[11]
        for i in range(len(value)):
            value[i] += ' '
        value.append('\n')
        newdata.append(value)
        count += 1
        print(value)

    stats = open(filename, 'w')
    for item in newdata:
        stats.writelines(item)
    stats.close()


def view_file(file):
    temp = open(file)
    data = temp.readlines()
    for item in data:
        print(item)


def main():
    view_file(filename)


if __name__ == '__main__':
    main()
