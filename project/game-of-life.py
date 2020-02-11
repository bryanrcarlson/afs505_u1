from sys import argv

class Board(object):
    def __init__(self, size):
        self.nrow = size
        self.ncol = size
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
    else:
        cell = {
            "row": int(dims[0]), 
            "col": int(dims[1])
        }
        print(cell)
        return cell
            

def main(argv):
    size = int(argv[1])
    board = Board(size)
    board.BuildGrid()

    i = 2
    while i < len(argv):
        cell = ParseCellArg(argv[i])
        board.ActivateCell(cell["row"], cell["col"])
        i += 1
    
    board.PrintGrid()

if __name__ == "__main__":
    main(argv)