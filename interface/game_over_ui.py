import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class GameOverUI(QMainWindow):
    def __init__(self, /, *, original_word, status):
        super().__init__()
        
        # Game name
        self.setWindowTitle('Hangman: Game Over')

        # Set window size
        self.setFixedSize(500, 700)

        # Set Icon 
        self.setWindowIcon(QIcon('./assets/images/icon/icon_logo.png'))

        # Levels styles
        self.btn_style = """font-size: 20px;
                            font-weight: bold;
                            font-family: Arial;
                            color: #333333;
                            border: 2px solid #333333;
                            border-radius: 5px;
                            background: silver;
                            padding: 10px;
                            """
        self.original_word = original_word
        self.status = status



        # Set UI
        self.setUI()
    
    def setUI(self):
        # Title
        if self.status:
            text = 'You Won'
            color = 'green'
        else:
            text = 'You Lost'
            color = 'red'

        self.title_label = QLabel(self, text=f'Game Over, {text}!')
        self.title_label.resize(500, 70)
        self.title_label.move(0, 50)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet(f"font-size: 35px; font-weight: bold; font-family: Arial; color: {color};")

        # The answer was
        self.answer_label = QLabel(self, text=f'The answer was: {self.original_word}')
        self.answer_label.resize(500, 70)
        self.answer_label.setGeometry(0, 85, 500, 70)
        self.answer_label.setAlignment(Qt.AlignCenter)
        self.answer_label.setStyleSheet("font-size: 20px; font-weight: bold; font-family: Arial; color: #333333;")

        self.secondary_label = QLabel(self, text='Would you like to play again?')
        self.secondary_label.resize(500, 70)
        self.secondary_label.move(0, 120)
        self.secondary_label.setAlignment(Qt.AlignCenter)
        self.secondary_label.setStyleSheet("font-size: 20px; font-weight: bold; font-family: Arial; color: #333333;")

        self.yes = QPushButton(self, text='Yes')
        self.yes.resize(400, 70)
        self.yes.move(50, 200)
        self.yes.setStyleSheet(self.btn_style)

        self.no = QPushButton(self, text='No')
        self.no.resize(400, 70)
        self.no.move(50, 280)
        self.no.setStyleSheet(self.btn_style)

        self.exit = QPushButton(self, text='Exit')
        self.exit.resize(400, 70)
        self.exit.move(50, 360)
        self.exit.setStyleSheet(self.btn_style)

        self.thanks = QLabel(self, text='Thanks for playing!')
        self.thanks.resize(500, 70)
        self.thanks.move(0, 500)
        self.thanks.setAlignment(Qt.AlignCenter)
        self.thanks.setStyleSheet("font-size: 20px; font-weight: bold; font-family: Arial; color: #333333;")



if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = GameOverUI()
    ui.show()
    sys.exit(app.exec_())

