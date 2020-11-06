def allr():
    return """
0 - 1000 : Rookie
1001 - 2000 : Veteran I
2001 - 3000 : Veteran II
3001 - 4000 : Veteran III
4001 - 6000 : Luck Elite I
6001 - 8000 : Luck Elite II
8001 - 10000 : Luck Elite III
10001 - 14000 : Expert
14001 - 20000 : Major Expert
20001 - 30000 : Champion
30001 - 50000 : Grand Champion
50000+ : LEGEND"""


def allrtel():
    return """
0 - 1000 : Rookie
1001 - 2000 : Veteran I
2001 - 3000 : Veteran II
3001 - 4000 : Veteran III
4001 - 6000 : Luck Elite I
6001 - 8000 : Luck Elite II
8001 - 10000 : Luck Elite III
10001 - 14000 : Expert
14001 - 20000 : Major Expert
20001 - 30000 : Champion
30001 - 50000 : Grand Champion
50000+ : LEGEND"""


def ranklist():
    rnkkk = ['Rookie', 'Veteran I', 'Veteran II', 'Veteran III', 'Luck Elite I', 'Luck Elite II', 'Luck Elite III',
             'Expert', 'Major Expert', 'Champion', 'Grand Champion', 'THE LEGEND']
    return rnkkk


def whatrank(points):
    rnk = ranklist()
    if points < 1000:
        return rnk[0]
    elif points < 2000:
        return rnk[1]
    elif points < 3000:
        return rnk[2]
    elif points < 4000:
        return rnk[3]
    elif points < 6000:
        return rnk[4]
    elif points < 8000:
        return rnk[5]
    elif points < 10000:
        return rnk[6]
    elif points < 14000:
        return rnk[7]
    elif points < 20000:
        return rnk[8]
    elif points < 30000:
        return rnk[9]
    elif points < 50000:
        return rnk[10]
    else:
        return rnk[11]


def whatrank_id(points):
    if points < 1000:
        return 0
    elif points < 2000:
        return 1
    elif points < 3000:
        return 2
    elif points < 4000:
        return 3
    elif points < 6000:
        return 4
    elif points < 8000:
        return 5
    elif points < 10000:
        return 6
    elif points < 14000:
        return 7
    elif points < 20000:
        return 8
    elif points < 30000:
        return 9
    elif points < 50000:
        return 10
    else:
        return 11


def free(rank_id):
    much = 0
    if rank_id == 1:
        much = 3
    elif rank_id == 2:
        much = 3
    elif rank_id == 3:
        much = 3
    elif rank_id == 4:
        much = 5
    elif rank_id == 5:
        much = 5
    elif rank_id == 6:
        much = 5
    elif rank_id == 7:
        much = 7
    elif rank_id == 8:
        much = 8
    elif rank_id == 9:
        much = 9
    elif rank_id == 10:
        much = 12
    elif rank_id == 11:
        much = 15
    return much


def next_rank(points):
    idd = whatrank_id(points)
    nam = whatrank(points)
    nextr = 0
    nextp = 0
    if points < 1000:
        nextr = 1
        nextp = 1000
    elif points < 2000:
        nextr = 2
        nextp = 2000
    elif points < 3000:
        nextr = 3
        nextp = 3000
    elif points < 4000:
        nextr = 4
        nextp = 4000
    elif points < 6000:
        nextr = 5
        nextp = 6000
    elif points < 8000:
        nextr = 6
        nextp = 8000
    elif points < 10000:
        nextr = 7
        nextp = 10000
    elif points < 14000:
        nextr = 8
        nextp = 14000
    elif points < 20000:
        nextr = 9
        nextp = 20000
    elif points < 30000:
        nextr = 10
        nextp = 30000
    elif points < 50000:
        nextr = 11
        nextp = 50000
    else:
        nextr = 12
        nextp = -1

    ot = []
    if nextp > 0:
        ot = [nextr, nextp - points, nextp]
    else:
        ot = [12, -1, nextp]
    return ot
