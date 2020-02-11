from sys import argv
import copy

class Board(object):
    def __init__(self, numberRows, numberColumns):
        self.nrow = numberRows
        self.ncol = numberColumns
        self.grid = None

    def BuildGrid(self):
        newGrid = []
        for row in range(self.nrow):
            currRow = []
            for col in range(self.ncol):
                currRow.append(0)
            newGrid.append(currRow)
        
        self.grid = newGrid

    def ActivateCell(self, row, col):
        if self.grid == None:
            raise Exception("Grid not initialized")
        if((row-1 < 0 | row-1 > len(self.nrow)) | (col-1 < 0 | col-1 > len(self.nrow))):
            raise Exception("Cell is outside of bounds")
        self.grid[row-1][col-1] = 1

    def CountNeighbors(self, row, col):
        neighbors = 0
        #NW
        if((row > 0) & (col > 0)):
            if(self.grid[row-1][col-1] == 1):
                neighbors += 1
                #print(f"{row+1}:{col+1} found NW neighbor")
        
        #N
        if(row > 0):
            if(self.grid[row-1][col] == 1):
                neighbors += 1
                #print(f"{row+1}:{col+1} found N neighbor")

        #NE
        if((row > 0) & (col < (self.ncol-1))):
            if(self.grid[row-1][col+1] == 1):
                neighbors += 1
                #print(f"{row+1}:{col+1} found NE neighbor")
        
        #E
        if(col < (self.ncol-1)):
            if(self.grid[row][col+1] == 1):
                neighbors += 1
                #print(f"{row+1}:{col+1} found E neighbor")

        #SE
        if((row < (self.nrow-1)) & (col < (self.ncol-1))):
            if(self.grid[row+1][col+1] == 1):
                neighbors += 1
                #print(f"{row+1}:{col+1} found SE neighbor")
        
        #S
        if(row < (self.nrow-1)):
            if(self.grid[row+1][col] == 1):
                neighbors += 1
                #print(f"{row+1}:{col+1} found S neighbor")

        #SW
        if((row < (self.nrow-1)) & (col > 0)):
            if(self.grid[row+1][col-1] == 1):
                neighbors += 1
                #print(f"{row+1}:{col+1} found SW neighbor")

        #W
        if(col > 0):
            if(self.grid[row][col-1] == 1):
                neighbors += 1
                #print(f"{row+1}:{col+1} found W neighbor")

        return neighbors

    def SwitchCell(self, row, col, neighbors, nextGrid):
        if(self.grid[row][col] == 0):
            if(neighbors == 3):
                nextGrid[row][col] = 1
        else:
            if(neighbors < 2):
                nextGrid[row][col] = 0
            elif(neighbors > 3):
                nextGrid[row][col] = 0

    def Step(self):
        #nextGrid = self.grid[:]
        #nextGrid = self.grid.copy()
        nextGrid = copy.deepcopy(self.grid)

        for row in range(self.nrow):
            for col in range(self.ncol):
                neighbors = self.CountNeighbors(row, col)
                self.SwitchCell(row, col, neighbors, nextGrid)
        self.grid = copy.deepcopy(nextGrid)
        self.PrintGrid()

    def PrintGrid(self):
        if self.grid == None:
            raise Exception("Grid not initialized")
        for row in self.grid:
            for cell in row:
                if cell == 0:
                    print("-", end="")
                else:
                    print("*", end = "")
            print("\n", end = "")

def ParseCellArg(cellStr):
    dims = cellStr.split(":")
    if(len(dims) != 2):
        raise Exception("Error parsing cell")

    cell = {
        "row": int(dims[0]), 
        "col": int(dims[1])
    }

    return cell
            
def main(argv):
    # Build the board and grid
    ticks = int(argv[1])
    board = Board(30, 80)
    board.BuildGrid()

    # Set initial conditions
    i = 2
    while i < len(argv):
        cell = ParseCellArg(argv[i])
        board.ActivateCell(cell["row"], cell["col"])
        i += 1
    board.PrintGrid()

    stepCount = 0
    while(stepCount < ticks):
        board.Step()
        stepCount += 1

if __name__ == "__main__":
    main(argv)