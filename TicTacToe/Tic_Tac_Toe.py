import os

class Grid:
    def __init__(self):
        self.__grid = [["_" for _ in range(3)] for _ in range(3)]

    def display_the_grid(self):
        os.system('cls')
        for row in self.__grid:
            print(row)

    def mark(self, player):
        row = int(input("row = "))
        column = int(input("column = "))

        self.__grid[row][column] = player.draw()

    def is_draw(self):
        if all("_" not in item for item in self.__grid):
            return "Draw"
        return False
    
    def player_won(self):
        if self._diagonal_win() or self._horizontal_win() or self._vertical_win():
            return "Win"
        return False


    def _diagonal_win(self):
        tmp = set()
        for i in range(len(self.__grid)):
            if self.__grid[i][i] == "_":
                return False
            tmp.add(self.__grid[i][i])
        if len(tmp) == 1:
            return True
        
        tmp = set()
        for i in range(len(self.__grid)):
            if self.__grid[i][len(self.__grid) - 1 - i] == "_":
                return False
            tmp.add(self.__grid[i][len(self.__grid) - 1 - i])
        if len(tmp) == 1:
            return True
            
        return False

    def _horizontal_win(self):
        for di in self.__grid:
            if len(set(di)) == 1 and "_" not in set(di):
                return True
        return False

    def _vertical_win(self):
        for col in range(len(self.__grid)):
            temp = set()
            for row in range(len(self.__grid)):
                temp.add(self.__grid[row][col])
            if len(temp) == 1 and "_" not in temp:
                return True
        return False

class X_Gamer:
    def __init__(self):
        self.name = input("Enter your name p1: ") 
        self.__marking = "X"
        self.next = None

    def draw(self):
        return self.__marking
    
class O_Gamer:
    def __init__(self):
        self.name = input("Enter your name p2: ")
        self.__marking = "O"
        self._next = None

    def draw(self):
        return self.__marking
    
class Start:
    def __init__(self):
        self.player1 = X_Gamer()
        self.player2 = O_Gamer()
        
        self.player1._next = self.player2
        self.player2._next = self.player1

        self.grid = Grid()    

    def start_the_game(self):
        self.__turn = self.player1
        while True:
            self.grid.display_the_grid()
            self.grid.mark(self.__turn)
            if result := self.grid.player_won() or self.grid.is_draw():
                break
            self.__turn = self.__turn._next
        
        self.display_the_result(result)
        
    def display_the_result(self, result):
        os.system('cls')

        if result == "Draw":
            print("Draw")
        elif result == "Win":
            print(f"The player {self.__turn.name} won")
            




game = Start()
game.start_the_game()