import os
import Gamer
import Table

class MainGame:
    def __init__(self):
        
        self.player1 = Gamer.Gamers("X")
        self.player2 = Gamer.Gamers("O")
        self.table = Table.Grid()    

        self.current = self.player1
        self.counter = 0

    def display_the_grid(self):
        os.system('cls')
        for row in self.table.grid:
            print(row)

    def marking(self, row, column):
        if self.counter % 2 == 0:
            self.current = self.player1
            self.mark = self.player1._mark
        else:
            self.current = self.player2
            self.mark = self.player2._mark

        self.table.grid[row][column] = self.mark
        self.counter += 1

        self.display_the_grid()

        return self.mark

    def is_draw(self):
        if all("_" not in item for item in self.table.grid):
            return "Draw"
        return False
    
    def player_won(self):
        if self._diagonal_win() or self._horizontal_win() or self._vertical_win():
            return "Win"
        return False


    def _diagonal_win(self):
        tmp = set()
        for i in range(len(self.table.grid)):
            if self.table.grid[i][i] == "_":
                return False
            tmp.add(self.table.grid[i][i])
        if len(tmp) == 1:
            return True
        
        tmp = set()
        for i in range(len(self.table.grid)):
            if self.table.grid[i][len(self.table.grid) - 1 - i] == "_":
                return False
            tmp.add(self.table.grid[i][len(self.table.grid) - 1 - i])
        if len(tmp) == 1:
            return True
            
        return False

    def _horizontal_win(self):
        for di in self.table.grid:
            if len(set(di)) == 1 and "_" not in set(di):
                return True
        return False

    def _vertical_win(self):
        for col in range(len(self.table.grid)):
            temp = set()
            for row in range(len(self.table.grid)):
                temp.add(self.table.grid[row][col])
            if len(temp) == 1 and "_" not in temp:
                return True
        return False
    
    def new_game(self):
        self.current = self.player1
        self.counter = 0
        print("I maybe was called")
        for i in range(len(self.table.grid)):
            for j in range(len(self.table.grid)):
                self.table.grid[i][j] = "_"
        self.display_the_grid()
