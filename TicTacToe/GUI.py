from PyQt6.QtWidgets import QMainWindow 
from PyQt6 import uic
from Game import MainGame

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Gui.ui', self)
        self.game = MainGame()

        self.buttons = [ self.button_00, self.button_01, self.button_02, self.button_10, self.button_11, self.button_12, self.button_20, self.button_21, self.button_22]
        self.label.setText(f"{self.game.current._name} - {self.game.current._mark}")

        self.button_00.clicked.connect(lambda: self.take_marking(self.button_00))
        self.button_01.clicked.connect(lambda: self.take_marking(self.button_01))
        self.button_02.clicked.connect(lambda: self.take_marking(self.button_02))
        self.button_10.clicked.connect(lambda: self.take_marking(self.button_10))
        self.button_11.clicked.connect(lambda: self.take_marking(self.button_11))
        self.button_12.clicked.connect(lambda: self.take_marking(self.button_12))
        self.button_20.clicked.connect(lambda: self.take_marking(self.button_20))
        self.button_21.clicked.connect(lambda: self.take_marking(self.button_21))
        self.button_22.clicked.connect(lambda: self.take_marking(self.button_22))

        self.NewGameButton.clicked.connect(self.new_game)

        self.QuitButton.clicked.connect(self.end_game)

    def take_marking(self, button):
        self.label.setText(f"{self.game.current._name} - {self.game.current._mark}")
        button.setText(self.game.marking(int(button.objectName()[-2]), int(button.objectName()[-1])))
        button.setEnabled(False)
        if result := self.game.is_draw() or self.game.player_won():
            self.stop_game()
            self.display_result(result)


    def stop_game(self):
        for b in self.buttons:
            b.setDisabled(True)

    def display_result(self, message):
        if message == "Win":
            self.label.setText(f"{self.game.current._name} won!")
        else:
            self.label.setText("Draw!")

    def new_game(self):
        print("I was called")
        self.game.new_game()
        for b in self.buttons:
            b.setText("")
            b.setEnabled(True)
        self.label.setText(f"{self.game.current._name} - {self.game.current._mark}")

    def end_game(self):
        self.close()




