# Written by Adam Pumphrey
# EHM Tracker file

import stats_csv as statformat
import stats_csv_parse as statparse
import attribute_csv as attparse
import sqlite3
import database_config as db_config


def get_statimport_files(statfile, teamid):
    """
    Takes a raw .csv file exported from EHM and creates up to four parsed stat files - regular season skates, regular
    season goalies, playoff skaters, and playoff goalies.
    :param statfile: string, name of .csv file exported from EHM's NHL stat page
    :param teamid: string, the identifier of the team you want to grab data for - may vary between EHM databases -
                   easy way to find teamid is to open the .csv file and look for the team you want eg) 'Canucks'
    :return:
    """
    statformat.parse_statfile(statfile, teamid)


def get_attimport_list(attfile, playeratts, year):
    """
    Takes a raw .csv file exported from EHM Assistant and formats, parses, and creates one file - used for importing
    players and player attributes. Returns a list to be used for importing.
    :param attfile: string, name of .csv file exported from EHM Assistant (with correct filters)
    :param playeratts: string, name of formatted .csv file created from attparse.format_file
    :param year: string, the year/season of the import with a semicolon eg) '2020;'
    :return: list, used for importing players and their attributes
    """
    attparse.format_file(attfile, year)
    return attparse.parse_data(playeratts)


def get_skaterstat_list(skaterfile):
    """
    Takes a formatted .csv file created via get_statimport_files and parses to obtain a list used for importing
    the retrieved data.
    :param skaterfile: string, name of formatted .csv file created via get_statimport_files
    :return: list, used for importing skater reg season/playoff stats
    """
    statparse.format_skaters(skaterfile)
    return statparse.parse_skaters(skaterfile)


def get_goaliestat_list(goaliefile):
    """
    Takes a formatted .csv file created via get_statimport_files and parses to obtain a list used for importing
    the retrieved data.
    :param goaliefile: string, name of formatted .csv file created via get_statimport_files
    :return: list, used for importing goalie reg season/playoff stats
    """
    statparse.format_goalies(goaliefile)
    return statparse.parse_goalies(goaliefile)


def connection(dbname):
    # def connection():
    """
    Establishes connection with ehmtracking.db database via sqlite3.
    :return: sqlite3.Connection - the connection to the ehmtracking.db database in use
    """
    dbname = 'newtest.db'
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        return conn
    except sqlite3.Error as e:
        print(e)
        return conn


def create_db(conn):
    """
    Creates tables in ehmtracking.db if they don't already exist.
    :param conn: sqlite3.Connection, connection to the database
    :return:
    """
    db_config.create_player(conn)
    db_config.create_player_attributes(conn)
    db_config.create_regplayer_stats(conn)
    db_config.create_reggoalie_stats(conn)
    db_config.create_poffplayer_stats(conn)
    db_config.create_poffgoalie_stats(conn)


def select_playertable(conn):
    c = conn.cursor()
    c.execute('''CREATE VIEW IF NOT EXISTS playerdisplay AS SELECT name, nationality, year, age, teamrights, 
    teamplaying, leagueplaying, positions FROM player''')
    result = c.execute("SELECT * FROM playerdisplay")
    return result


def del_playertableview(conn):
    c = conn.cursor()
    c.execute('''DROP VIEW IF EXISTS playerdisplay''')


