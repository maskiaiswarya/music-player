from tkinter import *
from tkinter import filedialog
from pygame import mixer

class Music:
    def __init__(self,a):
        a.geometry('300x200')
        a.title('Music Player')
        a.resizable(0,0)
        Load=Button(a,text='Load',width=10,font=('Times',10,'bold'),command=self.load)
        Play=Button(a,text='Play',width=10,font=('Times',10,'bold'),command=self.play)
        Stop = Button(a,text = 'Stop',  width = 10, font = ('Times', 10,'bold'), command = self.stop)
        Load.place(x=50,y=40)
        Play.place(x=150,y=40)
        Stop.place(x=110,y=75) 
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def stop(self):
        mixer.music.stop()
a=Tk()
a.configure(background="light pink")
heading= Label(a,text="MUSIC PLAYER ♫♫♫♫....",fg="blue",bg="pink",font=("Times",15,'bold'))
heading.pack(side=TOP)
app=Music(a)
a.mainloop()
