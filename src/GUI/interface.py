from tkinter import *
from PIL import ImageTk 
from src.equalizer.equalizer import Equalizer
from src.GUI.player import Player
from src.GUI.slider import Slider

def __main__():
    master = Tk()
    master.geometry("800x600")
    name_range = ['<320Hz', '320-960Hz', '960-2240Hz', '2240-4800Hz', '4800-9920Hz', '>9920Hz']
    Eq = Equalizer()    
    Eq.set_input_stream(path="src/music/sum41.wav")
    player = Player(master, Eq)

    master.protocol("WM_DELETE_WINDOW", player.on_closing)

    effectframe = Frame(master)
    middleframe = Frame(master)
    importframe = Frame(master)
    for i in range(6): 
        w = Slider(Eq.filters[i], master)
        w.setName(name_range[i])
        w.name.place(x=75-4+115*i, y=180)
        w.scale.place(x=75+115*i, y=200, height=200)
        w.label.place(x=75+2+115*i, y=410, height=20, width=60)
        w.name.config(font=("Helvetica", 12))
        w.label.config(font=("Helvetica", 12))

    var = IntVar()
    var.set(0)
    R0 = Radiobutton(effectframe, text="No effect", font=("Times New Roman", 14), 
                     activebackground=master['background'], variable=var, value=0, 
                     command=player.choice_no_effect)
    R1 = Radiobutton(effectframe, text="Echo", font=("Times New Roman", 14), 
                     activebackground=master['background'], variable=var, value=1, 
                     command=player.choice_echo_effect)
    R2 = Radiobutton(effectframe, text="Distortion", font=("Times New Roman", 14), 
                     activebackground=master['background'], variable=var, value=2, 
                     command=player.choice_distortion_effect)
    Label(effectframe, text="Choice effect:", height=5, font=("Helvetica", 16), 
          justify="center", anchor="c").grid(row=0, column=0)

    R0.grid(row=0, column=1)
    R1.grid(row=0, column=2)
    R2.grid(row=0, column=3)

    import_button_img = ImageTk.PhotoImage(file="src/images/import_button.png")
    B0 = Button(importframe, image=import_button_img, border=0, cursor="fleur", 
                activebackground=master['background'], command=player.open_audio)
    B0.grid(row=0, column=1, padx=20)
    Label(importframe, text="Import music file(*.wav):", height=5, font=("Helvetica", 16), 
          justify="center", anchor="c").grid(row=0, column=0)

    launch_button_img = ImageTk.PhotoImage(file="src/images/launch_button.png")
    B1 = Button(middleframe, image=launch_button_img, border=0, cursor="hand1",
                activebackground=master['background'], command=player.play)
    B1.grid(row=0, column=0, padx=10, pady=10)

    pause_button_img = ImageTk.PhotoImage(file="src/images/pause_button.png")
    B2 = Button(middleframe, image=pause_button_img, border=0, cursor="hand1",
                activebackground=master['background'], command=player.pause)
    B2.grid(row=0, column=1, padx=10, pady=10)

    restart_button_img = ImageTk.PhotoImage(file="src/images/restart_button.png")
    B3 = Button(middleframe, image=restart_button_img, border=0, cursor="hand1",
                activebackground=master['background'], command=player.restart)
    B3.grid(row=0, column=2, padx=10, pady=10)

    middleframe.place(x=265, y=430)
    importframe.place(x=265, y=30)
    effectframe.place(x=75, y=485)
    mainloop()

 
