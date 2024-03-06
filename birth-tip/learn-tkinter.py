import tkinter as tk
class Index(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack()

        # self.frame_left = tk.Frame()
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Creating the application variable
        self.contents = tk.StringVar()
        # Set it to some value
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # Define a callback when the user hits return
        # It prints the current value of the variable.
        self.entrythingy.bind("<Key-Return>", self.event_dealer)



        # button = tk.Button(text="Go to Window1", command=self.event_dealer)

    def event_dealer(self, event):
        print("Hi, the current entry content is: ", self.contents.get())


class Window1(tk.Frame):
    def __init__(self, parent=None):
        button = tk.Button(text="Button", command=self.root.destroy)
        button2 = tk.Button(text="Delete Button", command=button.destroy)
        button.pack(side="right")
        button2.pack(expand=1, side='left',pady=200)
        self.root.mainloop()
    # def quit(self):
    #     self.root.destroy()

class Window2(tk.Frame):
    def __init__(self, parent=None):
        self.root = tk.Tk()
        self.root.geometry('1000x500')
        frm = tk.Frame()
        frm.pack(expand=22)

        frm1 = tk.Frame(frm)
        frm1.pack(expand=3)

        lab1 = tk.Label(frm1, text="Label1", pady=5, relief="raised")
        lab2 = tk.Label(frm, text="Label2", relief="groove")
        lab3 = tk.Label(frm1, text="Label3", relief="flat")
        lab1.pack(expand=3)
        lab2.pack()
        lab3.pack()




        self.root.mainloop()

def main():
    root = tk.Tk()
    root.geometry('1500x750')
    app = Index(root)
    app.mainloop()
main()