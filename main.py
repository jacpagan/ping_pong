import subprocess as sp
class Player(): 
    def __init__(self):
        self.score = 0
        self.name = str(input("What's your name?"))


class Game(): 
    def __init__(self): 
        self.score = 0

    def home_score(self):
        self.score += 1

    def away_score(self): 
        self.score -= 1

    def start(self): 
        if self.score == 0:
            print('🏓 Evens 🏓')
            return 
        print('{} advantage'.format('Home 🏠' if self.score > 0 else 'Away 💨'))

sp.call('clear',shell=True)
play = True
player1 = Player()
player2 = Player()
while play: 
    game = Game()
    while game.score < 2 and game.score > -2:
        game.start()
        winner = str(input('Who scored? 🤔'))
        if winner == 1 or winner == player1.name: 
            game.home_score()
            print(player1.name, " scores!") 
        elif winner == 2 or winner == player2.name:
            game.away_score()
            print(player2.name, " scores!")
        if game.score == 2: 
            print('{} wins! 🎉'.format(player1.name))
            player1.score += 1
        elif game.score == -2: 
            print('{} wins! 🎉'.format(player2.name))
            player2.score += 1

    print("Overall scores: ")
    print("{}: {}".format(player1.name, player1.score))
    print("{}: {}".format(player2.name, player2.score))
    again = str(input("Do you want to play again? Type yes or no."))
    if again == "no":
        play = False
