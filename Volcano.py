'''
 CSCI3180 Principles of Programming Languages

 --- Declaration ---

 I declare that the assignment here submitted is original except for source
 material explicitly acknowledged. I also acknowledge that I am aware of
 University policy and regulations on honesty in academic work, and of the
 disciplinary guidelines and procedures applicable to breaches of such policy
 and regulations, as contained in the website
 http://www.cuhk.edu.hk/policy/academichonesty/

 Assignment 2
 Name : Wang Wei Xiao
 Student ID : 1155141608
 Email Addr : 1155141608@link.cuhk.edu.hk
'''
from Cell import Mountain 

class Volcano(Mountain):
    def __init__(self, row, col, freq):
        Mountain.__init__(self, row, col)
        self._countdown = freq 
        self._frequency = freq
        self._color = '\u001b[41m'
        self._active = True 

    # TODO: _active getter
    def active():
        return self._active
    
    def act(self, map):
        # TODO: reduce the countdown by 1 
        #       when the countdown is zero, refresh the countdown 
        #       get all objects occupying the neighboring cells 
        #       and update their properties accordingly 
        self._countdown -=1
        if self._countdown == 0:#condition: 
            self._countdown = self._frequency
            neighbors = map.get_neighbours(self._row,self._col)
            for i in neighbors:
                if i._occupant != None:
                    if i._occupant._name == 'Goblin':
                        i._occupant._active = False
                    elif i._occupant._name == 'Player':
                        i._occupant._hp -= 1
            print('\033[1;33;41mVolcano erupts! \033[0;0m')
            # add game logic 
        # END TODO 

    def display(self):
        # TODO: return a string representing the Volcano 
        string = ' '
        string += self._countdown()
        string += ' '
        string += self._color
        print(string,end = "")
        # END TODO 