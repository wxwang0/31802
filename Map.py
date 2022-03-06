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
from Cell import Cell

class Map:
    def __init__(self, height, width):
        self._rows = height
        self._cols = width
        self._cells = [[Cell() for x in range(width)] for y in range(height)]
    
    #TODO: rows getter
    def rows():
        return self.rows
    #TODO: cols getter
    def cols():
        return self.cols
    
    def get_cell(self, row, col):
        # TODO: check whether the position is out of boundary 
        #       if not, return the cell at (row, col)
        #       return None otherwise
        #condition:
        if  row < 0 or col <0 or row >= self._rows or col >= self._cols: 
            print('\033[1;31;46mNext move is out of boundary!\033[0;0m')
            return None 
        else:
            # return a cell
            return self._cells[row][col]
        # END TODO 

    def build_cell(self, row, col, cell):
        # TODO: check whether the position is out of boundary 
        #       if not, add a cell (row, col) and return True
        #       return False otherwise 
        if row < 0 or col <0 or row >= self._rows or col >= self._cols: 
            print('\033[1;31;46mThe position (%d, %d) is out of boundary!\033[0;0m' %(row, col))
            return False 
        else:
            # add a cell
            self._cells[row][col] = cell
            return True 
        # END TODO

    # return a list of cells which are neighbours of cell (row, col) 
    def get_neighbours(self, row, col):
        return_cells = []
        # TODO: return a list of neighboring cells of cell (row, col) 
        if row < self._rows-1:
            return_cells.append(self._cells[row+1,col])
            
        if col < self._cols-1:
            return_cells.append(self._cells[row,col+1])
            
        if row > 0:
            return_cells.append(self._cells[row-1,col])
            
        if col > 0:
            return_cells.append(self._cells[row,col-1])
            
        if col > 0 and col >0:
            return_cells.append(self._cells[row-1,col-1])
            
        if col > 0 and row < self._rows-1:
            return_cells.append(self._cells[row+1,col-1])
            
        if row > 0 and col < self._cols-1:
            return_cells.append(self._cells[row-1,col+1])
            
        if col < self._cols -1 and row < self._rows-1:
            return_cells.append(self._cells[row+1,col+1])
        
        return return_cells
        # END TODO
        

    def display(self):
        # TODO: print the map by calling diplay of each cell
        for j in range(self._cols):
            print("   ",j,end = "  ")
        print()
        for i in range(self._rows):
            print (i,end = " ")
            for j in range(self._cols):
                self._cells[i][j].display()
                print("   ",end = "")
            print()
        # END TODO
