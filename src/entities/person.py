class Person:
    '''
    
    A person participating in a white elephant.
    
    '''
    def __init__(self,name):
        self.name = name
        self.holding_present = False
        self._present = None
        self.rank = None

    @property
    def present(self):
        if not self.holding_present: 
            return "doesn't have a present."
        return self._present

    @present.setter
    def present(self, present):
        self._present = present
        return self._present

    def show_present(self):
        return f'{self.name} has {self.present}'
    
    def get_present(self,present_source,mode='random'):
        '''
        
        present_source -> list

        get present from another source (person or pile).
        '''
        from random import randint

        # select present from source
        if mode == 'random':
            # randomly select present from list
            number = randint(0,(len(present_source) - 1))

            # select that present based on index number
            present = present_source[number]
            
            # remove present from pile
            present_source.remove(present)
            
            # unwrap present
            present.unwrap()

        # present is stolen
        else:

            present = present_source

            if present.steal_count == 2:

                raise ValueError(f'{present.description} has been stolen 2 times. Can\'t steal') 
            
            # increment steal count.
            present.steal_count += 1

        #assign present to the person.
        self.present = present
        self.holding_present = True

        return 

    def give_present(self):
        '''
        removes present from person if stolen by another player.
        '''
        
        self.present = "doesn't have a present."
        self.holding_present = False
    
        return
