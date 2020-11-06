import telebot
from telebot import types
import bot_config as cfg
import random
import score
import dataz
import rankz as rnk
import time
import sqlite3 as sql

bot = telebot.TeleBot('TOKEN')

#  necessary variables
twiced = 0
players = {}
box = 'd'
boxes = []
streak = 0
lost = False
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
        pts = score.pointsgtn(name)
        rank = rnk.whatrank_id(pts)

        print(message.chat.id)
        print(name + ' has started bot.')
        bot.send_message(message.chat.id, 'Write /help to see other commands.')
    else:
        bot.send_message(message.chat.id, 'Game is already started.')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
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
            global guesses
            global name
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
                mark = types.InlineKeyboardMarkup(row_width=2)
                it1 = types.InlineKeyboardButton("Normal",
                                                 callback_data='norm')
                it2 = types.InlineKeyboardButton("Hardcore",
                                                 callback_data='hard')
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)
                com_start = True

                mark.add(it1, it2)

                bot.send_message(call.message.chat.id,
                                 '''Choose the game mode...''',
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

                bot.send_message(call.message.chat.id, 'Choose the level:',
                                 reply_markup=mark)
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)

            if '1n' in call.data:
                points = 100
                maxx = 5
                lifes = 2
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)
            elif '2n' in call.data:
                points = 150
                maxx = 10
                lifes = 3
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)
            elif '3n' in call.data:
                points = 200
                maxx = 20
                lifes = 4
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)
            elif '4n' in call.data:
                points = 300
                maxx = 35
                lifes = 4
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)
            elif '5n' in call.data:
                points = 400
                maxx = 60
                lifes = 5
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)
            elif '6n' in call.data:
                points = 500
                maxx = 100
                lifes = 6
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)

            if call.data == 'hard':
                mark = types.InlineKeyboardMarkup(row_width=1)
                it1 = types.InlineKeyboardButton("Level 1 - Nums from 1-2",
                                                 callback_data='level1h')
                it2 = types.InlineKeyboardButton("Level 2 - Nums from 1-3",
                                                 callback_data='level2h')
                it3 = types.InlineKeyboardButton("Level 3 - Nums from 1-4",
                                                 callback_data='level3h')
                it4 = types.InlineKeyboardButton("Level 4 - Nums from 1-5",
                                                 callback_data='level4h')
                it5 = types.InlineKeyboardButton("Level 5 - Nums from 1-6",
                                                 callback_data='level5h')
                it6 = types.InlineKeyboardButton("Level 6 - Nums from 1-7",
                                                 callback_data='level6h')

                mark.add(it1, it2, it3, it4, it5, it6)

                bot.send_message(call.message.chat.id,
                                 'Choose the level (YOU HAVE ONLY 1 LIFE!!!):',
                                 reply_markup=mark)
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)

            if '1h' in call.data:
                lifes = 1
                maxx = 2
                points = 100
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)
            elif '2h' in call.data:
                lifes = 1
                maxx = 3
                points = 250
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)
            elif '3h' in call.data:
                lifes = 1
                maxx = 4
                points = 500
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)
            elif '4h' in call.data:
                lifes = 1
                maxx = 5
                points = 850
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)
            elif '5h' in call.data:
                lifes = 1
                maxx = 6
                points = 1200
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)
            elif '6h' in call.data:
                lifes = 1
                maxx = 7
                points = 1750
                bot.delete_message(call.message.chat.id,
                                   call.message.message_id)

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
                    streak = 0
                    onn = 1
                    lost = False

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
                                bot.send_message(message.chat.id,
                                                 'Game session stopped!')
                            else:
                                print(zapros, ' is disturbing!!!!!')
                        print('checking...')
                        num = random.randint(1, maxx)
                        print(f'--{num}--')
                        bot.send_message(call.message.chat.id,
                                         """We got a number!
Guess🎲""")
                        if lost:
                            pointx = 0
                            streak = 0
                            lost = False
                        life = lifes
                        guesses = ""

                        while life > 0:
                            @bot.message_handler(content_types=['text'])
                            def guess(message):
                                global lost
                                global name
                                global pointx
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
                                        gi = 'Wrong input! Try again!'
                                        bot.send_message(message.chat.id, gi)
                                else:

                                    guezz = int(message.text)
                                    if guezz == num:

                                        pointx += points

                                        streak += 1

                                        bot.send_message(message.chat.id,
                                                         'Correct! Good job!')
                                        if streak % 2 == 0:
                                            idc = message.chat.id
                                            box = score.randombox()
                                            ex = ''
                                            if box == 'Legendary Box':
                                                score.updateboxes(name, 'lbox',
                                                                  1)
                                            elif box == 'Golden Box':
                                                if twiced > 0:
                                                    ex = 'x2 '
                                                    score.updateboxes(name,
                                                                      'gbox',
                                                                      2)
                                                    twiced -= 1
                                                else:
                                                    score.updateboxes(name,
                                                                      'gbox',
                                                                      1)
                                            elif box == 'Platinum Box':
                                                if twiced > 0:
                                                    ex = 'x2 '
                                                    score.updateboxes(name,
                                                                      'pbox',
                                                                      2)
                                                    twiced -= 1
                                                else:
                                                    score.updateboxes(name,
                                                                      'pbox',
                                                                      1)
                                            elif box == 'Silver Box':
                                                if twiced > 0:
                                                    ex = 'x2 '
                                                    score.updateboxes(name,
                                                                      'sbox',
                                                                      2)
                                                    twiced -= 1
                                                else:
                                                    score.updateboxes(name,
                                                                      'sbox',
                                                                      1)
                                            pep = f"You got {pointx} points"
                                            pep += f"""and <b>{ex}{box}</b>!
Keep going!"""
                                            bot.send_message(idc, pep,
                                                             parse_mode="html")

                                            """time.sleep(0.1)"""

                                        else:
                                            f = message.chat.id
                                            k = f"You got {pointx} points!"
                                            bot.send_message(f, k)

                                        life = 0
                                        point += pointx
                                    else:
                                        l = 'Incorrect! '
                                        life -= 1
                                        if life > 0:
                                            l += f'{life} lifes remaining.'
                                            bot.send_message(message.chat.id,
                                                             l)
                                            if guezz > num:
                                                f = message.chat.id
                                                k = 'Given number is smaller.'
                                                bot.send_message(f, k)
                                            else:
                                                f = message.chat.id
                                                k = 'Given number is bigger.'
                                                bot.send_message(f, )
                                        else:
                                            onn -= 1
                                            f = message.chat.id
                                            bot.send_message(f, f'''You lost!
Hidden number was {num}.
Use command /stop to stop the game.''')
                                            lost = True

                            time.sleep(1)
                            sec += 1
                            print(sec)

                    score.update(name, point)
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
                    bot.send_message(call.message.chat.id, f"""<b>Congratulations</b>🎉
You ranked up to - \"{rank_name}\"
Your next {free} boxes will be twiced🎁🎁
(/twicing - to see conditions)""", parse_mode='html')
                elif diff > 1:
                    rank_name = rnk.whatrank(pts)
                    free = 0
                    df = newrank - rank
                    for i in range(1, df + 1):
                        free += rnk.free(newrank - i)
                    bot.send_message(call.message.chat.id, f"""<b>Congratulations</b>🎉
You ranked up to - \"{rank_name}\"
You passed {diff} ranks!!!
Your next {free} boxes will be twiced🎁🎁
(/twicing - to see conditions)""", parse_mode='html')
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

                if can:
                    rand = 0
                    f = call.message.chat.id
                    bot.delete_message(f, call.message.message_id)
                    if which == 'sbox':
                        rand = random.randint(150, 200)
                    elif which == 'gbox':
                        rand = random.randint(500, 700)
                    elif which == 'pbox':
                        rand = random.randint(3000, 4000)
                    elif which == 'lbox':
                        rand = random.randint(15000, 20000)
                    score.update(name, rand)

                    bot.send_message(f, f'Congrats! You got {rand} points!')
                    score.updateboxes(name, which, (-1))
                    bot.send_message(f, f'''/open , /box''')
                else:
                    bot.send_message(f, f"You don't have any {chosen}es")
                print(have)

    except Exception as e:
        print(repr(e))


