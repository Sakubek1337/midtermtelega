import sqlite3 as sql


#  baza = sql.connect(':memory:')

#  c = baza.cursor()

def get_playerbox(nickname, s):
    s.execute("SELECT * FROM boxes WHERE nick=:nick", {'nick': nickname})
    return s.fetchone()


def get_player(nickname, s):
    s.execute("SELECT * FROM players WHERE nick=:nick", {'nick': nickname})
    return s.fetchone()


def get_playertime(nick, c):
    c.execute("SELECT * FROM time WHERE nick=:nick", {'nick': nick})
    return c.fetchone()
# ADD ----


def add_player(nickname, s, base):
    with base:
        s.execute("INSERT INTO players VALUES (:nick, 0)", {'nick': nickname})


def add_playerbox(nickname, s, base):
    with base:
        s.execute("INSERT INTO boxes VALUES (:nick, 0, 0, 0, 0)", {'nick': nickname})


def add_time(nick, c, base):
    with base:
        c.execute("INSERT INTO time VALUES (:nick, 0, 0, 0)", {'nick': nick})
#  UPDATE ----


def update_boxes(nicknam, box_name, amount, s, base):
    with base:
        playerboxes = get_playerbox(nicknam, s)
        if box_name == 'sbox':
            current_boxes = playerboxes[1]
            added = current_boxes + amount
            s.execute("UPDATE boxes SET sbox = :sbox WHERE nick=:nick", {'nick': nicknam, 'sbox': added})
        elif box_name == 'gbox':
            current_boxes = playerboxes[2]
            added = current_boxes + amount
            s.execute("UPDATE boxes SET gbox = :gbox WHERE nick=:nick", {'nick': nicknam, 'gbox': added})
        elif box_name == 'pbox':
            current_boxes = playerboxes[3]
            added = current_boxes + amount
            s.execute("UPDATE boxes SET pbox = :pbox WHERE nick=:nick", {'nick': nicknam, 'pbox': added})
        elif box_name == 'lbox':
            current_boxes = playerboxes[4]
            added = current_boxes + amount
            s.execute("UPDATE boxes SET lbox = :lbox WHERE nick=:nick", {'nick': nicknam, 'lbox': added})


def update_points(nicknam, points, s, base):
    with base:
        player = get_player(nicknam, s)
        current_pointz = player[1]
        added = current_pointz + points
        s.execute("UPDATE players SET points = :points WHERE nick=:nick", {'nick': nicknam, 'points': added})


def update_pointz(nicknam, points, s):
    #  sets exactly as points
    s.execute("UPDATE players SET points = :points WHERE nick=:nick", {'nick': nicknam, 'points': points})


def update_time(nick, hours, mins, seconds, c, base):
    with base:
        playertime = get_playertime(nick, c)
        playerhours = playertime[1]
        playerminutes = playertime[2]
        playerseconds = playertime[3]

        added_hours = playerhours + hours
        added_minutes = playerminutes + mins
        added_seconds = playerseconds + seconds

        newmins = added_seconds // 60
        added_minutes += newmins
        added_seconds -= newmins * 60

        newhours = added_minutes // 60
        added_minutes -= newhours * 60
        added_hours += newhours

        c.execute('''UPDATE time SET hours = :hours WHERE nick =:nick''', {'nick': nick, 'hours': added_hours})
        c.execute('''UPDATE time SET mins = :mins WHERE nick =:nick''', {'nick': nick, 'mins': added_minutes})
        c.execute('''UPDATE time SET seconds = :seconds WHERE nick =:nick''', {'nick': nick, 'seconds': added_seconds})
#  REMOVE ----


def remove_player(nickk, c, base):
    with base:
        c.execute('DELETE FROM players WHERE nick=:nick', {'nick': nickk})
