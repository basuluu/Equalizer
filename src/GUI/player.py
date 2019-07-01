from tkinter import messagebox
from tkinter import filedialog as fd
from threading import Thread
from src.effects.echo import EchoEffect
from src.effects.distortion import DistortionEffect

class Player:
    def __init__(self, tk_root, equalizer_obj):
        self.tk_root = tk_root
        self.eq = equalizer_obj
        self.play_is_active = False
        self.effect_is_active = False
    
    def choice_no_effect(self):
        self.effect_is_active = False

    def choice_echo_effect(self):
        self.effect = EchoEffect(self.eq)
        self.effect_is_active = True

    def choice_distortion_effect(self):
        self.effect = DistortionEffect(self.eq)
        self.effect_is_active = True

    def play_music(self):
        while self.play_is_active:
            if self.effect_is_active == True:
                self.effect.processing()
            else:
                self.eq.processing()
                
    def play(self):
        if not self.play_is_active:
            self.play_is_active = True
            t = Thread(target = self.play_music, args = ())
            t.start()

    def pause(self):
        self.play_is_active = False
            
    def restart(self):
        self.eq.data_start_pos = 0
        self.eq.data_end_pos = self.eq.rate_to_processing
        self.play()
    
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.play_is_active = False
            self.tk_root.destroy()

    def open_audio(self):
        file_path = fd.askopenfilename()
        if file_path:
            if file_path[-4:] != '.wav':
                self.open_audio()
            else:
                self.eq.set_input_stream(file_path)
