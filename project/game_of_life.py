"""Script to run Conway's Game of Life

.. module:: game_of_life
    :synopsis: project assignment for WSU AFS505 unit 1

.. moduleauthor:: Bryan Carlson
"""

from sys import argv
import copy

class GameOfLife(object):
    """Class to represent Conway's Game of Life
    
    :param nrow: The number of rows in the grid
    :type nrow: int
    :param ncol: The number of columns in the grid
    :type ncol: int
    :param grid: A 2-d grid of cells that are either active (true) or inactive (false)
    :type grid: 2-d list of booleans        
    """

    def __init__(self, number_rows, number_columns):
        """Constructor method
        """
        self.nrow = number_rows
        self.ncol = number_columns
        self.grid = None

    def build_grid(self):
        """initializes the grid using nrow and ncol attributes
        """

        newGrid = []
        for row in range(self.nrow):
            currRow = []
            for col in range(self.ncol):
                currRow.append(False)
            newGrid.append(currRow)
        
        self.grid = newGrid

    def activate_cell(self, row, col):
        """sets value in grid[row-1][int-1] to True

        :param row: row number of cell to activate, 1-nrow
        :type row: int
        :param col: col number of cell to activate, 1-ncol
        :type col: int
        """

        if self.grid == None:
            raise Exception("Grid not initialized")
        if((row-1 < 0 | row-1 > len(self.nrow)) | (col-1 < 0 | col-1 > len(self.nrow))):
            raise Exception("Cell is outside of bounds")
        self.grid[row-1][col-1] = True

    def count_neighbors(self, row, col):
        """returns integer value (0-8) for number of active cells adjacent to cell specified in arguments row,col

        :param row: row number of cell for which neighbors are counted, 1-nrow
        :type row: int
        :param col: col number of cell for which neighbors are counted, 1-ncol
        :type col: int
        :return: An int count of the number of active neighbors to given cell (0-8)
        """

        neighbors = 0
        #NW
        if((row > 0) & (col > 0)):
            if(self.grid[row-1][col-1] == True):
                neighbors += 1
        
        #N
        if(row > 0):
            if(self.grid[row-1][col] == True):
                neighbors += 1

        #NE
        if((row > 0) & (col < (self.ncol-1))):
            if(self.grid[row-1][col+1] == True):
                neighbors += 1
        
        #E
        if(col < (self.ncol-1)):
            if(self.grid[row][col+1] == True):
                neighbors += 1

        #SE
        if((row < (self.nrow-1)) & (col < (self.ncol-1))):
            if(self.grid[row+1][col+1] == True):
                neighbors += 1
        
        #S
        if(row < (self.nrow-1)):
            if(self.grid[row+1][col] == True):
                neighbors += 1

        #SW
        if((row < (self.nrow-1)) & (col > 0)):
            if(self.grid[row+1][col-1] == True):
                neighbors += 1

        #W
        if(col > 0):
            if(self.grid[row][col-1] == True):
                neighbors += 1

        return neighbors

    def switch_cell(self, row, col, neighbors, nextGrid):
        """follows conways game of life logic to activate/deactivate a cell in nextGrid based on number of neighbors

        :param row: row number of cell to switch, 1-nrow
        :type row: int
        :param col: col number of cell to switch, 1-ncol
        :type col: int
        :param neighbors: number of active neighbors that cell has
        :type neighbors: int
        :param nextGrid: represents the grid of the future timestep, changes to cell activation are made to this
        :type nextGrid: 2-d list of booleans
        """

        if(self.grid[row][col] == False):
            if(neighbors == 3):
                nextGrid[row][col] = True
        else:
            if(neighbors < 2):
                nextGrid[row][col] = False
            elif(neighbors > 3):
                nextGrid[row][col] = False

    def step(self):
        """moves the simulation forward a single tick by updating all cells in the grid and prints the updated grid
        """

        nextGrid = copy.deepcopy(self.grid)

        for row in range(self.nrow):
            for col in range(self.ncol):
                neighbors = self.count_neighbors(row, col)
                self.switch_cell(row, col, neighbors, nextGrid)
        self.grid = copy.deepcopy(nextGrid)
        self.print_grid()

    def print_grid(self):
        """prints the grid to stdout representing active cells as "*" and inactive as "-"
        """

        if self.grid == None:
            raise Exception("Grid not initialized")
        for row in self.grid:
            for cell in row:
                if cell:
                    print("*", end = "")
                else:
                    print("-", end="")
                    
            print("\n", end = "")

def parse_cell_arg(cellStr):
    """Takes a string in "#:#" format and converts it to a dictionary

    :return: A dictionary of {"row":int, "col":int} where row is number to left of ":" and col is number to right of ":" in cellStr
    """

    dims = cellStr.split(":")
    if(len(dims) != 2):
        raise Exception("Error parsing cell")

    cell = {
        "row": int(dims[0]), 
        "col": int(dims[1])
    }

    return cell
            
def main(argv):
    """Composition root to handle command line arguments and initialize classes

    :param argv: list of strings following call to script. argv[1] is assumed to be number of steps/ticks taken followed by 0-many strings to specify active cells in format #:# (e.g. 1:1 will activate the top-left cell of the grid)
    :type argv: list of strings
    """

    GRID_HEIGHT = 30
    GRID_WIDTH = 80

    # Build the board and grid
    ticks = int(argv[1])
    board = GameOfLife(GRID_HEIGHT, GRID_WIDTH)
    board.build_grid()

    # Set initial conditions
    i = 2
    while i < len(argv):
        cell = parse_cell_arg(argv[i])
        board.activate_cell(cell["row"], cell["col"])
        i += 1
    board.print_grid()

    stepCount = 0
    while(stepCount < ticks):
        board.step()
        stepCount += 1

if __name__ == "__main__":
    main(argv)