def allr():
    return """
0 - 2000 : Rookie
2001 - 7000 : Veteran I
7001 - 12000 : Veteran II
12001 - 20000 : Veteran III
20001 - 30000 : Luck Elite I
30001 - 45000 : Luck Elite II
45001 - 65000 : Luck Elite III
65001 - 100000 : Expert
100001 - 150000 : Major Expert
150001 - 250000 : Champion
250001 - 500000 : Grand Champion
500000+ : LEGEND"""


def allrtel():
    return """
0 - 2000 : Rookie
2001 - 7000 : Veteran I
7001 - 12000 : Veteran II
12001 - 20000 : Veteran III
20001 - 30000 : Luck Elite I
30001 - 45000 : Luck Elite II
45001 - 65000 : Luck Elite III
65001 - 100000 : Expert
100001 - 150000 : Major Expert
150001 - 250000 : Champion
250001 - 500000 : Grand Champion
500000+ : LEGEND"""


def ranklist():
    rnkkk = ['Rookie', 'Veteran I', 'Veteran II', 'Veteran III',
             'Luck Elite I', 'Luck Elite II', 'Luck Elite III',
             'Expert', 'Major Expert', 'Champion', 'Grand Champion',
             'THE LEGEND']
    return rnkkk


def whatrank(points):
    rnk = ranklist()
    if points < 2000:
        return rnk[0]
    elif points < 7000:
        return rnk[1]
    elif points < 12000:
        return rnk[2]
    elif points < 20000:
        return rnk[3]
    elif points < 30000:
        return rnk[4]
    elif points < 45000:
        return rnk[5]
    elif points < 65000:
        return rnk[6]
    elif points < 100000:
        return rnk[7]
    elif points < 150000:
        return rnk[8]
    elif points < 250000:
        return rnk[9]
    elif points < 500000:
        return rnk[10]
    else:
        return rnk[11]


def whatrank_id(points):
    if points < 2000:
        return 0
    elif points < 7000:
        return 1
    elif points < 12000:
        return 2
    elif points < 20000:
        return 3
    elif points < 30000:
        return 4
    elif points < 45000:
        return 5
    elif points < 65000:
        return 6
    elif points < 100000:
        return 7
    elif points < 150000:
        return 8
    elif points < 250000:
        return 9
    elif points < 500000:
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
        much = 4
    elif rank_id == 4:
        much = 4
    elif rank_id == 5:
        much = 5
    elif rank_id == 6:
        much = 5
    elif rank_id == 7:
        much = 6
    elif rank_id == 8:
        much = 7
    elif rank_id == 9:
        much = 8
    elif rank_id == 10:
        much = 9
    elif rank_id == 11:
        much = 10
    return much


def next_rank(points):
    idd = whatrank_id(points)
    nam = whatrank(points)
    nextr = 0
    nextp = 0
    if points < 2000:
        nextr = 1
        nextp = 2000
    elif points < 7000:
        nextr = 2
        nextp = 7000
    elif points < 12000:
        nextr = 3
        nextp = 12000
    elif points < 20000:
        nextr = 4
        nextp = 20000
    elif points < 30000:
        nextr = 5
        nextp = 30000
    elif points < 45000:
        nextr = 6
        nextp = 45000
    elif points < 65000:
        nextr = 7
        nextp = 65000
    elif points < 100000:
        nextr = 8
        nextp = 100000
    elif points < 150000:
        nextr = 9
        nextp = 150000
    elif points < 250000:
        nextr = 10
        nextp = 250000
    elif points < 500000:
        nextr = 11
        nextp = 500000
    else:
        nextr = 12
        nextp = -1

    if nextp > 0:
        ot = [nextr, nextp - points, nextp]
    else:
        ot = [12, -1, nextp]
    return ot
