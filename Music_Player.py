
# #Loading and playing music with Pygame
# from pygame import mixer
# mixer.init() #Inirializing pygame
# mixer.music.load.('filename.mp3') #Loading Music File
# mixer.music.pause() #Pausing the music
# mixer.music.play() #Playing Music File
#
# #Pausing and unpausing the music
#
# mixer.music.pause() #Pausing the music
#
# mixer.music.unpause() #Unpausing the music
#
# #Stopping a music file
#
# mixer.music.stop()


#Importing all the necessary files
from tkinter import *
from tkinter import filedialog
from pygame import mixer

#Implementing classes and buttons for the applications

class MusicPlayer:
    def __init__(self,window):
        window.geometry('320x100'); window.title('Iris player'); window.resizable(0,0)
        Load = Button(window, text = 'Load', width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Start',  width = 10, font = ('Times', 10), command = self.play)
        Pause = Button(window, text = 'Play/Pause', width = 10, font = ('Time', 10), command = self.pause)
        Stop = Button(window, text = 'Stop', width = 10, font = ('Time', 10), command = self.stop)
        Load.place(x=0, y=0);Play.place(x=110,y=20);Pause.place(x=220, y=20);Stop.place(x=110,y=60)
        self.music_file = False
        self.playing_state = False
    #Load method
    def load(self):
        self.music_file = filedialog.askopenfilename()

      #Play method
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    #Pause method
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    #Stop Method

    def stop(self):
        mixer.music.stop()

root = Tk()
app = MusicPlayer(root)
root.mainloop()






