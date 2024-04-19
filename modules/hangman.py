import random

from interface.hangman_ui import GameUI

from modules.helpers import get_definition
from modules.helpers import translate_text
from modules.helpers import open_ads

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

import os


from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl


is_game_on = True


class Hangman(GameUI):
    def __init__(self, /, *, sound_status, difficulty_level) -> None:
        super().__init__()
        self.lives = 6


        if sound_status:
            # Background music
            self.play_sound('bg_music.mp3', bg_music=True)
        if difficulty_level == 'easy':
            self.maxLen = 10
            self.minLen = 5
            self.chosen_word = self.choose_word()
            self.generate_blanks(len(self.chosen_word))

        elif difficulty_level == 'medium':
            self.maxLen = 5
            self.minLen = 3
            self.chosen_word = self.choose_word()
            self.generate_blanks(len(self.chosen_word))

        elif difficulty_level == 'hard':
            self.maxLen = 4
            self.minLen = 2
            self.chosen_word = self.choose_word()
            self.generate_blanks(len(self.chosen_word))

        self.display_definition(get_definition(self.chosen_word))
        


        self.guess = ''
        self.guessed_letters = []

        # connect function
        self.hint1_btn.clicked.connect(self.show_hint1)
        self.hint2_btn.clicked.connect(self.show_hint2)
        self.hint3_btn.clicked.connect(self.show_hint3)
        

    def choose_word(self) -> None:
        try:
            with open('./data/words.txt', 'r') as file:
                lines = file.readlines()

                chosen_word: str = random.choice(lines).strip()


                while len(chosen_word) > self.maxLen or len(chosen_word) < self.minLen:
                    chosen_word = random.choice(lines).strip()

                return chosen_word.lower()
        except FileNotFoundError:
            print("Error: 'words.txt' file not found.")
            return ""
        
    def display_letter(self, letter: str) -> None:
        global is_game_on
        if letter in self.guessed_letters:
            self.play_sound('buzzer.mp3')
            return

        if letter in self.chosen_word:
            for index, char in enumerate(self.chosen_word):
                if char == letter:
                    self.word_place[index] = letter
                    self.blank_label.setText('  '.join(self.word_place))
                    self.play_sound('correct.mp3')
                    if "".join(self.word_place) == self.chosen_word:
                        is_game_on = False
                        self.status = 'win'
                        self.close()
                        self.game_over()
                        
                        return 
        else:
            if letter not in self.guessed_letters:
                self.body_parts[6-self.lives].hide()
                self.play_sound('wrong-answer.mp3')
                
                self.lives -= 1
                if self.lives == 0:
                    self.close()
                    is_game_on = False
                    self.status = 'lose'
                    self.game_over()

        self.guessed_letters.append(letter)

    def show_hint1(self):
        self.disabled_hint = QIcon('./assets/images/hints/disabled_lightbulb.png')
        self.hint1_btn.setIcon = self.disabled_hint
        self.hint1_btn.setEnabled(False)
        self.play_sound('hint.mp3')

        self.hint1_label.setText(translate_text(self.chosen_word))

    def show_hint2(self):
        self.hint2_btn.setEnabled(False)
        not_found_chars = [char for char in self.chosen_word if char not in self.word_place]
        self.play_sound('hint.mp3')

        if not_found_chars:
            hint_char = random.choice(not_found_chars)
            hint_text = f"{hint_char}"
            self.hint2_label.setText(hint_text)
        else:
            self.hint2_label.setText("No character is missing.")

    

    
    def show_hint3(self):
        self.hint3_btn.setEnabled(False)
        self.play_sound('game-bonus.mp3')
        open_ads('https://rahmatilla.uz')
        

        self.hint1_btn.setEnabled(True)
        self.hint2_btn.setEnabled(True)

        self.hint3_label.setText('Hints unlocked!')



    def keyPressEvent(self, event):
        global is_game_on
        if not is_game_on:
            return
        key = event.key()
        if Qt.Key_A <= key <= Qt.Key_Z:  
            self.guess = chr(key).lower()
            self.display_letter(self.guess)
        else:
            pass
    
    def game_over(self) -> tuple[str, bool]:
        global is_game_on

        is_game_on = False

        if self.status == 'win':
            return self.chosen_word, True
        else:
            return self.chosen_word, False

    def get_game_status(self) -> bool:
        return is_game_on
    
    def closeEvent(self, event):
        try:
            self.player.stop()
            try:
                self.player2.stop()
            except:
                pass
        except:
            pass

    def play_sound(self, sound: str, bg_music: bool = False):
        try:
            sound_path = os.path.join('assets', 'music', sound)

            if bg_music:
                self.player: QMediaPlayer = QMediaPlayer()
                self.player.setMedia(QMediaContent(QUrl.fromLocalFile(sound_path)))
                self.player.setVolume(90)  
                self.player.play()
                self.player.positionChanged.connect(self.replay_sound)
            else:
                self.player2: QMediaPlayer = QMediaPlayer()

                self.player2.setMedia(QMediaContent(QUrl.fromLocalFile(sound_path)))
                self.player2.setVolume(30) 
                self.player2.play()
        except Exception as e:
            print(e)

    def replay_sound(self):
        if self.player.position() > 171000:
            self.player.setPosition(0)
        
    