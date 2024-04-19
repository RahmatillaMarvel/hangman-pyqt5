import sys
import time
import subprocess

from interface.game_over_ui import GameOverUI

from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl


class GameOver(GameOverUI):
    def __init__(self, /, *, original_word: str, status: str) -> None:
        
        super().__init__(original_word=original_word, status=status)
        print(status)
        if status:
            self.play_winning_sound()
        else:
            self.play_losing_sound()
        

        self.yes.clicked.connect(self.restart_game)
        self.no.clicked.connect(self.close_without_restart)
        self.exit.clicked.connect(self.close_application)


        self.show()
        


    def restart_game(self):
        global is_game_on
        is_game_on = True  
        self.close()  

        time.sleep(0.5)

        subprocess.call("python main.py", shell=True)

        sys.exit()

    def close_without_restart(self):
        self.close()
        sys.exit()

    def close_application(self):
        reply = QMessageBox.question(self, 'Exit Confirmation', 
            "Are you sure you want to exit the game?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def play_winning_sound(self):
        try:
            self.winning_sound: str = 'assets/music/congratulations.mp3'
            self.player: QMediaPlayer = QMediaPlayer()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.winning_sound)))
            self.player.play()

        except Exception as e:
            print(e)


    def play_losing_sound(self):
        try:
            self.losing_sound: str = 'assets/music/violin-lose.mp3'
            self.player: QMediaPlayer = QMediaPlayer()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.losing_sound)))
            self.player.play()

        except Exception as e:
            print(e)