@bot.message_handler(commands=['top'])
def welcomer(message):
    global started
    global com_start
    zapros = '{0.first_name}'.format(message.from_user)
    global name
    if name == zapros:
        com_start = False
        started = False
        listik = score.telboard()
        bot.send_message(message.chat.id, listik)


@bot.message_handler(commands=['rank'])
def welcomew(message):
    global started
    global com_start
    global name
    zapros = '{0.first_name}'.format(message.from_user)
    if name == zapros and not started:
        com_start = False
        started = False
        pointz = score.pointsgtn(name)
        rankk = rnk.whatrank(pointz)
        nex = rnk.next_rank(pointz)
        nexr = rnk.whatrank(nex[2])
        f = message.chat.id
        if nex[0] < 12:
            bot.send_message(f, f'''Your current rank is - {rankk}.
{nex[1]} points to {nexr}!''')


@bot.message_handler(commands=['ranks'])
def welcomew(message):
    global started
    global com_start
    global name
    zapros = '{0.first_name}'.format(message.from_user)
    if name == zapros and not started:
        com_start = False
        started = False
        ranks = rnk.allr()
        bot.send_message(message.chat.id, ranks)


@bot.message_handler(commands=['open'])
def opens(message):
    global started
    global com_start

    zapros = '{0.first_name}'.format(message.from_user)
    if name == zapros and not started:
        com_start = False
        started = False
        mark = types.InlineKeyboardMarkup(row_width=1)
        it1 = types.InlineKeyboardButton("Silver Box", callback_data='sbox')
        it2 = types.InlineKeyboardButton("Golden Box", callback_data='gbox')
        it3 = types.InlineKeyboardButton("Platinum Box", callback_data='pbox')
        it4 = types.InlineKeyboardButton("Legendary Box", callback_data='lbox')
        mark.add(it1, it2, it3, it4)
        f = message.chat.id
        bot.send_message(f, """Choose the case you want to open...""",
                         reply_markup=mark)


