import subprocess as sp
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
game = Game()
while game.score < 2 and game.score > -2:
    game.start()
    try:
        player = int(input('Who scored? 🤔'))
    except ValueError:
        print("Ooops! Invalid entry. ❌")
        break
    if player == 1: 
        game.home_score()
    elif player == 2:
        game.away_score()
    if game.score == 2: 
        print('Home wins! 🎉')
        break
    elif game.score == -2: 
        print('Away wins! 🎉') 
