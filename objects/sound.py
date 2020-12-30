from pygame import mixer


class Sound:
    def __init__(self, sound):
        self.sound = mixer.Sound(sound)
    
    def play(self, duration):
        self.sound.play()