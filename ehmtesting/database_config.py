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


def create_player_attributes(conn):
    statement = """CREATE TABLE IF NOT EXISTS playerattributes (id integer, name text, nation text, teamplaying text, 
    leagueplaying text, teamrights text, positions text, age integer, determination integer default 1, aggression 
    integer default 1, anticipation integer default 1, bravery integer default 1, flair integer default 1, 
    influence integer default 1, teamwork integer default 1, creativity integer default 1, workrate integer default 
    1, acceleration integer default 1, agility integer default 1, balance integer default 1, hitting integer default 
    1, speed integer default 1, stamina integer default 1, strength integer default 1, checking integer default 1, 
    deflections integer default 1, deking integer default 1, faceoffs integer default 1, offthepuck integer default 
    1, passing integer default 1, pokecheck integer default 1, positioning integer default 1, slapshot integer 
    default 1, stickhandling integer default 1, wristshot integer default 1, blocker integer default 1, glove integer 
    default 1, reboundcontrol integer default 1, recovery integer default 1, reflexes integer default 1); """
    try:
        c = conn.cursor()
        c.execute(statement)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def main():
    conn = connection()
    create_player_attributes(conn)
    conn.close()


if __name__ == '__main__':
    main()