def select_attributetable(conn):
    c = conn.cursor()
    c.execute('''CREATE VIEW IF NOT EXISTS attdisplay AS SELECT player.year as year, player.name as name, 
    player.teamplaying as team, player.leagueplaying as league, player.age as age, playerattributes.determination, 
    playerattributes.aggression, playerattributes.anticipation, playerattributes.bravery, playerattributes.flair, 
    playerattributes.influence, playerattributes.teamwork, playerattributes.creativity, playerattributes.workrate, 
    playerattributes.acceleration, playerattributes.agility, playerattributes.balance, playerattributes.hitting, 
    playerattributes.speed, playerattributes.stamina, playerattributes.strength, playerattributes.checking, 
    playerattributes.deflections, playerattributes.deking, playerattributes.faceoffs, playerattributes.offthepuck, 
    playerattributes.passing, playerattributes.pokecheck, playerattributes.positioning, playerattributes.slapshot, 
    playerattributes.stickhandling, playerattributes.wristshot, playerattributes.blocker, playerattributes.glove, 
    playerattributes.reboundcontrol, playerattributes.recovery, playerattributes.reflexes FROM playerattributes INNER 
    JOIN player ON player.id WHERE playerattributes.id = player.id''')
    result = c.execute("SELECT * FROM attdisplay")
    return result


def del_attview(conn):
    c = conn.cursor()
    c.execute('''DROP VIEW IF EXISTS attdisplay''')
    
    
def select_techatts(conn):
    c = conn.cursor()
    c.execute('''CREATE VIEW IF NOT EXISTS techattdisplay AS SELECT player.year, player.name, player.teamplaying, 
        player.leagueplaying, player.age, playerattributes.checking, playerattributes.deflections, 
        playerattributes.deking, playerattributes.faceoffs, playerattributes.hitting, playerattributes.offthepuck,
        playerattributes.passing, playerattributes.pokecheck, playerattributes.positioning, playerattributes.slapshot,
        playerattributes.stickhandling, playerattributes.wristshot FROM playerattributes INNER JOIN player ON player.id 
        WHERE playerattributes.id = player.id''')
    result = c.execute("SELECT * FROM techattdisplay")
    return result


def del_techattdisplay(conn):
    c = conn.cursor()
    c.execute("DROP VIEW IF EXISTS techattdisplay")
    
    
def select_mentatts(conn):
    c = conn.cursor()
    c.execute('''CREATE VIEW IF NOT EXISTS mentattdisplay AS SELECT player.year, player.name, player.teamplaying, 
        player.leagueplaying, player.age, playerattributes.aggression, playerattributes.anticipation, 
        playerattributes.bravery, playerattributes.creativity, playerattributes.determination, playerattributes.flair,
        playerattributes.influence, playerattributes.teamwork, playerattributes.workrate FROM playerattributes 
        INNER JOIN player ON player.id WHERE playerattributes.id = player.id''')
    result = c.execute("SELECT * FROM mentattdisplay")
    return result


def del_mentattdisplay(conn):
    c = conn.cursor()
    c.execute("DROP VIEW IF EXISTS mentattdisplay")
    
    
def select_physatts(conn):
    c = conn.cursor()
    c.execute('''CREATE VIEW IF NOT EXISTS physattdisplay AS SELECT player.year, player.name, player.teamplaying, 
        player.leagueplaying, player.age, playerattributes.acceleration, playerattributes.agility, 
        playerattributes.balance, playerattributes.speed, playerattributes.stamina, playerattributes.strength FROM 
        playerattributes INNER JOIN player ON player.id WHERE playerattributes.id = player.id''')
    result = c.execute("SELECT * FROM physattdisplay")
    return result


def del_physattdisplay(conn):
    c = conn.cursor()
    c.execute("DROP VIEW IF EXISTS physattdisplay")


def select_basic_regskaterstats(conn):
    c = conn.cursor()
    c.execute('''CREATE VIEW IF NOT EXISTS regbasicstatdisplay AS SELECT regplayerstats.year, player.name, 
    player.teamplaying, player.leagueplaying, player.age, regplayerstats.gamesplayed, regplayerstats.goals, 
    regplayerstats.assists, regplayerstats.points, regplayerstats.plusminus, regplayerstats.pims, regplayerstats.sog, 
    regplayerstats.shotpercent, regplayerstats.avr, regplayerstats.atoi, regplayerstats.hits FROM regplayerstats 
    INNER JOIN player ON player.id WHERE regplayerstats.id = player.id''')
    result = c.execute("SELECT * FROM regbasicstatdisplay")
    # ['Name', 'Year', 'Team', 'Games Played', 'G', 'A', 'P', '+/-', 'PIM', 'SOG',
    # 'Sh%', 'AvR', 'ATOI', 'HT']
    return result