@bot.message_handler(commands=['box'])
def welcomew(message):
    global started
    global com_start
    global name
    zapros = '{0.first_name}'.format(message.from_user)
    if name == zapros and not started:
        com_start = False
        started = False
        base = sql.connect('gtnp.db')
        c = base.cursor()
        have = dataz.get_playerbox(name, c)
        sboxs = have[1]
        gboxs = have[2]
        pboxs = have[3]
        lboxs = have[4]
        allb = have[1] + have[2] + have[3] + have[4]
        if allb > 0:
            bot.send_message(message.chat.id, f"""You have:
Silver Boxes - {sboxs}
Golden Boxes - {gboxs}
Platinum Boxes - {pboxs}
Legendary Boxes - {lboxs}
/open - to open box""")
        else:
            bot.send_message(message.chat.id, '''You don\'t have any boxes!''')


@bot.message_handler(commands=['score'])
def welcomes(message):
    global started
    global com_start
    global name
    zapros = '{0.first_name}'.format(message.from_user)
    if name == zapros and not started:
        com_start = False
        started = False
        pointz = score.pointsgtn(name)
        timee = score.times(name)
        hours = timee[1]
        minutes = timee[2]
        seconds = timee[3]
        if hours > 0:
            if hours > 1:
                mes = f'''{name} - {pointz}
Played: {hours} hours {minutes} minutes {seconds} seconds.'''
            else:
                mes = f'''{name} - {pointz}
Played: {hours} hour {minutes} minutes {seconds} seconds.'''
        else:
            mes = f'''{name} - {pointz}
Played: {minutes} minutes {seconds} seconds.'''
        bot.send_message(message.chat.id, mes)


@bot.message_handler(commands=['info'])
def info(message):
    global started
    global com_start
    global name
    zapros = '{0.first_name}'.format(message.from_user)
    if name == zapros and not started:
        com_start = False
        started = False
        infoo = """Bot:
Owner: Mambetkadyrov S.K.
Made for: Midterm Exam 2020
Last update: 06.11.2020  01:58 AM
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

TOP:
⭐️- means player is a real person"""
        bot.send_message(message.chat.id, infoo)


@bot.message_handler(commands=['help'])
def welcomez(message):
    global name
    global started
    global com_start
    zapros = '{0.first_name}'.format(message.from_user)
    if name == zapros and not started:
        com_start = False
        started = False
        f = message.chat.id
        bot.send_message(f, """/score - To see your points and time
/top - To see current TOP 25 players
/rank - To see your current rank
/ranks - To see all ranks
/com - To see only commands
/twicing - To see box-twicing conditions
/help - To see all possible commands
/box - To see your number of boxes
/info - To get additional info
/open - To open box
/start - To start the game
/stop - To stop the game
""")


@bot.message_handler(commands=['twicing'])
def welcomez(message):
    global name
    global started
    global com_start
    zapros = '{0.first_name}'.format(message.from_user)
    if name == zapros and not started:
        com_start = False
        started = False
        bot.send_message(message.chat.id, """Conditions of box-twicing:
- If bot stops, number of twiced boxes will be nullified🚫
- Twicing does not work for Legendary Boxes
- If you rank up, your new number of twiced boxes
will be added to your current amount
""")


bot.polling(none_stop=True)
