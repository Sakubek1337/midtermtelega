import telebot
from telebot import types
import bot_config as cfg
import random
import score
import dataz
import rankz as rnk
import time
import sqlite3 as sql

bot = telebot.TeleBot(cfg.TOKEN)

#  necessary variables
twiced = 0
players = {}
box = 'd'
boxes = []
chat_id = ''
streak = 0
lost = False
session = 0
pointx = 0
going = 0
bonus = 0
dic = {}
aydi = ''
mode = 0
started = False
name = 's'
right = 1
onn = 0
num = 0
point = 0
guesses = []
points = 0
maxx = 0
lifes = 0
life = 0
com_start = False
rank = 'gg'


#  ....
@bot.message_handler(commands=['start'])
def welcome(message):
    global com_start
    global name
    global twiced
    global rank
    global aydi
    if not com_start:
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("START", callback_data='start')

        markup.add(item1)

        bot.send_message(message.chat.id,
                         '''Hello, {0.first_name}! I am <b>Game-Bot</b>!
You can play with me the game called "🎲Guess the Number🎲".'''.format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)
        name = '{0.first_name}'.format(message.from_user)

        score.register(name)
        score.person(name)
        pts = score.pointsgtn(name)
        rank = rnk.whatrank_id(pts)

        print(message.chat.id)
        print(name + ' has started bot.')
        l = message.chat.id
        bot.send_message(l, 'Write command /help to see other commands.')
    else:
        bot.send_message(l, 'Game is already started.')
        zapros = '{0.first_name}'.format(message.from_user)
        if name != zapros:
            bot.send_message(l, f'{name} is playing now.')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            global twiced
            global rank
            global pointx
            global going
            global mode
            global streak
            global started
            global points
            global num
            global box
            global boxes
            global mode
            global onn
            global life
            global lifes
            global maxx
            global bonus
            global point
            global session
            global guesses
            global name
            global chat_id
            global com_start

            pointx = 0
            going = 0
            started = False
            right = 1
            onn = 0
            num = 0
            point = 0
            guesses = []
            points = 0
            maxx = 0
            lifes = 0
            life = 0
            bonus = 0

            if call.data == 'start':
                l = call.message.chat.id
                mark = types.InlineKeyboardMarkup(row_width=2)
                it1 = types.InlineKeyboardButton("Normal",
                                                 callback_data='norm')
                it2 = types.InlineKeyboardButton("Hardcore",
                                                 callback_data='hard')
                bot.delete_message(l, call.message.message_id)
                com_start = True

                mark.add(it1, it2)

                bot.send_message(l, '''Choose the game mode...''',
                                 reply_markup=mark)

            elif call.data == 'norm':
                mark = types.InlineKeyboardMarkup(row_width=1)
                it1 = types.InlineKeyboardButton("Nums from 1-5(2 lifes)",
                                                 callback_data='level1n')
                it2 = types.InlineKeyboardButton("Nums from 1-10(3 lifes)",
                                                 callback_data='level2n')
                it3 = types.InlineKeyboardButton("Nums from 1-20(4 lifes)",
                                                 callback_data='level3n')
                it4 = types.InlineKeyboardButton("Nums from 1-35(4 lifes)",
                                                 callback_data='level4n')
                it5 = types.InlineKeyboardButton("Nums from 1-60(5 lifes)",
                                                 callback_data='level5n')
                it6 = types.InlineKeyboardButton("Nums from 1-100(6 lifes)",
                                                 callback_data='level6n')

                mark.add(it1, it2, it3, it4, it5, it6)
                l = call.message.chat.id
                bot.send_message(l, 'Choose the level:', reply_markup=mark)
                bot.delete_message(l, call.message.message_id)
            l = call.message.chat.id
            if '1n' in call.data:
                points = 100
                maxx = 5
                lifes = 2
                bot.delete_message(l, call.message.message_id)
            elif '2n' in call.data:
                points = 150
                maxx = 10
                lifes = 3
                bot.delete_message(l, call.message.message_id)
            elif '3n' in call.data:
                points = 200
                maxx = 20
                lifes = 4
                bot.delete_message(l, call.message.message_id)
            elif '4n' in call.data:
                points = 300
                maxx = 35
                lifes = 4
                bot.delete_message(l, call.message.message_id)
            elif '5n' in call.data:
                points = 400
                maxx = 60
                lifes = 5
                bot.delete_message(l, call.message.message_id)
            elif '6n' in call.data:
                points = 500
                maxx = 100
                lifes = 6
                bot.delete_message(l, call.message.message_id)

            if call.data == 'hard':
                mark = types.InlineKeyboardMarkup(row_width=1)
                it1 = types.InlineKeyboardButton("Nums from 1-2",
                                                 callback_data='level1h')
                it2 = types.InlineKeyboardButton("Nums from 1-3",
                                                 callback_data='level2h')
                it3 = types.InlineKeyboardButton("Nums from 1-4",
                                                 callback_data='level3h')
                it4 = types.InlineKeyboardButton("Nums from 1-5",
                                                 callback_data='level4h')
                it5 = types.InlineKeyboardButton("Nums from 1-6",
                                                 callback_data='level5h')
                it6 = types.InlineKeyboardButton("Nums from 1-7",
                                                 callback_data='level6h')

                mark.add(it1, it2, it3, it4, it5, it6)

                bot.send_message(l, 'Choose the level (YOU HAVE ONLY 1 LIFE!)',
                                 reply_markup=mark)
                bot.delete_message(l, call.message.message_id)

            if '1h' in call.data:
                lifes = 1
                maxx = 2
                points = 100
                bot.delete_message(l, call.message.message_id)
            elif '2h' in call.data:
                lifes = 1
                maxx = 3
                points = 250
                bot.delete_message(l, call.message.message_id)
            elif '3h' in call.data:
                lifes = 1
                maxx = 4
                points = 500
                bot.delete_message(l, call.message.message_id)
            elif '4h' in call.data:
                lifes = 1
                maxx = 5
                points = 850
                bot.delete_message(l, call.message.message_id)
            elif '5h' in call.data:
                lifes = 1
                maxx = 6
                points = 1200
                bot.delete_message(l, call.message.message_id)
            elif '6h' in call.data:
                lifes = 1
                maxx = 7
                points = 1750
                bot.delete_message(l, call.message.message_id)

            if 'level' in call.data and 'n' in call.data:
                mode = 'norm'
                started = True
                bonus = 25
            elif 'level' in call.data and 'h' in call.data:
                mode = 'hard'
                started = True
                bonus = 100
            while started and 'r' in mode:

                going = True
                sec = 0

                while going:
                    global boxes
                    global lost
                    global streak
                    pointx = points
                    streak = 0
                    onn = 1
                    lost = False
                    l = call.message.chat.id

                    while onn == 1:
                        @bot.message_handler(commands=['stop'])
                        def stop(message):
                            global streak
                            global mode
                            global life
                            global started
                            global going
                            global onn
                            global mode
                            global point
                            global name
                            global com_start
                            i = message.chat.id
                            zapros = '{0.first_name}'.format(message.from_user)
                            if name == zapros:
                                print(f'{name} got {point} points.')
                                streak = 0
                                going = False
                                com_start = False
                                started = False
                                onn -= 1
                                mode = '0'
                                life = 0
                                bot.send_message(i, 'Game session stopped!')
                            else:
                                print(zapros, ' is disturbing!!!!!')
                        print('checking...')
                        num = random.randint(1, maxx)
                        print(f'--{num}--')
                        session = 0
                        bot.send_message(l, """We got a number!
Guess🎲""")
                        if lost:
                            pointx = 0
                            streak = 0
                            lost = False
                        life = lifes
                        guesses = ""
                        right = 1

                        while life > 0:
                            @bot.message_handler(content_types=['text'])
                            def guess(message):
                                global chat_id
                                i = message.chat.id
                                global lost
                                global name
                                global pointx
                                global session
                                global points
                                global streak
                                global box
                                global onn
                                global twiced
                                global life
                                global bonus
                                global maxx
                                global going
                                global point
                                global guesses
                                global num
                                global right

                                for f in message.text:
                                    if f not in '1234567890':
                                        right -= 1
                                if right != 1:
                                    if life > 0:
                                        c = 'Wrong input! Try again!'
                                        bot.send_message(i, c)
                                else:
                                    right = 1
                                    session = 0
                                    guezz = int(message.text)
                                    if guezz == num:
                                        if pointx == 0:
                                            pointx = points
                                        streak += 1

                                        if mode == 'hard' and streak > 1:
                                            pointx += 25

                                        bot.send_message(i, 'Correct!')
                                        if streak % 2 == 0 or mode == 'hard'
                                        and streak > 1:
                                            baze = sql.connect('gtnp.db')
                                            w = baze.cursor()
                                            n = name
                                            twiced = dataz.get_playertw(n, w)
                                            baze.close()
                                            box = score.randombox()
                                            ex = ''
                                            if box == 'Legendary Box':
                                                score.updateboxes(n, 'lbox', 1)
                                            elif box == 'Golden Box':
                                                if twiced[1] > 0:
                                                    ex = 'x2 '
                                                    score.updateboxes(n,
                                                                      'gbox',
                                                                      2)
                                                    score.updatetw(n, -1)
                                                else:
                                                    score.updateboxes(n,
                                                                      'gbox',
                                                                      1)
                                            elif box == 'Platinum Box':
                                                if twiced[1] > 0:
                                                    ex = 'x2 '
                                                    score.updateboxes(name,
                                                                      'pbox',
                                                                      2)
                                                    score.updatetw(name, -1)
                                                else:
                                                    score.updateboxes(name,
                                                                      'pbox',
                                                                      1)
                                            elif box == 'Silver Box':
                                                if twiced[1] > 0:
                                                    ex = 'x2 '
                                                    score.updateboxes(name,
                                                                      'sbox',
                                                                      2)
                                                    score.updatetw(name, -1)
                                                else:
                                                    score.updateboxes(name,
                                                                      'sbox',
                                                                      1)
                                            bot.send_message(i, f"""You got {pointx} points and <b>{ex}{box}</b>!
Keep going!""", parse_mode="html")

                                            """time.sleep(0.1)"""

                                        else:
                                            c = f"You got {pointx} points!"
                                            bot.send_message(i, c)
                                        life = 0
                                        score.update(name, pointx)
                                        point += pointx
                                        print(f"+{pointx}")
                                    else:
                                        life -= 1
                                        if life > 0:
                                            c = f'Incorrect! {life}'
                                            c += ' lifes remaining.'
                                            bot.send_message(i, c)
                                            if guezz > num:
                                                v = 'Given number is smaller.'
                                                bot.send_message(i, v)
                                            else:
                                                v = 'Given number is bigger.'
                                                bot.send_message(i, v)
                                        else:
                                            onn -= 1
                                            bot.send_message(i, f'''You lost!
Hidden number was {num}.
Use command /stop to stop the game.''')
                                            lost = True
                                            time.sleep(0.05)

                            time.sleep(1)
                            sec += 1
                            session += 1
                            o = 24
                            if name == 'Mambetkadyrov':
                                o = 9999
                            print(sec)
                            if session > o:
                                print(f'{name} got {point} points.')
                                streak = 0
                                going = False
                                com_start = False
                                started = False
                                onn -= 1
                                mode = '0'
                                life = 0
                                h = 'Game session stopped due to AFK!'
                                bot.send_message(chat_id, h)

                mins = sec // 60
                hours = 0
                msg = '!'
                sec -= mins * 60
                if mins < 60:
                    msg = f'''Total points - {point}.
You played: {mins} minutes {sec} seconds.'''
                elif mins < 1440:
                    hours = mins // 60
                    mins -= hours * 60
                    if hours > 1:
                        msg = f'''Total points - {point}.
You played: {hours} hours {mins} minutes {sec} seconds.'''
                    elif hours == 1:
                        msg = f'''Total points - {point}.
You played: {hours} hour {mins} minutes {sec} seconds.'''

                bot.send_message(call.message.chat.id, msg)
                score.updatetime(name, hours, mins, sec)

                pts = score.pointsgtn(name)
                newrank = rnk.whatrank_id(pts)
                diff = newrank - rank
                if diff == 1:
                    rank_name = rnk.whatrank(pts)
                    free = rnk.free(newrank)
                    k = "<b>Congratulations</b>"
                    bot.send_message(call.message.chat.id, f"""{k}🎉
You ranked up to - \"{rank_name}\"
Your next {free} boxes will be twiced🎁🎁
(/twicing - to see conditions)""", parse_mode='html')
                    score.updatetw(name, free)
                elif diff > 1:
                    rank_name = rnk.whatrank(pts)
                    free = 0
                    df = newrank - rank
                    for i in range(1, df + 1):
                        free += rnk.free(newrank - i)
                    k = "<b>Congratulations</b>"
                    bot.send_message(call.message.chat.id, f"""{k}🎉
You ranked up to - \"{rank_name}\"
You passed {diff} ranks!!!
Your next {free} boxes will be twiced🎁🎁
(/twicing - to see conditions)""", parse_mode='html')
                    score.updatetw(name, free)
                rank = newrank

            if "box" in call.data:
                base = sql.connect('gtnp.db')
                c = base.cursor()
                have = dataz.get_playerbox(name, c)

                sboxs = have[1]
                gboxs = have[2]
                pboxs = have[3]
                lboxs = have[4]
                which = ''
                chosen = '0'
                can = True
                if 's' in call.data:
                    chosen = 'Silver Box'
                    if sboxs == 0:
                        can = False
                    else:
                        which = "sbox"
                elif 'g' in call.data:
                    chosen = 'Golden Box'
                    if gboxs == 0:
                        can = False
                    else:
                        which = "gbox"
                elif 'p' in call.data:
                    chosen = 'Platinum Box'
                    if pboxs == 0:
                        can = False
                    else:
                        which = "pbox"
                elif 'l' in call.data:
                    chosen = 'Legendary Box'
                    if lboxs == 0:
                        can = False
                    else:
                        which = "lbox"
                l = call.message.chat.id
                if can:
                    rand = 0
                    bot.delete_message(l, call.message.message_id)
                    if which == 'sbox':
                        rand = random.randint(150, 200)
                    elif which == 'gbox':
                        rand = random.randint(300, 500)
                    elif which == 'pbox':
                        rand = random.randint(3000, 4000)
                    elif which == 'lbox':
                        rand = random.randint(15000, 20000)
                    print(name + ' opened ' + which)
                    score.update(name, rand)
                    bot.send_message(l,
                                     f'''Congrats! You got {rand} points!''')
                    score.updateboxes(name, which, (-1))
                    bot.send_message(l, f'''/open , /stats''')

                    pts = score.pointsgtn(name)
                    newrank = rnk.whatrank_id(pts)
                    diff = newrank - rank
                    if diff == 1:
                        rank_name = rnk.whatrank(pts)
                        free = rnk.free(newrank)
                        bot.send_message(l, f"""<b>Congratulations</b>🎉
You ranked up to - \"{rank_name}\"
Your next {free} boxes will be twiced🎁🎁""", parse_mode='html')
                        score.updatetw(name, free)
                        rank = newrank
                    elif diff > 1:
                        rank_name = rnk.whatrank(pts)
                        free = 0
                        df = newrank - rank
                        for i in range(1, df + 1):
                            free += rnk.free(newrank - i)
                        bot.send_message(l, f"""<b>Congratulations</b>🎉
You ranked up to - \"{rank_name}\"
You passed {diff} ranks!!!
Your next {free} boxes will be twiced🎁🎁""", parse_mode='html')
                        score.updatetw(name, free)
                        rank = newrank
                else:
                    bot.send_message(l, f"You don't have any {chosen}es")
                print(have)

    except Exception as e:
        print(repr(e))


