import webbrowser
from tkinter import *

window = Tk()
window.title("Jane Doe")
window.geometry("300x100")

def onClick(x):
    webbrowser.open(x, new=1)
label = Label(text="and im asking whyyyy lord?")
label.pack()

labelOne = Label(text="if this is how i dieeeeeee lord???.")
labelOne.pack()

url = "https://www.youtube.com/watch?v=-qUQ-YSW6Do"

click = Button(text="Click here!", command=lambda: onClick(url))
click.pack()

window.mainloop()