import webbrowser
from tkinter import *

window = Tk()
window.title("DdP Program")
window.geometry("300x100")

def onClick(x):
    webbrowser.open(x, new=1)
label = Label(text="jane doe")
label.pack()

labelOne = Label(text="Just john and me, forever eternally jane doe.")
labelOne.pack()

url = "https://www.youtube.com/watch?v=-qUQ-YSW6Do"

click = Button(text="Click here!", command=lambda: onClick(url))
click.pack()

window.mainloop()