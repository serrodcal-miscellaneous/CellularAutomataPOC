import random
from time import sleep
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt

def new_mitotic_event():
    return np.random.randint(5,11)

def set_new_mitotic_event(agenda, time, position):
    if time in agenda:
        events = agenda[time]
        events.append(position)
        agenda[time] = events
    else:
        agenda[time] = list(position)
    return agenda

class Genome:

    def __init__(self, sg, igi, ea, ag, ei, mt, tl):
        self.sg = sg
        self.igi = igi
        self.ea = ea
        self.ag = ag
        self.ei = ei
        self.mt = mt
        self.tl = tl

    def __str__(self):
        return '[' + str(self.sg) + ', ' + str(self.igi) + ', ' + str(self.ea) + ', ' + str(self.ag) + ', ' + str(self.ei) + ', ' + str(self.mt) + ', ' + str(self.tl) + ']'

    def decrease_telomer(self):
        self.tl -= 1

if __name__ == "__main__":

    #Global parameters definition and initialization
    #TODO: hacer que sea configurable por fichero, usando argparse

    sleep_time = 0.5

    time = 100
    iterations = range(time)

    grid_size = 10

    mutation_rate = 10**5 
    telomer_length = 50
    death_probability = 10
    factor_increase_base_rate_mutation = 10**2
    kill_neighbor = 30
    random_death = 10**3

    #Rename several global parameters

    m = mutation_rate
    tl = telomer_length
    e = death_probability
    i = factor_increase_base_rate_mutation
    g = kill_neighbor
    a = random_death

    #Global structures definition

    mitotics_events = dict()

    """grid = np.array([['[*, *, *, *, *, *, *]' for j in range(grid_size)] for i in range(grid_size)]) #TODO transformar la cadena por algun numero"""

    #Global structures initialization

    half_grid = int(grid_size/2)
    
    """grid[half_grid][half_grid] = str(cells[0])"""

    #First cell

    cells = {(half_grid, half_grid): [Genome(0, 0, 0, 0, 0, 0, tl)]}

    #mitotics_events structure initialization

    mitotics_events[new_mitotic_event()] = list((half_grid, half_grid))

    #Run

    for iteration in tqdm(iterations):
        if iteration in mitotics_events:
            events = mitotics_events[iteration]
            if len(events) > 0:
                #TODO: hacer iteración por eventos y ejecutar los 5 tests
                next_mitotic_event = True
                if next_mitotic_event:
                    mitotics_events = set_new_mitotic_event(mitotics_events, iteration + new_mitotic_event() , (0,0)) #TODO: La posición dependerá de cada célula
                    print(mitotics_events)
        sleep(sleep_time)

    #print(grid)
    #print(Genome(0,0,0,0,0,0,0))
    #print(new_mitotic_event())
    #print(mitotics_events)
    #print(cells)

    """Z = np.random.randint(0,2,(256,512))

    for i in range(100): 
        iterate(Z)
        size = np.array(Z.shape)
        dpi = 72.0
        figsize= size[1]/float(dpi),size[0]/float(dpi)
        fig = plt.figure(figsize=figsize, dpi=dpi, facecolor="white")
        fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)
        plt.imshow(Z,interpolation='nearest', cmap=plt.cm.gray_r)
        plt.xticks([]), plt.yticks([])
        plt.show()"""

    """grid = np.array([[1,0,0,0,0,0],[0,0,0,1,0,0],[0,1,0,1,0,0],[0,0,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])

    print(grid)

    print()

    print(count_neighbours(grid))"""


"""def apply_conway_rules(neighbours):

    new_cell = None

def count_neighbours(grid):
    N = np.zeros(grid.shape, dtype=int)
    N[1:-1,1:-1] += (grid[ :-2, :-2] + grid[ :-2,1:-1] + grid[ :-2,2:] + grid[1:-1, :-2] + grid[1:-1,2:] + grid[2: , :-2] + grid[2: ,1:-1] + grid[2: ,2:])
    return N"""

"""def iterate(Z):
    # Count neighbours
    N = (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
         Z[1:-1,0:-2]                + Z[1:-1,2:] +
         Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])

    # Apply rules
    birth = (N==3) & (Z[1:-1,1:-1]==0)
    survive = ((N==2) | (N==3)) & (Z[1:-1,1:-1]==1)
    Z[...] = 0
    Z[1:-1,1:-1][birth | survive] = 1
    return Z"""