from time import sleep
from core.game_components import Field
from core.printing import Printing
import argparse


class GameOfLife:
    def __init__(
            self,
            n_rows=8,
            n_cols=8,
            density_value=0.4,
            n_iterations=10,
            pause_len=1,
            # in python source code its a black square: https://www.fileformat.info/info/unicode/char/25a0/index.htm
            alive_cell_symbol="\u25A0",
            not_alive_cell_symbol=' ',
    ):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.pause_len = pause_len
        self.n_iterations = n_iterations
        self.alive_cell_symbol = alive_cell_symbol
        self.not_alive_cell_symbol = not_alive_cell_symbol
        self.field = Field(n_rows=n_rows, n_cols=n_cols, density_value=density_value)
        self.printer = Printing(n_cols=n_cols, col_len=3)

    def _grid_to_plot(self):
        """This function creates a matrix of symbols to print."""
        grid_to_plot = [[] for _ in range(self.n_rows)]
        for i, row in enumerate(self.field.grid):
            for cell in row:
                grid_to_plot[i].append(self.alive_cell_symbol if cell.alive else self.not_alive_cell_symbol)
        return grid_to_plot

    def print_current_state(self):
        """This function prints current state of game of life."""
        self.printer.print_messages_lines(self._grid_to_plot())

    @property
    def start_new_game(self):
        """This function starts new game of life and makes given number of iterations."""
        self.field.simulate_random_population()
        for n_iteration in range(self.n_iterations):
            if not self.field.is_state_changed:
                print('After the last iteration the state has not changed ')
                print('so the game ends. Final state of game of life:')
                self.print_current_state()
                self.field.is_state_changed = True
                return None
            print(f'ITERATION {n_iteration + 1}/{self.n_iterations}')
            self.print_current_state()
            self.field.update_current_state()
            sleep(self.pause_len)
            print("\n\n")
        print('Given number of iterations were done.')
        print('Final state of game of life:')
        self.print_current_state()


if __name__ == "__main__":
    alive_cell_symbol = "\u25A0"
    not_alive_cell_symbol = ' '
    parser = argparse.ArgumentParser(description=f'Game of life python module. In this implementation of game of life '
                                                 'we assume that the field is continuous and so it forms a torus '
                                                 'surface. So the leftmost element is connected to the rightmost '
                                                 'element of the same row and the topmost element is connected to the'
                                                 'lowers element of the same columns. Information about notations: '
                                                 f'"{alive_cell_symbol}" - is an symbol of alive cell, '
                                                 f'"{not_alive_cell_symbol}" - is an symbol of dead cell.')
    parser.add_argument('n_rows', type=int, help='Number of rows of the game field')
    parser.add_argument('n_cols', type=int, help='Number of columns of the game field')
    parser.add_argument('-density', dest="density_value", type=float, default=0.5,
                        help='Parameter which is responsible for density of default random initialization of game '
                             'field, probability of each cell to be born in random initialization')
    parser.add_argument('-n_iters', dest="n_iterations", type=int, default=10,
                        help='Number of iterations of game of life')
    parser.add_argument('-pause_len', dest="pause_len", type=float, default=1,
                        help='Length of pause in seconds between iterations of the game')
    args = parser.parse_args()
    gol = GameOfLife(
        n_rows=args.n_rows,
        n_cols=args.n_cols,
        density_value=args.density_value,
        n_iterations=args.n_iterations,
        pause_len=args.pause_len
    )
    gol.start_new_game
