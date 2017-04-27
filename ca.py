import numpy as np

def count_neighbours(grid):
    N = np.zeros(grid.shape, dtype=int)
    N[1:-1,1:-1] += (grid[ :-2, :-2] + grid[ :-2,1:-1] + grid[ :-2,2:] + grid[1:-1, :-2] + grid[1:-1,2:] + grid[2: , :-2] + grid[2: ,1:-1] + grid[2: ,2:])
    return N

if __name__ == "__main__":
    grid = np.array([[0,0,0,0,0,0],[0,0,0,1,0,0],[0,1,0,1,0,0],[0,0,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])

    print(grid)

    print()

    print(count_neighbours(grid))