def del_regbasicstatview(conn):
    c = conn.cursor()
    c.execute('''DROP VIEW IF EXISTS regbasicstatdisplay''')


def select_adv_regskaterstats(conn):
    c = conn.cursor()
    c.execute('''CREATE VIEW IF NOT EXISTS regadvstatdisplay AS SELECT regplayerstats.year, player.name, 
    player.teamplaying, player.leagueplaying, player.age, regplayerstats.gamesplayed, regplayerstats.ppg, 
    regplayerstats.ppa, regplayerstats.ppp, regplayerstats.shg, regplayerstats.sha, regplayerstats.shp, 
    regplayerstats.gwg, regplayerstats.fg, regplayerstats.giveaways, regplayerstats.takeaways, 
    regplayerstats.fopercent, regplayerstats.shotsblocked, regplayerstats.appt, regplayerstats.apkt, 
    regplayerstats.plus, regplayerstats.minus, regplayerstats.firststars FROM regplayerstats INNER JOIN player ON 
    player.id WHERE regplayerstats.id = player.id''')
    result = c.execute("SELECT * FROM regadvstatdisplay")
    # ['Name', 'Team', 'League', 'Year', 'Games Played', 'PPG', 'PPA', 'PPP', 'SHG',
    #  'SHA', 'SHP', 'GWG', 'FG', 'GV', 'TK', 'FO%', 'SHB', 'APPT', 'APKT', '+', '-',
    #  'FS']
    return result


def del_regadvstatview(conn):
    c = conn.cursor()
    c.execute('''DROP VIEW IF EXISTS regadvstatdisplay''')
    
    
def select_adv_poffskaterstats(conn):
    c = conn.cursor()
    c.execute('''CREATE VIEW IF NOT EXISTS poffadvstatdisplay AS SELECT poffplayerstats.year, player.name, 
    player.teamplaying, player.leagueplaying, player.age, poffplayerstats.gamesplayed, poffplayerstats.ppg, 
    poffplayerstats.ppa, poffplayerstats.ppp, poffplayerstats.shg, poffplayerstats.sha, poffplayerstats.shp, 
    poffplayerstats.gwg, poffplayerstats.fg, poffplayerstats.giveaways, poffplayerstats.takeaways, 
    poffplayerstats.fopercent, poffplayerstats.shotsblocked, poffplayerstats.appt, poffplayerstats.apkt, 
    poffplayerstats.plus, poffplayerstats.minus, poffplayerstats.firststars FROM poffplayerstats INNER JOIN player ON 
    player.id WHERE poffplayerstats.id = player.id''')
    result = c.execute("SELECT * FROM poffadvstatdisplay")
    # ['Name', 'Team', 'League', 'Year', 'Games Played', 'PPG', 'PPA', 'PPP', 'SHG',
    #  'SHA', 'SHP', 'GWG', 'FG', 'GV', 'TK', 'FO%', 'SHB', 'APPT', 'APKT', '+', '-',
    #  'FS']
    return result


def del_poffadvstatview(conn):
    c = conn.cursor()
    c.execute('''DROP VIEW IF EXISTS poffadvstatdisplay''')


def select_basic_poffskaterstats(conn):
    c = conn.cursor()
    c.execute('''CREATE VIEW IF NOT EXISTS poffbasicstatdisplay AS SELECT poffplayerstats.year, player.name, 
    player.teamplaying, player.leagueplaying, player.age, poffplayerstats.gamesplayed, poffplayerstats.goals, 
    poffplayerstats.assists, poffplayerstats.points, poffplayerstats.plusminus, poffplayerstats.pims, 
    poffplayerstats.sog, poffplayerstats.shotpercent, poffplayerstats.avr, poffplayerstats.atoi, poffplayerstats.hits 
    FROM poffplayerstats INNER JOIN player ON player.id WHERE poffplayerstats.id = player.id''')
    result = c.execute("SELECT * FROM poffbasicstatdisplay")
    # ['Name', 'Year', 'Team', 'Games Played', 'G', 'A', 'P', '+/-', 'PIM', 'SOG',
    # 'Sh%', 'AvR', 'ATOI', 'HT']
    return result


