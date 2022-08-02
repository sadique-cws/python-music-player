from tkinter import *
from turtle import right

root = Tk()
root.title("cws player")
root.geometry("920x670")
root.config(bg="#0f1a2b")
root.resizable(False,False)

# top_image = PhotoImage(file="images/top.png")
# Label(root, image=top_image,bg="#0f1a2b").place(y=-170,x=50)

logo_image = PhotoImage(file="images/music icon.png")
Label(root,image=logo_image,bg="#0f1a2b",bd=0).place(x=50,y=50)

play_btn = PhotoImage(file="images/play button.png")
Button(root, image=play_btn,bg="#0f1a2b",bd=0).place(x=115,y=300)

stop_btn = PhotoImage(file="images/stop button.png")
Button(root, image=stop_btn,bg="#0f1a2b",bd=0).place(x=30,y=380)

resume_btn = PhotoImage(file="images/resume button.png")
Button(root, image=resume_btn,bg="#0f1a2b",bd=0).place(x=115,y=380)

pause_btn = PhotoImage(file="images/pause button.png")
Button(root, image=pause_btn,bg="#0f1a2b",bd=0).place(x=200,y=380)

menu = PhotoImage(file="images/menu.png")
Label(root,image=menu,bg="#0f1a2b",bd=0).place(x=450,y=200)

root.mainloop()