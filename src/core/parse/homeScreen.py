import tkinter
from tkinter import *
from PIL import *
import customtkinter
from core.parse.game_parser import *
import tkinter.messagebox
import os
import time

state = False
def click(event):
    gameInput.config(state=NORMAL)
    gameInput.delete(0,END)

def press(event):
    try:

        global gameInput

        #g.add_game(gameInput.get())
        gameInputs = gameInput.get().split(",")
        for gameInput in gameInputs:
            try:
                g.add_game(gameInput)
            except:
                pass
        # a = g.get_movie_recommendations()[0]
        #a.image.save(a.name+".jpg")
        #img2 = ImageTk.PhotoImage(Image.open("WarHunt.jpg"))
        a = g.get_movie_recommendations()

        a[0].image.show()
        for i in range(1,5):
            time.sleep(1)
            a[i].image.show()
            print(a[i].name)
        # frame1.lower()
        # frame2.lift()
        # frame2.place(x=5, y=5)
        # frame3.lift()
        # #lb = Label(frame3,image=img2).pack()
        # frame3.place(x=50,y=50)

    except:
        tkinter.messagebox.showinfo("Invalid Game:", "Please enter a new game")
        pass


def prev():
    frame2.lower()
    frame1.lift()
    state = False
    frame3.lower()

window = Tk()
window.title = "Video Game to Movie Recommender"
width = 923
height = 641
window.geometry("923x641")

# # Search function
gameInput = ""
frame1 = Frame(window, bg='#a2b0a5')
labelSearch = Label(frame1,text="I like playing...", bg='#a2b0a5',font=("Helvetica", 25))

gameInput = Entry(frame1, font=("Helvetica", 25))
gameInput.insert(0,"name of game")
gameInput.config(state=DISABLED)
gameInput.bind("<Button-1>", click)
gameInput.bind("<Return>", press)

frame1.place(x=width/2-160,y=height/2-100)

frame2 = Frame(window, bg='black')
#back_btn = PhotoImage(file="back.png")
b = Button(frame2, text="return", command=prev, bg='#d5f7e3',width=8, height=2, font=("Helvetica", 12))
b.pack()


frame3 = Frame(window)


labelSearch.pack()
gameInput.pack()

bg = PhotoImage(file ="home Background.png")
background = Label(window, image = bg)
background.lower()
background.place(x = 0, y = 0)

background.pack()

mainloop()

# if __name__ == "__main__": GUI()
#
# #window = customtkinter.CTk()
# window = Tk()
# width = 1920 # Width
# height = 1080 # Height
# window.geometry(f'{width}x{height}+{-10}+{0}')
#
# # Set Background image
# bg = PhotoImage(file = "home Background.png")
# background = Label(window, image = bg)
# # background.place(x = 0, y = 0)
# background.pack()
#
# def click(event):
#     gameInput.config(state=NORMAL)
#     gameInput.delete(0,END)
#
# def press(event):
#     window.destroy()
#     import movieScreen
#
#
# # Search function
# labelSearch = Label(window,text = "I like playing...")
# gameInput = Entry(window)
# gameInput.insert(0,"name of game")
# gameInput.config(state=DISABLED)
# gameInput.bind("<Button-1>", click)
#
# gameInput.bind("<Return>", press)
#
# labelSearch.pack()
# gameInput.pack()
#
#
# window.mainloop()