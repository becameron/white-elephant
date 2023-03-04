from .person import Person
from .present import Present
import sys
import time
import os

class Game:
    '''
    white elephant game. Rules can be found here: https://en.wikipedia.org/wiki/White_elephant_gift_exchange
    '''
    def __init__(self):
        self.participants = []
        self.present_pile = []
        self.choices = {
                        '1':self.pick_present,
                        '2':self.steal_present,
                        '3':self.display_unwrapped,
                        }
        self.choice_desc = f'Select and option:\n'\
                            f'1: Take present from pile.\n'\
                            f'2: Steal present.\n'\
                            f'3: Display unwrapped presents.\n'

    def run(self,mode='game'):

        if mode != 'test':
            # asks for participants and their presents
            self.start_game()

        # ranks the participants randomly
        self.turn_order()

        # presents each person with their choices
        # for their turn
        for participant in self.participants:            
                self.menu_options(participant)



    def start_game(self):
        # move to attribute
        num_players = int(input('how many people are playing?\n'))

        for i in range(1,num_players + 1):
            player = input("enter player's name:\n")
            present = input("enter player's present description:\n")

            self.participants.append(Person(player))
            self.present_pile.append(Present(present))

            print(  f'\n{player} entered with present {present}.\n')
            time.sleep(1)
            self.clear_terminal()
            print(  f'{i} of {num_players} players entered.\n')

    def turn_order(self):
        from random import choice

        rank_list = [i for i in range(1,len(self.participants) + 1)]

        for participant in self.participants:
            rank = choice(rank_list)
            participant.rank = rank
            rank_list.remove(rank)

        self.participants.sort(key=lambda x: x.rank)

        # prints the order of turns.
        print('\nPeople will choose presents in the following order:')

        for participant in self.participants:
            print(f'{participant.rank}. {participant.name}')
        print('\n')

        return

    def menu_options(self,participant):
        
        # cycles person through the options 
        # until they obtain a present.

        while True:
            print(
                    f'\n{participant.name}\n'\
                    f'{self.choice_desc}'
                    )

            selection = input('')
            print('\n')

            func = self.choices[selection]

            func(participant)
            
            # loop breaks once person has seleccted a present.
            if participant.present != "doesn't have a present.":
                time.sleep(2)
                self.clear_terminal()
                break
            
        return 

    def pick_present(self,person):

        person.get_present(self.present_pile)

        return print(f'{person.name} unwrapped {person.present}!')

    def steal_present(self,person): 

        # show all participants presents
        self.display_unwrapped()
        
        ans = input('which person would you like to steal from?\n')
        print('\n')

        # loop through participants to see if the player
        # gave a valid entry
        for other in self.participants:
            if other.name.lower() == ans.lower():
                ## try to steal present.
                try:

                    person.get_present(other.present,mode='steal')
                
                except ValueError:

                    print(f'Present has already been stolen twice, please select another person.')
                    
                    # allow person to retry to steal from someone else.
                    return self.steal_present(person)

                # other player gives up present
                other.give_present()

                print(f'{person.name} stole {person.present} from {other.name}!')
                print(f'{other.name} can now select a gift')

                # allow person stolen from to have another turn.
                self.menu_options(other)

                return 

        # will exit back to menu options if no valid input is provided.    
        return 

    def display_unwrapped(self,*args):
        for participant in self.participants:
            print(participant.show_present())
        print('\n')

    @staticmethod
    def clear_terminal():
        os.system('cls||clear')

    def quit(self):
        print('game over.')
        del self


