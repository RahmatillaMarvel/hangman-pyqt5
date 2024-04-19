import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap

class GameUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Game name
        self.setWindowTitle('Hangman')

        # Set window size
        self.setFixedSize(1000, 700)

        # Set Icon 
        self.setWindowIcon(QIcon('./assets/images/icon/icon_logo.png'))

        # Set background color
        self.setStyleSheet("background-color: #fff;")

        # Set UI
        self.setUI()
    
    def setUI(self):
        # Title
        self.game_title = QLabel(self, text='Hangman')
        self.game_title.resize(1000, 70)
        self.game_title.move(0, 20)
        self.game_title.setAlignment(Qt.AlignCenter)
        self.game_title.setStyleSheet("font-size: 35px; font-weight: bold; font-family: Arial; color: #333333;")

        self.draw_gallow()
        self.hint1()
        self.hint1_display_label()
        self.hint2()
        self.hint2_display_label()
        self.hint3()
        self.hint3_display_label()
        

    def display_definition(self, definition):
        self.definition_label = QLabel(self, text = definition)
        self.definition_label.setGeometry(550, 120, 400, 100)
        self.definition_label.setWordWrap(True)
        self.definition_label.setStyleSheet("font-size: 18px; font-weight: bold; font-family: Arial; color: #333333;")
    def generate_blanks(self, count):
        self.word_place = ['_'] * count
        self.blank_label = QLabel(self, text='  '.join(self.word_place))
        self.blank_label.resize(600, 70)
        self.blank_label.move(400, 300)
        self.blank_label.setAlignment(Qt.AlignCenter)
        self.blank_label.setStyleSheet("font-size: 35px; font-weight: bold; font-family: Arial; color: #333333;")
        
    def draw_gallow(self):
        gallow = QPixmap('./assets/images/hangman.png')
        self.gallow = QLabel(self)
        self.gallow.setPixmap(gallow)
        self.gallow.setScaledContents(True)
        self.gallow.setGeometry(0, 150, 400, 500)
        self.cover_head()
        self.cover_body()
        self.cover_left_hand()
        self.cover_right_hand()
        self.cover_left_leg()
        self.cover_right_leg()

        self.body_parts = [self.blank_cover, self.body_cover, self.left_hand_cover, self.right_hand_cover, self.left_leg_cover, self.right_leg_cover]

    
    def cover_head(self):
        self.blank_cover = QLabel(self)
        self.blank_cover.setGeometry(240, 270, 160, 150)
        self.blank_cover.setStyleSheet("background-color: white; border: ")
    
    def cover_body(self):
        self.body_cover = QLabel(self)
        self.body_cover.setGeometry(240, 420, 160, 250)
        self.body_cover.setStyleSheet("background-color: white; border: ")

    def cover_left_hand(self):
        self.left_hand_cover = QLabel(self)
        self.left_hand_cover.setGeometry(240, 420, 69, 70)
        self.left_hand_cover.setStyleSheet("background-color: white")
    
    def cover_right_hand(self):
        self.right_hand_cover = QLabel(self)
        self.right_hand_cover.setGeometry(325, 420, 75, 70)
        self.right_hand_cover.setStyleSheet("background-color: white;")
    
    
    def cover_left_leg(self):
        self.left_leg_cover = QLabel(self)
        self.left_leg_cover.setGeometry(249, 552, 69, 80)
        self.left_leg_cover.setStyleSheet("background-color: white;")


    def cover_right_leg(self):
        self.right_leg_cover = QLabel(self)
        self.right_leg_cover.setGeometry(318, 552, 69, 80)
        self.right_leg_cover.setStyleSheet("background-color: white;")

    def hint1(self):
        self.hint1_btn = QPushButton(self)
        self.lightbulb = QIcon('./assets/images/hints/lightbulb.png')
        self.hint1_btn.setIcon(self.lightbulb)
        self.hint1_btn.setIconSize(QSize(50, 50))
        self.hint1_btn.setGeometry(550, 400, 50, 50)
        self.hint1_btn.setEnabled(False)

    def hint1_display_label(self):
        self.hint1_label = QLabel(self, text = "Translaton of word")
        self.hint1_label.setGeometry(600, 400, 300, 70)
        self.hint1_label.setAlignment(Qt.AlignCenter)
        self.hint1_label.setStyleSheet("font-size: 20px; font-weight: bold; font-family: Arial; color: #333333;")

    def hint2(self):
        self.hint2_btn = QPushButton(self)
        self.lightbulb = QIcon('./assets/images/hints/key.png')
        self.hint2_btn.setIcon(self.lightbulb)
        self.hint2_btn.setIconSize(QSize(50, 50))
        self.hint2_btn.setGeometry(550, 500, 50, 50)
        self.hint2_btn.setEnabled(False)

    def hint2_display_label(self):
        self.hint2_label = QLabel(self, text = "Open a letter")
        self.hint2_label.setGeometry(600, 500, 300, 70)
        self.hint2_label.setAlignment(Qt.AlignCenter)
        self.hint2_label.setStyleSheet("font-size: 20px; font-weight: bold; font-family: Arial; color: #333333;")

    def hint3(self):
        self.hint3_btn = QPushButton(self)
        self.lightbulb = QIcon('./assets/images/hints/premium.png')
        self.hint3_btn.setIcon(self.lightbulb)
        self.hint3_btn.setIconSize(QSize(50, 50))
        self.hint3_btn.setGeometry(550, 600, 50, 50)

    def hint3_display_label(self):
        self.hint3_label = QLabel(self, text = "Unlock hints")
        self.hint3_label.setGeometry(600, 600, 300, 70)
        self.hint3_label.setAlignment(Qt.AlignCenter)
        self.hint3_label.setStyleSheet("font-size: 20px; font-weight: bold; font-family: Arial; color: #333333;")
# For testing ui
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = GameUI()
    ui.show()
    sys.exit(app.exec_())