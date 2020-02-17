import random

score_1 = 0
score_2 = 0
# def rand ():
#     p1_d_1 = random.randint(1, 7)
#     p1_d_2 = random.randint(1, 7)
#     return p1_d_1
#     return p1_d_2

while score_1 < 100 and score_2 < 100:
    p1_d_1 = random.randint(1, 7)
    p1_d_2 = random.randint(1, 7)
    print('player 1 turn: {} {}'.format(p1_d_1,p1_d_2))

    if p1_d_1 == 1 and p1_d_2 == 1:
        # player_1 = p1_d_1 + p1_d_2
        score_1 = 0
        print('your turn is end And your score is {}'.format(score_1))

    elif p1_d_1 == 1 or p1_d_2 == 1:
        # player_1 = p1_d_1 + p1_d_2
        score_1 = score_1 + 0
        print('Your score till this trun is {} '.format(score_1))

    else:
        player_1 = p1_d_1 + p1_d_2

        user = input('you want to hold your points press y if not then press n ').lower()
        if user == 'y':
            score_1 = score_1 + player_1
            print('Your Total score is {}'.format(score_1))
        else:
            score_1 = score_1 + 0

score_1 = score_1




