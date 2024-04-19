import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,  QSize



class StartingUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Game name
        self.setWindowTitle('Hangman: Intro & Setting')

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

        # Set UI
        self.setUI()
    
    def setUI(self):
        # Title
        self.title_label = QLabel(self, text='Hangman')
        self.title_label.resize(500, 70)
        self.title_label.move(0, 50)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 35px; font-weight: bold; font-family: Arial; color: #333333;")

        self.secondary_label = QLabel(self, text='Please choose difficulty level:')
        self.secondary_label.resize(500, 70)
        self.secondary_label.move(0, 120)
        self.secondary_label.setAlignment(Qt.AlignCenter)
        self.secondary_label.setStyleSheet("font-size: 20px; font-weight: bold; font-family: Arial; color: #333333;")

        self.easy_level = QPushButton(self, text='Easy')
        self.easy_level.resize(400, 70)
        self.easy_level.move(50, 200)
        self.easy_level.setStyleSheet(self.btn_style)

        self.medium_level = QPushButton(self, text='Medium')
        self.medium_level.resize(400, 70)
        self.medium_level.move(50, 280)
        self.medium_level.setStyleSheet(self.btn_style)

        self.hard_level = QPushButton(self, text='Hard')
        self.hard_level.resize(400, 70)
        self.hard_level.move(50, 360)
        self.hard_level.setStyleSheet(self.btn_style)

        # Sound settings
        self.mute_sound = QPushButton(self, icon=QIcon('./assets/images/icon/mute.png'))
        self.mute_sound.setIconSize(QSize(40, 40))
        self.mute_sound.resize(40, 40)
        self.mute_sound.move(50, 500)
        self.mute_sound.setStyleSheet("border: none; background: transparent;")
        self.mute_sound.hide()

        # Unmute sound
        self.unmute_sound = QPushButton(self, icon=QIcon('./assets/images/icon/unmute.png'))
        self.unmute_sound.setIconSize(QSize(40, 40))
        self.unmute_sound.resize(40, 40)
        self.unmute_sound.move(50, 500)
        self.unmute_sound.setStyleSheet("border: none; background: transparent")

        # Sound label
        self.sound_label = QLabel(self, text='Sound is on')
        self.sound_label.resize(100, 40)
        self.sound_label.move(100, 500)
        self.sound_label.setAlignment(Qt.AlignCenter)
        self.sound_label.setStyleSheet("font-size: 15px; font-weight: bold; font-family: Arial; color: #333333;")

        # Copyright
        self.copyright = QLabel(self)
        self.copyright.setText('Copyright © 2024. All rights reserved. <br><br> Developed by: <br> <a href="http://rahmatilla.uz">Rahmatilla Xudoyberdiyev</a>')
        self.copyright.resize(500, 70)
        self.copyright.move(0, 600)
        self.copyright.setAlignment(Qt.AlignCenter)
        self.copyright.setStyleSheet("font-size: 15px; font-weight: bold; font-family: Arial; color: #333333;")
        self.copyright.setOpenExternalLinks(True)





# For testing ui
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = StartingUI()
    ui.show()
    sys.exit(app.exec_())