@bot.message_handler(commands=['world'])
def welcomer(message):
    global started
    global com_start
    zapros = '{0.first_name}'.format(message.from_user)
    global name
    print(zapros + ' /world')
    listik = score.telboard()
    bot.send_message(message.chat.id, listik)


@bot.message_handler(commands=['local'])
def welcomer(message):
    zapros = '{0.first_name}'.format(message.from_user)
    print(zapros + ' /local')
    listik = score.localboard()
    bot.send_message(message.chat.id, listik)


@bot.message_handler(commands=['top'])
def welcomer(message):
    zapros = '{0.first_name}'.format(message.from_user)
    print(zapros + ' /top')
    bot.send_message(message.chat.id, """World's TOP 30 players - /world
Local TOP players - /local""")


@bot.message_handler(commands=['ranks'])
def welcomew(message):
    global started
    global com_start
    global name
    zapros = '{0.first_name}'.format(message.from_user)
    if name == zapros and not started:
        print(zapros + ' /ranks')
        com_start = False
        started = False
        ranks = rnk.allr()
        bot.send_message(message.chat.id, ranks)


@bot.message_handler(commands=['open'])
def opens(message):
    global started
    global com_start
    i = message.chat.id
    zapros = '{0.first_name}'.format(message.from_user)
    if name == zapros and not started:
        print(zapros + ' /open')
        com_start = False
        started = False
        base = sql.connect('gtnp.db')
        c = base.cursor()
        have = dataz.get_playerbox(name, c)
        sboxs = have[1]
        gboxs = have[2]
        pboxs = have[3]
        lboxs = have[4]
        allb = sboxs + lboxs + pboxs + gboxs
        if allb > 0:
            mark = types.InlineKeyboardMarkup(row_width=1)
            it1 = types.InlineKeyboardButton("Silver Box",
                                             callback_data='sbox')
            it2 = types.InlineKeyboardButton("Golden Box",
                                             callback_data='gbox')
            it3 = types.InlineKeyboardButton("Platinum Box",
                                             callback_data='pbox')
            it4 = types.InlineKeyboardButton("Legendary Box",
                                             callback_data='lbox')
            mark.add(it1, it2, it3, it4)
            bot.send_message(i, """Choose the case you want to open...""",
                             reply_markup=mark)
        else:
            bot.send_message(i, """You don't have any boxes to open :(""")


