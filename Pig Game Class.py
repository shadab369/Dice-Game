import random


# def rand ():
#     p1_d_1 = random.randint(1, 7)
#     p1_d_2 = random.randint(1, 7)
#     return p1_d_1
#     return p1_d_2
class Piggame:

    def __init__(self):

        self.p1 = input('Player1 Enter The Name : ').capitalize()
        self.p2 = input('Player2 Enter The Name : ').capitalize()
        self.score_1 = 0
        self.score_2 = 0

    def player1(self):


        self.score_1
        input('{} Press Enter To Roll The Dice.'.format(self.p1))

        while self.score_1 < 100 and self.score_2 < 100:

            p1_d_1 = random.randint(1, 6)
            p1_d_2 = random.randint(1, 6)
            print('{} Your Turn: {} {}'.format(self.p1,p1_d_1,p1_d_2))

            if p1_d_1 == 1 and p1_d_2 == 1:
                self.score_1 = 0
                print('{} Your Turn Is End And Your Score Is {}'.format(self.p1,self.score_1))
                p1.player2()

            elif p1_d_1 == 1 or p1_d_2 == 1:
                self.score_1 = self.score_1 + 0
                print('{} Your Score Till This Trun Is {} '.format(self.p1,self.score_1))
                p1.player2()

            else:
                player_1 = p1_d_1 + p1_d_2

                user = input('You Want To Hold Your Points Press y If Not Then Press n ').lower()
                if user == 'y':
                    self.score_1 = self.score_1 + player_1

                    # if score_1 >= 100:
                    #     print('{} Your Total score is {}'.format(p1, 100))
                    print('{} Your Total score is {}'.format(self.p1, self.score_1))
                    if self.score_1 >=100:
                        print('Congratulation! {} You Won The Game.'.format(self.p1))
                else:
                    self.score_1 = self.score_1 + 0


        self.score_1 = self.score_1




    def player2(self):

        self.score_2
        input('{} Press Enter To Roll The Dice.'.format(self.p2))

        while self.score_1 < 100 and self.score_2 < 100:

            p2_d_1 = random.randint(1, 6)
            p2_d_2 = random.randint(1, 6)
            print('{} Your Turn: {} {}'.format(self.p2, p2_d_1, p2_d_2))

            if p2_d_1 == 1 and p2_d_2 == 1:
                self.score_2 = 0
                print('{} Your Turn Is End And Your Score Is {}'.format(self.p2, self.score_2))
                p1.player1()

            elif p2_d_1 == 1 or p2_d_2 == 1:
                self.score_2 = self.score_2 + 0
                print('{} Your Score Till This Trun Is {} '.format(self.p2,self.score_2))
                p1.player1()

            else:
                player_2 = p2_d_1 + p2_d_2

                user = input('You Want To Hold Your Points Press y If Not Then Press n ').lower()
                if user == 'y':
                    self.score_2 = self.score_2 + player_2
                    # if score_2 >=100:
                    #     print('{} Your Total score is {}'.format(p2, 100))
                    print('{} Your Total score is {}'.format(self.p2, self.score_2))
                    if self.score_2 >=100:
                        print('Congratulation! {} You Won The Game.'.format(self.p2))
                else:
                    self.score_2 = self.score_2 + 0

        self.score_2 = self.score_2


p1 = Piggame()
p1.player2()
