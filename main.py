import threading
import tkinter as tk

LARGE_FONT = ("Comic Sans", 12)

class Oberflaeche(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # get the information about width and height of your screen
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()

        # to get rid of the titlebar:
        # self.overrideredirect(1)

        # redefine the geometry of your mainwindow
        self.geometry("%dx%d+0+0" % (w, h))
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()
        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):  # Method representing the thread's activity
        app = Oberflaeche() # Toplevel-Widget
        app.mainloop()  # mainloop of Tk

# define one "app" as App - this starts the GUI
app = App()

# From this point on we can run a thread in parallel to our
print('Now we can continue running code while mainloop runs!')

# dummy lines to have something to calculate for proof of threading
i=0
while i < 100000:
    i = i+1
    print(i)
    if(i==100000):
        i=0



################################################################
# import tkinter as tk                # python 3
# from tkinter import font  as tkfont # python 3
# #import Tkinter as tk     # python 2
# #import tkFont as tkfont  # python 2
#
#
#
#
# #
# # class App(threading.Thread):
# #
# #     def __init__(self):
# #         threading.Thread.__init__(self)
# #         self.start()
# #
# #     def callback(self):
# #         self.root.quit()
# #
# #     def run(self):
# #         self.root = tk.Tk()
# #         self.root.protocol("WM_DELETE_WINDOW", self.callback)
# #
# #         label = tk.Label(self.root, text="Hello World")
# #         label.pack()
# #
# #         self.root.mainloop()
# #
# #
# # app = App()
# # print('Now we can continue running code while mainloop runs!')
# #
# # for i in range(100000):
# #     print(i)
#
#
# class SampleApp(threading.Thread):
#
#     def __init__(self): #, args: object, kwargs: object) -> object:
#         threading.Thread.tk.Tk.__init__(self) #, *args, **kwargs)
#         #tk.Tk.__init__(self, *args, **kwargs)
#
#         self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
#
#         # the container is where we'll stack a bunch of frames
#         # on top of each other, then the one we want visible
#         # will be raised above the others
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         # get the information about width and height of your screen
#         w, h = self.winfo_screenwidth(), self.winfo_screenheight()
#
#         # to get rid of the titlebar:
#         #self.overrideredirect(1)
#
#         # redefine the geometry of your mainwindow
#         self.geometry("%dx%d+0+0" % (w, h))
#
#         self.frames = {}
#
#         for F in (StartPage, PageOne, PageTwo, PageTemplate):
#             page_name = F.__name__
#             frame = F(parent=container, controller=self)
#             self.frames[page_name] = frame
#
#             # put all of the pages in the same location;
#             # the one on the top of the stacking order
#             # will be the one that is visible.
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         self.show_frame("StartPage")
#         self.start()
#
#     def show_frame(self, page_name):
#         '''Show a frame for the given page name'''
#         frame = self.frames[page_name]
#         frame.tkraise()
#
#
#     def callback(self):
#         self.root.quit()
#
#     def run(self):
#         self.root = tk.Tk()
#         self.root.protocol("WM_DELETE_WINDOW", self.callback)
#
#         label = tk.Label(self.root, text="Hello World")
#         label.pack()
#
#         self.root.mainloop()
#
#
#
# class StartPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is the start page", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#
#         button1 = tk.Button(self, text="Go to Page One",
#                             command=lambda: controller.show_frame("PageOne"))
#         button2 = tk.Button(self, text="Go to Page Two",
#                             command=lambda: controller.show_frame("PageTwo"))
#         button3 = tk.Button(self, text="Quit",
#                             command=self.quit)
#         button4 = tk.Button(self, text="test rfid.py import",
#                             command=rfid.test)
#         button1.pack()
#         button2.pack()
#         button3.pack()
#         button4.pack()
#
#
# class PageOne(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is page 1", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#         button.pack()
#
#
# class PageTwo(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is page 2", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#         button.pack()
#
#
# class PageTemplate(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#
#
#
# #if __name__ == "__main__":
#
# app = SampleApp()
#     #app.mainloop()
#
# for i in range(100000):
#     print(i)
# # ich bin ein neuer Kommentar
