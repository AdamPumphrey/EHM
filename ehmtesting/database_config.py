# Written by Adam Pumphrey
# EHM tracker database configuration

import sqlite3


def connection():
    dbname = 'ehmtracking.db'
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        return conn
    except sqlite3.Error as e:
        print(e)
        return conn


def create_player(conn):
    statement = """CREATE TABLE IF NOT EXISTS player (id integer NOT NULL, name text, nationality text, year integer 
    NOT NULL, age integer, teamrights text, teamplaying text NOT NULL, leagueplaying text, positions text, 
    PRIMARY KEY (id, year, teamplaying)); """
    try:
        c = conn.cursor()
        c.execute(statement)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def create_regplayer_stats(conn):
    statement = """CREATE TABLE IF NOT EXISTS regplayerstats (id integer NOT NULL, year integer NOT NULL, 
    teamplaying text NOT NULL, gamesplayed int default 0, goals int default 0, assists int default 0, points int 
    default 0, plusminus int default 0, pims int default 0, sog int default 0, shotpercent real default 0.00, 
    avr real default 0.00, atoi text default '00:00', hits int default 0, ppg int default 0, ppa int default 0, 
    ppp int default 0, shg int default 0, sha int default 0, shp int default 0, gwg int default 0, fg int default 0, 
    giveaways int default 0, takeaways int default 0, fopercent real default 0.00, shotsblocked int default 0, 
    appt text default '00:00', apkt text default '00:00', plus int default 0, minus int default 0, firststars int 
    default 0, PRIMARY KEY ( id, year, teamplaying)); """
    try:
        c = conn.cursor()
        c.execute(statement)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def create_reggoalie_stats(conn):
    statement = """CREATE TABLE IF NOT EXISTS reggoaliestats (id integer NOT NULL, year integer NOT NULL, 
    teamplaying text NOT NULL, gamesplayed int default 0, wins int default 0, losses int default 0, ties int default 
    0, shotsagainst int default 0, goalsagainst int default 0, gaa real default 0.00, svp real default 0.000, 
    shutouts int default 0, minutes int default 0, PRIMARY KEY (id, year, teamplaying)); """
    try:
        c = conn.cursor()
        c.execute(statement)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def create_poffgoalie_stats(conn):
    statement = """CREATE TABLE IF NOT EXISTS poffgoaliestats (id integer NOT NULL, year integer NOT NULL, 
    teamplaying text NOT NULL, gamesplayed int default 0, wins int default 0, losses int default 0, ties int default 
    0, shotsagainst int default 0, goalsagainst int default 0, gaa real default 0.00, svp real default 0.000, 
    shutouts int default 0, minutes int default 0, PRIMARY KEY (id, year, teamplaying)); """
    try:
        c = conn.cursor()
        c.execute(statement)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def create_poffplayer_stats(conn):
    statement = """CREATE TABLE IF NOT EXISTS poffplayerstats (id integer NOT NULL, year integer NOT NULL, 
    teamplaying text NOT NULL, gamesplayed int default 0, goals int default 0, assists int default 0, points int 
    default 0, plusminus int default 0, pims int default 0, sog int default 0, shotpercent real default 0.00, 
    avr real default 0.00, atoi text default '00:00', hits int default 0, ppg int default 0, ppa int default 0, 
    ppp int default 0, shg int default 0, sha int default 0, shp int default 0, gwg int default 0, fg int default 0, 
    giveaways int default 0, takeaways int default 0, fopercent real default 0.00, shotsblocked int default 0, 
    appt text default '00:00', apkt text default '00:00', plus int default 0, minus int default 0, firststars int 
    default 0, PRIMARY KEY ( id, year, teamplaying)); """
    try:
        c = conn.cursor()
        c.execute(statement)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def create_player_attributes(conn):
    statement = """CREATE TABLE IF NOT EXISTS playerattributes (id integer NOT NULL, year integer NOT NULL, 
    teamplaying text NOT NULL, determination integer default 1, aggression integer default 1, anticipation integer 
    default 1, bravery integer default 1, flair integer default 1, influence integer default 1, teamwork integer 
    default 1, creativity integer default 1, workrate integer default 1, acceleration integer default 1, 
    agility integer default 1, balance integer default 1, hitting integer default 1, speed integer default 1, 
    stamina integer default 1, strength integer default 1, checking integer default 1, deflections integer default 1, 
    deking integer default 1, faceoffs integer default 1, offthepuck integer default 1, passing integer default 1, 
    pokecheck integer default 1, positioning integer default 1, slapshot integer default 1, stickhandling integer 
    default 1, wristshot integer default 1, blocker integer default 1, glove integer default 1, reboundcontrol 
    integer default 1, recovery integer default 1, reflexes integer default 1, PRIMARY KEY (id, year, teamplaying));"""
    try:
        c = conn.cursor()
        c.execute(statement)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def main():
    conn = connection()
    create_player(conn)
    create_player_attributes(conn)
    create_regplayer_stats(conn)
    create_poffplayer_stats(conn)
    conn.close()


if __name__ == '__main__':
    main()