@bot.message_handler(commands=['stats', 'score'])
def welcomes(message):
    global started
    global com_start
    global name
    zapros = '{0.first_name}'.format(message.from_user)
    if name == zapros and not started:
        print(zapros + ' /status')
        com_start = False
        started = False
        pointz = score.pointsgtn(name)
        timee = score.times(name)
        hours = timee[1]
        minutes = timee[2]
        seconds = timee[3]
        msg = f'''{name} - {pointz}'''
        pointz = score.pointsgtn(name)
        rankk = rnk.whatrank(pointz)
        nex = rnk.next_rank(pointz)
        nexr = rnk.whatrank(nex[2] + 5)
        if nex[0] < 12:
            msg += f'''
Rank - {rankk}.
{nex[1]} points to {nexr}.'''
        else:
            msg += f'''
Rank - {rankk}.'''

        base = sql.connect('gtnp.db')
        c = base.cursor()
        have = dataz.get_playerbox(name, c)
        sboxs = have[1]
        gboxs = have[2]
        pboxs = have[3]
        lboxs = have[4]
        db = sql.connect('gtnp.db')
        d = db.cursor()
        tw = dataz.get_playertw(name, d)
        db.close()

        msg += f"""
Silver Boxes - {sboxs}
Golden Boxes - {gboxs}
Platinum Boxes - {pboxs}
Legendary Boxes - {lboxs}

/open - to open box

Box-twicings - {tw[1]}"""
        if hours > 0:
            if hours > 1:
                msg += f'''

Played: {hours} hours {minutes} minutes {seconds} seconds.'''
            else:
                msg += f'''
Played: {hours} hour {minutes} minutes {seconds} seconds.'''
        else:
            msg += f'''
Played: {minutes} minutes {seconds} seconds.'''

        bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['info'])
