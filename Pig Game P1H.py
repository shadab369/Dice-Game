import random

player1 = input('Enter The Name : ')

score_1 = 0
score_2 = 0

def Player():

    global score_1

    input('Press Enter To Roll The Dice {}'.format(player1))

    while score_1 < 100 and score_2 < 100:

        p1_d1 = random.randint(1,6)

        p1_d2 = random.randint(1,6)

        print('Your Turn: {} {}'.format(p1_d1,p1_d2))

        if p1_d1 == 1 and p1_d2 == 1:
            score_1 = 0
            print('{} Your Turn Is End And Your Score Is {}'.format(player1,score_1))
            Computer()

        elif p1_d1 == 1 or p1_d2 == 1:
            score_1 = score_1 + 0
            print('{} Your Score Till This Trun Is {} '.format(player1,score_1))
            Computer()
        else:
            p1 = p1_d1 + p1_d2
            user = input('{} You Want To Hold Your Points Press y If Not Then Press n '.format(player1)).lower()

            if user == 'y':
                score_1 = score_1 + p1
                print('{} Your Total score is {}'.format(player1,score_1))

                if score_1 >= 100:
                     print('Congratulation! {} You Won The Game.'.format(player1))
            else:
                score_1 = score_1 + 0
    score_1 = score_1


def Computer():

    global score_2

    # input('Press Enter To Roll The Dice {}'.format(player1))

    while score_1 < 100 and score_2 < 100:

        com_d1 = random.randint(1, 6)

        com_d2 = random.randint(1, 6)

        print('Computer  Turn: {} {}'.format(com_d1, com_d2))

        if com_d1 == 1 and com_d2 == 1:
            score_2 = 0
            print('Computer Turn Is End And Your Score Is {}'.format(score_2))
            Player()

        elif com_d1 == 1 or com_d2 == 1:
            score_2 = score_2 + 0
            print('Computer Score Till This Trun Is {} '.format(score_2))
            Player()
        else:
            com = com_d1 + com_d2
            score_2= score_2 + com
            print('Computer Total score is {}'.format(score_2))

            if score_2 >= 100:
                print('Congratulation! Computer You Won The Game.')

    score_2 = score_2

Player()
