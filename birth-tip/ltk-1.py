import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Birthday Tips")
        self.geometry("1000x500")
        # create frames for index
        self.index_1 = Index()
        self.index_2 = SubIndex()


class Index(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack(expand=0, fill='both')
        self.frm1 = tk.Frame()
        self.label1 = tk.Label(self.frm1, text="text")
        self.label2 = tk.Label(self.frm1, text="text")
        self.label3 = tk.Label(self.frm1, text="text")
        self.label4 = tk.Label(self.frm1, text="text")
        self.label5 = tk.Label(self.frm1, text="text")

        self.frm1.pack()
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.label5.pack()

        self.button = tk.Button(self.frm1, text="Button")
        self.button.bind("<Button-1>", self.change)
        self.button.pack()

        self.frm2 = tk.Frame()
        self.button2 = tk.Button(self.frm2, text="Button2")
        self.button2.bind("<Button-1>", self.change2)
        self.button2.pack()

        self.label2_2 = tk.Label(self.frm2, text="This is frm2")
        # self.frm2.pack()
        self.label2_2.pack()

    def change(self, event):
        self.frm1.pack_forget()
        self.frm2.pack()

    def change2(self, event):
        self.frm2.pack_forget()
        self.frm1.pack()




class SubIndex(tk.Frame):
    def __init__(self, parent=None):
        super().__init__()




def main():
    app = MyApp()
    app.mainloop()

main()