from tkinter import *
import multiprocessing
from playsound  import playsound
root = Tk()
root.title('Sound')
root.geometry('600x400')
p = multiprocessing.Process(target=playsound, args=('stimela.mp3',))



def playmusic():
    p.start()

def stopmusic():
    p.terminate()


play_btn = Button(root, text='Play', command=playmusic)
play_btn.place(x=5, y=50)

stop_btn = Button(root, text='Stop', command=stopmusic)
stop_btn.place(x=5, y=100)


root.mainloop()
