import sys
import subprocess

try:
    from PyQt5.QtWidgets import QApplication
    from deep_translator import GoogleTranslator
    import requests
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    subprocess.check_call([sys.executable, 'main.py'])
   


from modules.hangman import Hangman
from modules.game_over import GameOver
from modules.starting import Starting

from PyQt5.QtWidgets import QApplication

# Running
if __name__ == '__main__':
    
    app: QApplication = QApplication(sys.argv)
    
    starting: Starting = Starting()

    app.exec_()
    is_sound_on = starting.get_sound_status()
    chosen_level = starting.get_difficulty_level()

    if chosen_level:

        mainInterface: Hangman = Hangman(sound_status = is_sound_on, difficulty_level = chosen_level)

        mainInterface.show()

        app.exec_()

        is_game_on = mainInterface.get_game_status()

        if not is_game_on:
            chosen_word, status = mainInterface.game_over()
            game_over: GameOver = GameOver(original_word=chosen_word, status=status)
            
            app.exec_()

    if starting.close or game_over.close or mainInterface.close:
        sys.exit()