class Present:
    '''
    A present designed to be held and stolen :)
    '''
    def __init__(self,description,status='wrapped!'):
        self.status =  status
        self.steal_count = 0
        self._description = description

    def __repr__(self):
        return  f'{self.description}'

    @property
    def description(self):
        if self.status == 'wrapped!': 
            return 'wrapped!'
        return self._description

    @description.setter
    def description(self, description):
        self._description = description
        return self._description

    def unwrap(self):
        '''
        present unwarps when removed from game pile.
        '''
        if self.status == 'wrapped!':
            self.status = 'unwrapped'
            return self.__repr__()

        else:
            print('This present is already unwrapped!\n')
            return self.__repr__()