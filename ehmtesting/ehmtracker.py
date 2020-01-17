# Written by Adam Pumphrey
# EHM Tracker file

import stats_csv_test as statformat
import stats_csv_parse as statparse
import attribute_csv_test as attparse
import sqlite3
import database_config as db_config
import os.path


def get_statimport_files(statfile, teamid):
    statformat.parse_statfile(statfile, teamid)


def get_attimport_list(attfile, playeratts):
    attparse.format_file(attfile)
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


def import_player(conn, playeratts):
    c = conn.cursor()
    for row in playeratts:
        c.execute("INSERT INTO player VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (row['Id'], row['Name'], row['Nation'],
                                                                            row['Year'], row['Age'], row['Team Rights'],
                                                                            row['Team'], row['League'],
                                                                            row['Position(s)']))
    conn.commit()


def import_playeratts(conn, playeratts):
    pass


def import_skaterstats(conn, skaterstats):
    pass


def import_goaliestats(conn, goaliestats):
    pass


def import_poff_skaterstats(conn, skaterstats):
    pass


def import_poff_goaliestats(conn, goaliestats):
    pass


def main():
    attfile = 'testplayers.csv'
    statfile = 'teststats2.csv'
    teamid = 'Canucks'
    playeratts = 'playeratt_import.csv'
    regskaters = 'regseason_statimport.csv'
    reggoalies = 'regseason_goalstatimport.csv'
    poffskaters = 'playoff_statimport.csv'
    poffgoalies = 'playoff_goalstatimport.csv'
    conn = connection()
    #create_db(conn)
    get_statimport_files(statfile, teamid)
    player_attlist = get_attimport_list(attfile, playeratts)
    reg_skaterstats = get_skaterstat_list(regskaters)
    reg_goaliestats = get_goaliestat_list(reggoalies)
    poff_skaterstats = get_skaterstat_list(poffskaters)
    poff_goaliestats = get_goaliestat_list(poffgoalies)
    import_player(conn, player_attlist)
    conn.close()


if __name__ == '__main__':
    main()





