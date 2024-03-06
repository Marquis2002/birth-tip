import datetime
import tkinter as tk
from tkinter import  ttk
from dateutil import parser

next_birth = datetime.date.today()
distance_days = 111
aiming_date = datetime.date.today() + datetime.timedelta(days=5)
aiming_saturday = datetime.date.today() + datetime.timedelta(days=9)
planning_days = 1


def outcome(next_birth, distance_days, aiming_date, aiming_saturday):
    # print(f"The date of {person.name}'s next birthday is {next_birth}.\n")
    print(f"From today to this date, there are still {distance_days} days.\n")
    print(f"And as you want to plan the party {planning_days} days in advance,"
          f"we find {aiming_date} is exactly the date you need.")
    print(f"Since you may want to find a Saturday to start planning, we recommend {aiming_saturday} as the proper day.")

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.quitButton = tk.Button(self, text="Quit Button", command=self.quit)
        self.quitButton.grid()



def main():

    # Method1

    # app = Application()
    # app.master.title('Sample application')
    # app.mainloop()

    # Method 2

    root = tk.Tk(screenName="screen name", baseName="base name", )
    root.title("Birthday Tips")

    Lable = tk.Label(root, text="GUI Tkinter")
    Lable.pack()

    Button = tk.Button(root, text="Quit", command=)

    root.mainloop()



main()