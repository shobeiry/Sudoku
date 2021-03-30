from src.sudoku import Sudoku
import numpy as np
if __name__ == '__main__':
    s = Sudoku(25)
    print(np.array(s.new_game()))
    print(np.array(s.board))
    # s.get()