def del_poffbasicstatview(conn):
    c = conn.cursor()
    c.execute('''DROP VIEW IF EXISTS poffbasicstatdisplay''')


def select_reggoaliestats(conn):
    c = conn.cursor()
    c.execute('''CREATE VIEW IF NOT EXISTS reggoaliestatdisplay AS SELECT reggoaliestats.year, player.name, 
    player.teamplaying, player.leagueplaying, player.age, reggoaliestats.gamesplayed, reggoaliestats.wins, 
    reggoaliestats.losses, reggoaliestats.ties, reggoaliestats.shotsagainst, reggoaliestats.goalsagainst, 
    reggoaliestats.gaa, reggoaliestats.svp, reggoaliestats.shutouts, reggoaliestats.minutes FROM reggoaliestats INNER 
    JOIN player ON player.id WHERE reggoaliestats.id = player.id''')
    result = c.execute("SELECT * FROM reggoaliestatdisplay")
    # ['Name', 'Team', 'League', 'Year', 'GP', 'W', 'L', 'T', 'SHA', 'GA', 'GAA', 'SV%',
    #  'SO', 'MP']
    return result


def del_reggoalstatdisplay(conn):
    c = conn.cursor()
    c.execute('''DROP VIEW IF EXISTS reggoaliestatdisplay''')


def select_poffgoaliestats(conn):
    c = conn.cursor()
    c.execute('''CREATE VIEW IF NOT EXISTS poffgoaliestatdisplay AS SELECT poffgoaliestats.year, player.name, 
    player.teamplaying, player.leagueplaying, player.age, poffgoaliestats.gamesplayed, poffgoaliestats.wins, 
    poffgoaliestats.losses, poffgoaliestats.ties, poffgoaliestats.shotsagainst, poffgoaliestats.goalsagainst, 
    poffgoaliestats.gaa, poffgoaliestats.svp, poffgoaliestats.shutouts, poffgoaliestats.minutes FROM poffgoaliestats 
    INNER JOIN player ON player.id WHERE poffgoaliestats.id = player.id''')
    result = c.execute("SELECT * FROM poffgoaliestatdisplay")
    # ['Name', 'Team', 'League', 'Year', 'GP', 'W', 'L', 'T', 'SHA', 'GA', 'GAA', 'SV%',
    #  'SO', 'MP']
    return result
    
    
def del_poffgoaliestatdisplay(conn):
    c = conn.cursor()
    result = c.execute("DROP VIEW IF EXISTS poffgoaliestatdisplay")
    return result


