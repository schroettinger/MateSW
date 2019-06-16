from tkinter import *
import sys



class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("hi there, everyone!")


# one root element as tk inter main element
root = Tk()

# get the information about width and height of your screen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

# to get rid of the titlebar:
root.overrideredirect(1)

# redefine the geometry of your mainwindow
root.geometry("%dx%d+0+0" % (w, h))

# one instance of the 'App' class
app = App(root)

# start the mainloop for showing the window
root.mainloop()


