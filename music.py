import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer
root = Tk()
root.title("cws player")
root.geometry("920x670")
root.config(bg="#0f1a2b")
root.resizable(False,False)

mixer.init()

# top_image = PhotoImage(file="images/top.png")
# Label(root, image=top_image,bg="#0f1a2b").place(y=-170,x=50)

def addMusicHandle():
    path = filedialog.askdirectory()

    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

                

def playMusic():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(music_name)
    mixer.music.play()

logo_image = PhotoImage(file="images/music icon.png")
Label(root,image=logo_image,bg="#0f1a2b",bd=0).place(x=50,y=50)

play_btn = PhotoImage(file="images/play button.png")
Button(root, image=play_btn,bg="#0f1a2b",bd=0,command=playMusic).place(x=115,y=300)

stop_btn = PhotoImage(file="images/stop button.png")
Button(root, image=stop_btn,bg="#0f1a2b",bd=0).place(x=30,y=380)

resume_btn = PhotoImage(file="images/resume button.png")
Button(root, image=resume_btn,bg="#0f1a2b",bd=0).place(x=115,y=380)

pause_btn = PhotoImage(file="images/pause button.png")
Button(root, image=pause_btn,bg="#0f1a2b",bd=0).place(x=200,y=380)

menu = PhotoImage(file="images/menu.png")
Label(root,image=menu,bg="#0f1a2b",bd=0).place(x=450,y=200)

frame_playlist = Frame(root, bd=2,  relief=RIDGE)
frame_playlist.place(x=455, y= 320, width=390, height=190)

add_music = Button(root,command=addMusicHandle,text="Add Music",bg="cyan",fg="black",highlightbackground="cyan",highlightcolor="black")
add_music.place(x=480,y=290)

playlist = Listbox(frame_playlist,width=100,fg="white",bg="#333333",bd=0)
playlist.pack(side=LEFT, fill=BOTH)





root.mainloop()