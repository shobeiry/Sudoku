# Sudoku
 Python sudoku
 
```python
from src.sudoku import Sudoku
s = Sudoku(9) # set sudoku as 9x9 sudoku (this number must be sqrt able. like as 4, 9, 25, ...)
print(s.new_game()) # create sudoku game
print(s.board) # view game answer
```