def info(message):

    global started
    global com_start
    global name
    zapros = '{0.first_name}'.format(message.from_user)
    if name == zapros and not started:
        print(zapros + ' /info')
        com_start = False
        started = False
        infoo = """
Bot:
Owner: Mambetkadyrov S.K.
Made for: Midterm Exam 2020
Last update: 06.11.2020  07:26 PM

\"Guess the number\":
Goal: To guess hidden number and test own luck🎰
Modes: 2
Levels : 6 * 2
TOP players: ✅
Ranks: ✅
Lucky Boxes: ✅
Time tracker: ✅
Multiplayer (at the same time): 🚫

*Every time you make right guess your streak will increase by 1.
Every even streak you will get 1 random 🎁.
If you lose, your streak will be nullified🚫.

Lucky Boxes🎁:
  Drop chances:
  Silver Box - 59%
  Golden Box - 35%
  Platinum Box - 5%
  Legendary Box - 1%

Conditions of box-twicing:
- Twicing does not work for Legendary Boxes
- If you rank up,
your new number of twiced boxes will be added to your current amount
"""
        bot.send_message(message.chat.id, infoo)


@bot.message_handler(commands=['help'])
def welcomez(message):
    global name
    global started
    global com_start
    zapros = '{0.first_name}'.format(message.from_user)
    if name == zapros and not started:
        print(zapros + ' /help')
        com_start = False
        started = False
        bot.send_message(message.chat.id, """/stats - To see your statistics
/local - To see local TOP players
/world - To see global TOP 30 players
/ranks - To see all ranks
/twicing - To see box-twicing conditions
/help - To see all possible commands
/info - To get additional info
/open - To open box
/start - To start the game
/stop - To stop the game
""")


bot.polling(none_stop=True)
