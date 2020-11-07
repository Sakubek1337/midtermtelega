import sqlite3 as sql
from dataz import remove_player, get_playerbox, add_playerbox, update_boxes
from dataz import get_player, update_points, add_player
import dataz
import rankz as rnk
import telebot
import random


def randombox():
    num = random.randint(1, 1000)
    boxes_names = ['Silver Box', 'Golden Box', 'Platinum Box', 'Legendary Box']
    if num > 992:
        got = boxes_names[3]
    elif num > 945:
        got = boxes_names[2]
    elif num > 595:
        got = boxes_names[1]
    else:
        got = boxes_names[0]
    return got


def times(nick):
    base = sql.connect('gtnp.db')
    c = base.cursor()
    timez = dataz.get_playertime(nick, c)
    return timez


def boxes(nick):
    base = sql.connect('gtnp.db')
    c = base.cursor()
    boxez = get_playerbox(nick, c)
    return boxez


def person(nick):
    base = sql.connect('gtnp.db')
    c = base.cursor()
    verd = dataz.is_real(nick)
    if verd == 'false':
        with base:
            if nick != 'Sakubek':
                c.execute("INSERT INTO real VALUES (:nick,)", {'nick': nick})


def register(nick):
    base = sql.connect('gtnp.db')
    c = base.cursor()
    score = get_player(nick, c)
    hasbox = get_playerbox(nick, c)
    hastw = dataz.get_playertw(nick, c)
    hastime = dataz.get_playertime(nick, c)
    if score is None:
        add_player(nick, c, base)
    if hasbox is None:
        add_playerbox(nick, c, base)
    if hastime is None:
        dataz.add_time(nick, c, base)
    if hastw is None:
        dataz.add_playertw(nick, c, base)


def pointsgtn(name):
    base = sql.connect('gtnp.db')
    c = base.cursor()
    score = get_player(name, c)
    return score[1]


def scoregtn(name):
    base = sql.connect('gtnp.db')
    c = base.cursor()
    score = get_player(name, c)
    if score is not None:
        base.close()
        return f'{score[0]} - {score[1]}'
    else:
        add_player(name, c, base)
        score = get_player(name, c)
        base.close()
        return f'{score[0]} - {score[1]}'


def scoreboard():
    base = sql.connect('gtnp.db')
    c = base.cursor()
    i = 1
    for row in c.execute('SELECT * FROM players ORDER BY points DESC'):
        print(f'{i}.{row[0]} ({rnk.whatrank(row[1])}) - {row[1]}')
        i += 1
    base.close()


def timeboard():
    base = sql.connect('gtnp.db')
    c = base.cursor()


def telboard():
    base = sql.connect('gtnp.db')
    c = base.cursor()

    listz = '🌎World\'s Top 30 players: \n'
    i = 1
    for row in c.execute('SELECT * FROM players ORDER BY points DESC'):
        if i < 31:
            imya = row[0]

            if i == 1:
                listz += f'🥇 {imya} — {row[1]} pts\n'
                i += 1
            elif i == 2:
                listz += f'🥈 {imya} — {row[1]} pts\n'
                i += 1
            elif i == 3:
                listz += f'🥉 {imya} — {row[1]} pts\n'
                i += 1
            else:
                listz += f'{i}. {imya} — {row[1]} pts\n'
                i += 1
        else:
            break
    base.close()
    return listz


def localboard():
    base = sql.connect('gtnp.db')
    c = base.cursor()
    listz = '🇰🇬Local Top players: \n'
    reals = []
    for g in c.execute("""SELECT * FROM real ORDER BY nick"""):
        reals.append(g[0])
    i = 1
    for row in c.execute('SELECT * FROM players ORDER BY points DESC'):
        if row[0] in reals:
            imya = row[0]
            if i == 1:
                listz += f'🥇 {imya} — {row[1]} pts\n'
                i += 1
            elif i == 2:
                listz += f'🥈 {imya} — {row[1]} pts\n'
                i += 1
            elif i == 3:
                listz += f'🥉 {imya} — {row[1]} pts\n'
                i += 1
            else:
                listz += f'{i}. {imya} — {row[1]} pts\n'
                i += 1
    return listz


def remove(nick):
    base = sql.connect('gtnp.db')
    c = base.cursor()
    remove_player(nick, c, base)
    base.close()


def update(nick, points):
    base = sql.connect('gtnp.db')
    c = base.cursor()
    update_points(nick, points, c, base)
    base.close()


def updateboxes(nick, boxname, amount):
    base = sql.connect('gtnp.db')
    c = base.cursor()
    update_boxes(nick, boxname, amount, c, base)
    base.close()


def updatetime(nick, hours, mins, secs):
    base = sql.connect('gtnp.db')
    c = base.cursor()
    dataz.update_time(nick, hours, mins, secs, c, base)
    base.close()


def updatetw(nick, tws):
    base = sql.connect('gtnp.db')
    c = base.cursor()
    dataz.update_tw(nick, tws, c, base)
    base.close()
