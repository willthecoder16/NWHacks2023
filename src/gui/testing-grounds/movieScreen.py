from tkinter import *

window = Tk()
width = 923
height = 641
window.geometry("923x641")

def prevPage():
    window.destroy()


frame1 = Frame(window)
b = Button(
    window,
    text="Previous Page",
    command=prevPage
    )
b.pack()

# ws.geometry("{}x{}+{}+{}".format(width, height, int(x), int(y)))

# f = ("Times bold", 14)

# def prevPage():
#     ws.destroy()
#     import homeScreen
    
# Label(
#     ws,
#     text="This is First page",
#     padx=20,
#     pady=20,
#     bg='#5d8a82',
#     font=f
# ).pack(expand=True, fill=BOTH)

# Button(
#     ws, 
#     text="Previous Page", 
#     font=f,
#     command=prevPage
#     ).pack(fill=X, expand=TRUE, side=LEFT)

# button = ws.CTkButton(master=ws, text="prev", command=prevPage)



mainloop()