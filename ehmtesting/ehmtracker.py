# Written by Adam Pumphrey
# EHM Tracker file

import stats_csv_test as statformat
import stats_csv_parse as statparse
import attribute_csv_test as attparse
import sqlite3
import database_config as db_config


def get_statimport_files(statfile, teamid):
    statformat.parse_statfile(statfile, teamid)


def get_attimport_list(attfile, playeratts, year):
    attparse.format_file(attfile, year)
    return attparse.parse_data(playeratts)


def get_skaterstat_list(skaterfile):
    statparse.format_skaters(skaterfile)
    return statparse.parse_skaters(skaterfile)


def get_goaliestat_list(goaliefile):
    statparse.format_goalies(goaliefile)
    return statparse.parse_goalies(goaliefile)


def connection():
    dbname = 'ehmtracking.db'
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        return conn
    except sqlite3.Error as e:
        print(e)
        return conn


def create_db(conn):
    db_config.create_player(conn)
    db_config.create_player_attributes(conn)
    db_config.create_regplayer_stats(conn)
    db_config.create_reggoalie_stats(conn)
    db_config.create_poffplayer_stats(conn)
    db_config.create_poffgoalie_stats(conn)


def import_player(conn, playeratts):
    """
    Takes a playeratt_import.csv file.
    :param conn:
    :param playeratts:
    :return:
    """
    c = conn.cursor()
    existing_players = []
    existing_atts = []
    for row in playeratts:
        c.execute("SELECT * FROM player WHERE id = ?", (row['Id'],))
        result = c.fetchall()
        if result:
            existing_players.append(str(result[0][0]))
        c.execute("SELECT * FROM playerattributes WHERE id = ? AND year = ? AND teamplaying = ?", (row['Id'],
                                                                                                   row['Year'],
                                                                                                   row['Team']))
        result = c.fetchall()
        if result:
            existing_atts.append((str(result[0][0]), str(result[0][1]), str(result[0][2])))

    for row in playeratts:
        if row['Id'] not in existing_players:
            c.execute("INSERT INTO player VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (row['Id'], row['Name'], row['Nation'],
                                                                                row['Year'], row['Age'],
                                                                                row['Team Rights'],
                                                                                row['Team'], row['League'],
                                                                                row['Position(s)']))
        else:
            c.execute('''UPDATE player SET year = ?, age = ?, teamrights = ?, 
            teamplaying = ?, leagueplaying = ?, positions = ? WHERE id = ?''', (row['Year'], row['Age'],
                                                                                row['Team Rights'], row['Team'],
                                                                                row['League'], row['Position(s)'],
                                                                                row['Id']))
        if (row['Id'], row['Year'], row['Team']) not in existing_atts:
            c.execute('''INSERT INTO playerattributes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (row['Id'], row['Year'], row['Team'],
                                                                    row['Determination'], row['Aggression'],
                                                                    row['Anticipation'], row['Bravery'], row['Flair'],
                                                                    row['Influence'], row['Teamwork'],
                                                                    row['Creativity'], row['Work Rate'],
                                                                    row['Acceleration'], row['Agility'], row['Balance'],
                                                                    row['Hitting'], row['Speed'], row['Stamina'],
                                                                    row['Strength'], row['Checking'],
                                                                    row['Deflections'], row['Deking'], row['Faceoffs'],
                                                                    row['Off The Puck'], row['Passing'],
                                                                    row['Pokecheck'], row['Positioning'],
                                                                    row['Slapshot'], row['Stickhandling'],
                                                                    row['Wristshot'], row['Blocker'], row['Glove'],
                                                                    row['Rebound Control'], row['Recovery'],
                                                                    row['Reflexes']))

    conn.commit()


def import_skaterstats(conn, skaterstats, playoffs=0):
    c = conn.cursor()
    for row in skaterstats:
        c.execute("SELECT id FROM player WHERE name = ? AND positions = ?", (row['Name'], row['Pos']))
        result = c.fetchall()
        if len(result) == 1:
            row['Id'] = result[0][0]
            print(row)
        else:
            print('error')
            print(row)
            return
        if not playoffs:
            c.execute('''INSERT INTO regplayerstats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (row['Id'], row['Year'], row['Team'], row['GP'], row['G'], row['A'],
                                              row['P'], row['+/-'], row['PIM'], row['SOG'], row['Sh%'], row['AvR'],
                                              row['ATOI'], row['HT'], row['PPg'], row['PPa'], row['PPp'], row['SHg'],
                                              row['SHa'], row['SHp'], row['GWG'], row['FG'], row['GA'], row['TA'],
                                              row['FO'], row['SB'], row['APPT'], row['APKT'], row['+'], row['-'],
                                              row['FS']))
        else:
            c.execute('''INSERT INTO poffplayerstats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (row['Id'], row['Year'], row['Team'], row['GP'], row['G'],
                                                          row['A'], row['P'], row['+/-'], row['PIM'], row['SOG'],
                                                          row['Sh%'], row['AvR'], row['ATOI'], row['HT'], row['PPg'],
                                                          row['PPa'], row['PPp'], row['SHg'], row['SHa'], row['SHp'],
                                                          row['GWG'], row['FG'], row['GA'], row['TA'], row['FO'],
                                                          row['SB'], row['APPT'], row['APKT'], row['+'], row['-'],
                                                          row['FS']))
    conn.commit()


def import_goaliestats(conn, goaliestats):
    pass


def import_poff_goaliestats(conn, goaliestats):
    pass


def main():
    attfile = 'canuckatts.csv'
    year = '2020;'
    statfile = 'canuckstats.csv'
    teamid = 'Canucks'
    playeratts = 'playeratt_import.csv'
    regskaters = 'regseason_statimport.csv'
    reggoalies = 'regseason_goalstatimport.csv'
    poffskaters = 'playoff_statimport.csv'
    poffgoalies = 'playoff_goalstatimport.csv'
    conn = connection()
    create_db(conn)
    get_statimport_files(statfile, teamid)
    player_attlist = get_attimport_list(attfile, playeratts, year)
    reg_skaterstats = get_skaterstat_list(regskaters)
    reg_goaliestats = get_goaliestat_list(reggoalies)
    poff_skaterstats = get_skaterstat_list(poffskaters)
    poff_goaliestats = get_goaliestat_list(poffgoalies)
    import_player(conn, player_attlist)
    import_skaterstats(conn, reg_skaterstats)
    conn.close()


if __name__ == '__main__':
    main()
