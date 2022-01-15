from random import random


class Cell:
    def __init__(self, alive=False):
        self.alive = alive


class Field:
    def __init__(self, n_rows=10, n_cols=10, density_value=0.5):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.density_value = density_value
        self.grid = [[Cell() for _ in range(n_cols)] for _ in range(n_rows)]
        self.is_state_changed = True

    def simulate_random_population(self):
        """"This function generates a random initialization of game field."""
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                proba = random()
                if proba < self.density_value:
                    self.grid[i][j].alive = True

    @staticmethod
    def count_n_neighbours(grid, i, j, n_rows, n_cols):
        """This function counts a number of neighbours of given cell of game field."""
        # we assume that game field is continuous and forms a torus surface
        n_neighbours = 0
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                if k == i and l == j:
                    continue
                if grid[k % n_rows][l % n_cols].alive:
                    n_neighbours += 1
        return n_neighbours

    def update_current_state(self):
        """This function updates a state of the game according to the rules of cell's survival, death and birth."""
        self.is_state_changed = True
        cells_to_update = []
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                n = self.count_n_neighbours(self.grid, i, j, self.n_rows, self.n_cols)
                if self.grid[i][j].alive and not (n == 2 or n == 3):  # cell dies if there are < 2 or > 3 neighbours
                    cells_to_update.append((i, j, False))
                if not self.grid[i][j].alive and n == 3:  # cell is born if there are exactly 3 neighbours
                    cells_to_update.append((i, j, True))
        if not cells_to_update:
            self.is_state_changed = False
        for i, j, is_alive in cells_to_update:
            self.grid[i][j].alive = is_alive