def import_player(conn, playeratts):
    """
    Imports player data and player attribute data into database.
    We want one line for each player in 'player' table (hence update condition), however we are fine with multiple
    lines per player in 'playerattributes' so we can display attribute growth. 'Player' table contains core player data,
    'playerattributes' is meant to show year-over-year growth of players.
    Idea with 'playerattributes' is to import once a season - therefore no updates necessary.
    :param conn: sqlite3.Connection, connection to the database
    :param playeratts: list, the player data to be imported
    :return:
    """
    c = conn.cursor()
    existing_players = []
    existing_atts = []
    for row in playeratts:
        # check database ('player' table) to see if player already exists
        c.execute("SELECT * FROM player WHERE id = ?", (row['Id'],))
        result = c.fetchall()
        if result:
            # add existing player to existing player list
            existing_players.append(str(result[0][0]))
        # check database ('playerattributes' table) to see if player already has attributes entered for that year/team
        c.execute("SELECT * FROM playerattributes WHERE id = ? AND year = ? AND teamplaying = ?", (row['Id'],
                                                                                                   row['Year'],
                                                                                                   row['Team']))
        result = c.fetchall()
        if result:
            # add player with existing attributes to existing player attributes list
            existing_atts.append((str(result[0][0]), str(result[0][1]), str(result[0][2])))

    for row in playeratts:
        # if player does not exist in database
        if row['Id'] not in existing_players:
            c.execute("INSERT INTO player VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (row['Id'], row['Name'], row['Nation'],
                                                                                row['Year'], row['Age'],
                                                                                row['Team Rights'],
                                                                                row['Team'], row['League'],
                                                                                row['Position(s)']))
        # player exists in database - update values for player
        else:
            c.execute('''UPDATE player SET year = ?, age = ?, teamrights = ?, 
            teamplaying = ?, leagueplaying = ?, positions = ? WHERE id = ?''', (row['Year'], row['Age'],
                                                                                row['Team Rights'], row['Team'],
                                                                                row['League'], row['Position(s)'],
                                                                                row['Id']))
        # if player attribute data does not exist in database
        if (row['Id'], row['Year'], row['Team']) not in existing_atts:
            c.execute('''INSERT INTO playerattributes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (row['Id'], row['Year'], row['Team'],
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
    """
    Imports skater stat data into database.
    Individual stat lines in db denoted by combination of ID, year, and team. Therefore multiple entries can exist
    for the same player in the same year if they change teams during the year. Update condition will overwrite
    existing data for that combination of ID, year, and team - it exists to counter key errors. Skater stats intended
    to be imported once a year, preferably with playoff data.
    :param conn: sqlite3.Connection, connection to the database
    :param skaterstats: list, skater stats to be imported
    :param playoffs: int, optional, denotes playoff stat importing
    :return:
    """
    c = conn.cursor()
    existing_poffstats = []
    existing_regstats = []
    for row in skaterstats:
        # grab ID of current player from 'player' table
        c.execute("SELECT id FROM player WHERE name = ? AND positions = ?", (row['Name'], row['Pos']))
        result = c.fetchall()
        # ID grabbed should match ID given, error if not
        if len(result) == 1:
            row['Id'] = result[0][0]
        else:
            print('error')
            return
        # reg season checking
        if not playoffs:
            # check database ('player' table) to see if player already exists
            c.execute("SELECT * FROM regplayerstats WHERE id = ? AND year = ? AND teamplaying = ?", (row['Id'],
                                                                                                     row['Year'],
                                                                                                     row['Team']))
            result = c.fetchall()
            if result:
                # add existing players to existing player list
                existing_regstats.append((str(result[0][0]), str(result[0][1]), str(result[0][2])))
        # playoff checking
        else:
            # check database ('player' table) to see if player already exists
            c.execute("SELECT * FROM poffplayerstats WHERE id = ? AND year = ? AND teamplaying = ?", (row['Id'],
                                                                                                      row['Year'],
                                                                                                      row['Team']))
            result = c.fetchall()
            if result:
                # add existing players to existing player list
                existing_poffstats.append((str(result[0][0]), str(result[0][1]), str(result[0][2])))

    for row in skaterstats:
        # reg season importing
        if not playoffs:
            # if player stats not already in table
            if (str(row['Id']), row['Year'], row['Team']) not in existing_regstats:
                c.execute('''INSERT INTO regplayerstats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (row['Id'], row['Year'], row['Team'], row['GP'],
                                                         row['G'], row['A'], row['P'], row['+/-'], row['PIM'],
                                                         row['SOG'], row['Sh%'], row['AvR'], row['ATOI'], row['HT'],
                                                         row['PPg'], row['PPa'], row['PPp'], row['SHg'], row['SHa'],
                                                         row['SHp'], row['GWG'], row['FG'], row['GA'], row['TA'],
                                                         row['FO'], row['SB'], row['APPT'], row['APKT'], row['+'],
                                                         row['-'], row['FS']))
            else:
                # player stats already in table - overwrite
                c.execute('''UPDATE regplayerstats SET year = ?, teamplaying = ?, gamesplayed = ?, goals = ?, 
                assists = ?, points = ?, plusminus = ?, pims = ?, sog = ?, shotpercent = ?, avr = ?, atoi = ?, 
                hits = ?, ppg = ?, ppa = ?, ppp = ?, shg = ?, sha = ?, shp = ?, gwg = ?, fg = ?, giveaways = ?, 
                takeaways = ?, fopercent = ?, shotsblocked = ?, appt = ?, apkt = ?, plus = ?, minus = ?, firststars = 
                ? WHERE id = ?''', (row['Year'], row['Team'], row['GP'], row['G'], row['A'], row['P'],
                                    row['+/-'], row['PIM'], row['SOG'], row['Sh%'], row['AvR'], row['ATOI'], row['HT'],
                                    row['PPg'], row['PPa'], row['PPp'], row['SHg'], row['SHa'], row['SHp'], row['GWG'],
                                    row['FG'], row['GA'], row['TA'], row['FO'], row['SB'], row['APPT'], row['APKT'],
                                    row['+'], row['-'], row['FS'], row['Id']))
        # playoff stat importing
        else:
            # if player stats not already in table
            if (str(row['Id']), row['Year'], row['Team']) not in existing_poffstats:
                c.execute('''INSERT INTO poffplayerstats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (row['Id'], row['Year'], row['Team'],
                                                               row['GP'], row['G'], row['A'], row['P'], row['+/-'],
                                                               row['PIM'], row['SOG'], row['Sh%'], row['AvR'],
                                                               row['ATOI'], row['HT'], row['PPg'], row['PPa'],
                                                               row['PPp'], row['SHg'], row['SHa'], row['SHp'],
                                                               row['GWG'], row['FG'], row['GA'], row['TA'],
                                                               row['FO'], row['SB'], row['APPT'], row['APKT'],
                                                               row['+'], row['-'], row['FS']))
            else:
                # player stats already in table - overwrite
                c.execute('''UPDATE poffplayerstats SET year = ?, teamplaying = ?, gamesplayed = ?, goals = ?, 
                assists = ?, points = ?, plusminus = ?, pims = ?, sog = ?, shotpercent = ?, avr = ?, atoi = ?, 
                hits = ?, ppg = ?, ppa = ?, ppp = ?, shg = ?, sha = ?, shp = ?, gwg = ?, fg = ?, giveaways = ?, 
                takeaways = ?, fopercent = ?, shotsblocked = ?, appt = ?, apkt = ?, plus = ?, minus = ?, firststars = 
                ? WHERE id = ?''', (row['Year'], row['Team'], row['GP'], row['G'], row['A'], row['P'],
                                    row['+/-'], row['PIM'], row['SOG'], row['Sh%'], row['AvR'], row['ATOI'], row['HT'],
                                    row['PPg'], row['PPa'], row['PPp'], row['SHg'], row['SHa'], row['SHp'], row['GWG'],
                                    row['FG'], row['GA'], row['TA'], row['FO'], row['SB'], row['APPT'], row['APKT'],
                                    row['+'], row['-'], row['FS'], row['Id']))
    conn.commit()


def import_goaliestats(conn, goaliestats, playoffs=0):
    """
    Imports goalie stat data into database.
    Individual stat lines in db denoted by combination of ID, year, and team. Therefore multiple entries can exist
    for the same player in the same year if they change teams during the year. Update condition will overwrite
    existing data for that combination of ID, year, and team - it exists to counter key errors. Goalie stats intended
    to be imported once a year, preferably with playoff data.
    :param conn: sqlite3.Connection, connection to the database
    :param goaliestats: list, goalie stats to be imported
    :param playoffs: int, optional, denotes playoff stat importing
    :return:
    """
    c = conn.cursor()
    existing_poffgoalstats = []
    existing_reggoalstats = []
    for row in goaliestats:
        # grab ID of current players from 'player' table
        c.execute("SELECT id FROM player WHERE name = ? AND positions = ?", (row['Name'], row['Pos']))
        result = c.fetchall()
        # ID grabbed should match ID given, error if not
        if len(result) == 1:
            row['Id'] = result[0][0]
        else:
            print('error')
            return
        # reg season checking
        if not playoffs:
            # check database ('player' table) to see if player already exists
            c.execute("SELECT * FROM reggoaliestats WHERE id = ? AND year = ? AND teamplaying = ?", (row['Id'],
                                                                                                     row['Year'],
                                                                                                     row['Team']))
            result = c.fetchall()
            if result:
                # add existing players to existing player list
                existing_reggoalstats.append((str(result[0][0]), str(result[0][1]), str(result[0][2])))
        # playoff checking
        else:
            # check database ('player' table) to see if player already exists
            c.execute("SELECT * FROM poffgoaliestats WHERE id = ? AND year = ? AND teamplaying = ?", (row['Id'],
                                                                                                      row['Year'],
                                                                                                      row['Team']))
            result = c.fetchall()
            if result:
                # add existing players to existing player list
                existing_poffgoalstats.append((str(result[0][0]), str(result[0][1]), str(result[0][2])))

    for row in goaliestats:
        # reg season importing
        if not playoffs:
            # if player stats not already in table
            if (str(row['Id']), row['Year'], row['Team']) not in existing_reggoalstats:
                c.execute('''INSERT INTO reggoaliestats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                          (row['Id'], row['Year'], row['Team'], row['GP'], row['W'], row['L'], row['T'],
                           row['SHA'], row['GA'], row['GAA'], row['SV%'], row['SO'], row['TOI']))
            else:
                # player stats already in table - overwrite
                c.execute('''UPDATE reggoaliestats SET year = ?, teamplaying = ?, gamesplayed = ?, 
                wins = ?, losses = ?, ties = ?, shotsagainst = ?, goalsagainst = ?, gaa = ?, svp = ?, shutouts = ?, 
                minutes = ? WHERE id = ?''', (row['Year'], row['Team'], row['GP'], row['W'], row['L'],
                                              row['T'], row['SHA'], row['GA'], row['GAA'], row['SV%'], row['SO'],
                                              row['TOI'], row['Id']))
        # playoff importing
        else:
            # if player stats not already in table
            if (str(row['Id']), row['Year'], row['Team']) not in existing_poffgoalstats:
                c.execute('''INSERT INTO poffgoaliestats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                          (row['Id'], row['Year'], row['Team'], row['GP'], row['W'], row['L'], row['T'],
                           row['SHA'], row['GA'], row['GAA'], row['SV%'], row['SO'], row['TOI']))
            else:
                # player stats already in table - overwrite
                c.execute('''UPDATE poffgoaliestats SET year = ?, teamplaying = ?, gamesplayed = ?, wins = ?, 
                losses = ?, ties = ?, shotsagainst = ?, goalsagainst = ?, gaa = ?, svp = ?, shutouts = ?, minutes = ? 
                WHERE id = ?''', (row['Year'], row['Team'], row['GP'], row['W'], row['L'], row['T'],
                                  row['SHA'], row['GA'], row['GAA'], row['SV%'], row['SO'], row['TOI'], row['Id']))
    conn.commit()


def main():
    attfile = 'canuckatts.csv'
    attfile2 = 'canuckatts2.csv'
    year = '2020;'
    year2 = '2021;'
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
    import_skaterstats(conn, poff_skaterstats, 1)
    import_goaliestats(conn, reg_goaliestats)
    import_goaliestats(conn, poff_goaliestats, 1)
    conn.close()


if __name__ == '__main__':
    main()
