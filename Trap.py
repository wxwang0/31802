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
# Duck Typing
class Trap:
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._occupying = None
        self._name = 'Trap'

    # TODO: _occupying get and setter
    def occupying(self):
        return self._occupying
    
    def occupying(self,cell):
        self._occupying = cell
    # TODO: _name getter
    def name(self):
        return self._name

    def interact_with(self, comer):
        # TODO: Add game logic.
        if comer._name == 'Goblin':
            print('\033[1;31;43mA goblin entered a trap at (%d, %d)and died.\033[0;0m' % (self._row, self._col))
            comer._active = False
            self._occupying.remove_occupant()
            return False
            # TODO: Add game logic.
        elif comer._name == 'Player':
            print('\033[1;31;43mYou entered a trap at (%d, %d)! HP - 1.\033[0;0m' % (self._row, self._col))
            comer._hp -=1
            comer._oxygen -=1
            self._occupying.remove_occupant()
            return True
            # TODO: Add game logic.


    def display(self):
        # TODO: Add display logic.
        string = " "
        return string
