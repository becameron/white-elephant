from entities.game import Game
from entities.person import Person
from entities.present import Present

## Game is currently in test mode
## TODO:
## set persons present to a default value
## if the person has the default value then steal fails
## make it so that a person can't steal from the same person who stole from them.

if __name__ == '__main__':
    
    todd = Person(name='Todd')
    todd_present = Present('an elephant')
    beth = Person(name='Beth')
    beth_present = Present('a trumpet')
    henry = Person(name='Henry')
    henry_present = Present('a donkey')

    game = Game()
    game.participants = [todd,beth,henry]
    game.present_pile = [todd_present,beth_present,henry_present]
    game.run(mode='test')
    # game.run()