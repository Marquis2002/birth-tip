import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()




# method 1
# from dateutil import parser
# import datetime
# from tkinter import *
# from tkinter import ttk
#
# val1 = 23223
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text=f"text1 = {23223}").grid(column=0, row=0)
# btn = ttk.Button(frm, text="hello")
# btn.grid(column=2, row=2)
#
# fred = Button(frm, text="hi", padx=20, pady=30, fg="red", bg="blue")
# fred.grid(column=2, row=3)
# print(f"btn's configure is :{btn.configure()}\n")
# print(f"btn's keys() is :{btn.keys()}\n")
# print(f"btn.configure().keys() is :{btn.configure().keys()}\n")
#
# print(f"set(btn.configure().keys()) - set(frm.configure().keys()) is: {set(btn.configure().keys()) - set(frm.configure().keys())}\n")
# print(f"dir(btn) is :{dir(btn)}\n")
# # print(f"set(dir(btn) - set(dir(frm))) is : {set(dir(btn) - set(dir(frm)))}")
#
# # ttk.Button(frm, text=f"text2").grid(column=1, row=0)
# root.mainloop()
#
