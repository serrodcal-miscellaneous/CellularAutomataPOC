import random
from time import sleep
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt

def new_mitotic_event():
    return np.random.randint(5,11)

#TODO: Refactorizar con lo que hay en el buble de ejecución
"""def set_new_mitotic_event(agenda, time, position):
    if time in agenda:
        events = agenda[time]
        events.append(position)
        agenda[time] = events
    else:
        agenda[time] = list(position)
    return agenda"""

def check_full_neighborhood(cell, cells): #TODO: comprobar el grid para ver si el vecindario tiene espacio
    return True

def kill_cell(tests_result, cells, cell):
    return False

def apply_mitotic(mitotic_candidate_cell, cells):
    return False

#Tests: Salvo excepcion, se devuelve 1 cuando hay mitosis, y 0 cuando aplica la muerte.

def test_1(cell, a):
    if np.random.randint(0, a) < 1/a:
        return 0
    return 1

def test_2(cell, e, cells): #Si no esta activo EA y aplica la muerte, devuelve 0. En otro caso, devolve 1.
    if cell in cells:
        cell_genome = cells[cell]
        n = cell_genome.mutations()
        if not cell_genome.ea:
            if np.random.randint(0,n) < n/e:
                return 0
    return 1

def test_3(cell): 
    #TODO: Hay que buscar en el articulo que procedimiento sigue este test.
    return 1

def test_4(cell, cells):
    full = check_full_neighborhood(cell, cells)
    if full and cell.igi and np.random.random(0, g) < 1/g:
        return 1
    return 0

def test_5(cell): 
    if cell.tl == 0 and cell.ei:
        return 1
    return 0

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

    def mutations(sefl):
        count = 0
        if self.sg:
            count += 1
        if self.igi:
            count += 1
        if self.ea:
            count += 1
        if self.ag:
            count += 1
        if self.ei:
            count += 1
        if self.mt:
            count += 1
        return count

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

    """grid = np.array([['[*, *, *, *, *, *, *]' for j in range(grid_size)] for i in range(grid_size)]) #TODO transformar la cadena por algun numero"""

    #Global structures initialization

    half_grid = int(grid_size/2)

    """grid[half_grid][half_grid] = str(cells[0])"""

    #First cell

    first_cell_position = (half_grid, half_grid)

    cells = {first_cell_position: Genome(0, 0, 0, 0, 0, 0, tl)}

    #mitotics_events structure initialization

    mitotics_events = {new_mitotic_event(): [first_cell_position]}

    #Run

    for iteration in tqdm(iterations):
        if iteration in mitotics_events:
            events = mitotics_events[iteration]
            del mitotics_events[iteration]
            for event in events:
                print(events)
                if event in cells:
                    mitotic_candidate_cell = cells[event]
                    tests_result = test_1(mitotic_candidate_cell, a)
                    tests_result += test_2(mitotic_candidate_cell, e, cells)
                    tests_result += test_3(mitotic_candidate_cell,) #Ver TODO en funcion.
                    tests_result += test_4(mitotic_candidate_cell, cells)
                    tests_result += test_5(mitotic_candidate_cell)
                    if kill_cell(tests_result, cells, mitotic_candidate_cell):
                        print("Cell death event succeded!")
                    elif apply_mitotic(mitotic_candidate_cell, mitotic_candidate_cell):
                        print("Mitotic event succeded!")
                    else: #Programar nuevo evento mitotico
                        print("New event succeded!")
                        new_event_time = new_mitotic_event() + iteration
                        print("New event time: " + str(new_event_time) + ", at: " + str(event))
                        if new_event_time in mitotics_events:
                            events_aux = mitotics_events[new_event_time]
                            events_aux.append(event)
                            mitotics_events[new_event_time] = events_aux
                        else:
                            mitotics_events.update({new_event_time: [event]})
        sleep(sleep_time)

