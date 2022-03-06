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
from Map import Map
from Cell import Plain, Mountain, Swamp
from GameCharacter import Player, Goblin

class Engine:
    def __init__(self, data_file):
        self._actors = []
        self._map = None 
        self._player = None 
        with open(data_file, 'r') as fp:
            line = fp.readline()
            if not line:
                return None 
            else:
                items = line.split()
                if len(items) != 5:
                    print('INVALID DATA FILE.')
                    return None 
                num_of_row = int(items[0])
                num_of_col = int(items[1])
                p_ox = int(items[2])
                p_hp = int(items[3])
                num_of_goblins = int(items[4])

            self._map = Map(num_of_row, num_of_col)
            
            # TODO: initialize each cell of the map object 
            #       using the build_cell method 
            for i in range(num_of_row):
                line = fp.readline()
                if not line:
                    return None
                else:
                    items = line.split()
                    if len(items) != num_of_col:
                       print('INVALID DATA FILE.')
                       return None
                    for j in range(num_of_col):
                        if items[j] == 'P':
                            self._map.build_cell(i,j,Plain(i,j)) 
                        elif items[j] == 'M':
                            self._map.build_cell(i,j,Mountain(i,j))
                        elif items[j] == 'S':
                            self._map.build_cell(i,j,Swamp(i,j))
            # END TODO
           
            self._player = Player(num_of_row - 1, 0, p_hp, p_ox)
            # TODO: initilize the position of the player 
            #       using the set_occupant and occupying setter;
            #       add the player to _actors array
            cell = self._map.get_cell(num_of_row - 1, 0)
            cell.set_occupant(self._player)
            self._player.occupying(cell)
            self._actors.append(self._player)
            # END TODO 


            for gno in range(num_of_goblins):
                # TODO: initilize each Goblin on the map
                #       using the set_occupant and occupying setter;
                #       add each Goblin to _actors array
                line = fp.readline()
                if not line:
                    return None
                else:
                    items = line.split()
                    length = len(items)
                    actions = []
                    for i in range(2, length):
                        actions.append(items[i])
                    new_goblin = Goblin(int(items[0]),int(items[1]),actions)
                cell = self._map.get_cell(int(items[0]),int(items[1]))
                cell.set_occupant(new_goblin)
                new_goblin.occupying(cell)
                self._actors.append(new_goblin)
                # END TOD

    def run(self):
        # main rountine of the game
        self.print_info()
        while not self.state():            
            for obj in self._actors:
                if obj._active: 
                    obj.act(self._map)
            self.print_info()
            self.clean_up()
        self.print_result()

    def clean_up(self):
        # TODO: remove all objects in _actors which is not active 
        for i in self._actors:
            if i._active != True:
                self._actors.remove(i)
        # END TODO

    # check if the game ends and return if the player win or not.
    def state(self):
         # TODO: check if the game ends and 
        #       return an integer for the game status
        if self._player._hp * self._player._oxygen <= 0:
            return -1
        elif self._player._row == 0 and self._player._col == self._map._cols-1:
            return 1
        else:
            return 0
        # END TODO 
        
    def print_info(self):
        self._map.display()
        # TODO: display the remaining oxygen and HP 
        print("Oxygen: %d, HP: %d." %(self._player._oxygen,self._player._hp))
        # END TODO
        
    def print_result(self):
        # TODO: print a string that shows the result of the game. 
        if self.state() == 1:
            print("Congrats! You win!")
        if self.state() == -1:
            print("Bad Luck! You lose.")
        # END TODO

        
