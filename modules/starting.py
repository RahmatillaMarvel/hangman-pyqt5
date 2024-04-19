from interface.starting_ui import StartingUI

chosen_level: str | None = None
is_sound_on: bool = True


class Starting(StartingUI):
    def __init__(self) -> None:
        super().__init__()


        self.easy_level.clicked.connect(lambda: self.set_difficulty_level('easy'))
        self.medium_level.clicked.connect(lambda: self.set_difficulty_level('medium'))
        self.hard_level.clicked.connect(lambda: self.set_difficulty_level('hard'))

        self.mute_sound.clicked.connect(lambda: self.sound_settings(False))
        self.unmute_sound.clicked.connect(lambda: self.sound_settings(True))

        
        self.show()


    def set_difficulty_level(self, level: str) -> None:
        global chosen_level
        chosen_level = level
        self.close()

    def get_difficulty_level(self) -> str:
        if chosen_level:
            return chosen_level
        
    def sound_settings(self, status: bool) -> None:
        global is_sound_on
        if status:
            self.unmute_sound.hide()
            self.mute_sound.show()
            self.sound_label.setText('Sound: OFF')
            is_sound_on = False
        else:
            self.unmute_sound.show()
            self.mute_sound.hide()
            self.sound_label.setText('Sound: ON')
            is_sound_on = True

    def get_sound_status(self) -> bool:
        return is_sound_on
    


    def closeEvent(self, event):
        try:
            self.player.stop()
        except:
            pass