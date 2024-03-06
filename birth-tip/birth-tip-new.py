
import string
import datetime
from dateutil import parser
from tkinter import *
from tkinter import ttk


# Input Parameters
date = datetime.date.today()
planning_days = 0
# date_str1 = "2002.12.26"
# date1 = parser.parse(date_str1)


print(f">>>>>date is: {date}")


class Person(object):
    def __init__(self, name, birthday, relation):
        self.name = name
        self.birthday = birthday
        self.relation = relation

# Mediate Parameters
distance = 0


# Outcome Parameters


# Down from here, five functions are created by step.
def welcome():
    print("Welcome to the birthday tip. \nThis program will help you ")
    input("Enter anything to go on\n> ")


def insert():
    # print(f"Whether a new member needs to be inserted(y/n)")
    # flag_insert = input("> ")
    print(f"do you want to initialize the information?(y/n)\n")
    while 1:
        flag_init = input("initialization> ")
        if flag_init == 'y':
            with open("members.txt", "w") as inif:
                pass
            break
        elif flag_init == 'n':
            break
        else:
            print(f"The word entered is wrong, please enter again\n")

    while 1:
        flag_ins = True
        while 1:
            flag = input("Whether a new member needs to be inserted(y/n)\n>  ")
            if flag == 'y':
                print(f"insert the member's name and birthday:\n")
                inf_name = input("name> ")
                inf_rel = input("relationship> ")
                inf_birth = input("birthday> ")

                with open("members.txt", "a") as f:
                    f.write(inf_name)
                    f.write(" ")
                    f.write(inf_rel)
                    f.write(" ")
                    f.write(inf_birth)
                    f.write("\n")
                break
            elif flag == 'n':
                flag_ins = False
                break
            else:
                print(f"The word entered is wrong, please enter again\n")

        if not flag_ins:
            break


def enter_info():
    global person
    global date
    # global planning_days
    # print("\tPlease enter your friend's name and birthday.\n")
    with open("members.txt", "r") as f1:
        for line in f1.readlines():
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            print(line)

    f2 = open("members.txt", "r")
    lines = f2.readlines()
    while 1:
        flag_name = False
        print(f"Please enter the name that you choose.\n")
        name = input("name > ")
        for line in lines:
            if line.find(name) != -1:
                birthday = line[find_nth_(line, 2):]
                birthday = birthday.strip('\n')
                relation
                flag_name = True

                break
        if flag_name:
            break
        else:
            print(f"can`t find the information, please enter again\n")

    person = Person(name, birthday, relation)
    # print(f"\tHow many days do you want to cost planning the party in advance?\nPlease enter here\n")
    # planning_days = input("planning_days > ")


def calculation():
    global planning_days
    global aiming_saturday
    to_date = date
    # At the very beginning, resolve the person's information.
    print(f"{person.name}'s birthday is {person.birthday}")
    birth_date = parser.parse(person.birthday)
    while 1:
        flag = input("Enter 'y' if you want to use the date today.\n>  ")
        if flag == 'y':
            to_date = datetime.date.today()
            break
        elif flag == 'n':
            print(f"n has been entered.\n")
            print(f"Please enter the date you want to use.\n")
            new_date = input("> ")
            to_date = parser.parse(new_date).date()
            break
        else:
            print(f"The word entered is wrong, please enter again\n")

    # Getting the nearest birthday named this_birth
    # Then calculate the days between those two dates
    # After that, decide which the next birth
    to_year = to_date.year
    this_birth = birth_date.replace(year=to_year).date()
    distance_1 = this_birth - to_date
    distance_days = distance_1.days

    if distance_days > 0:
        next_birth = this_birth
    else:
        next_birth = this_birth.replace(year=to_year + 1)

    distance_1 = next_birth - to_date
    distance_days = distance_1.days
    # print(f">>>distance_days is :{distance_days}")

    print(f"The next birthday date is {next_birth}.")
    print(f"Today is {distance_days} days until the next birthday.")

    print(f"\tHow many days do you want to cost planning the party in advance?\nPlease enter here\n")
    while 1:
        planning_days = input("planning_days > ")
        if int(planning_days) < 0:
            print("The number entered is wrong, please enter again\n")
        elif int(planning_days) > distance_days:
            print(f"The time entered is longer than the time interval, please enter again\n")
        else:
            break

    # Now calculating the exact date when we start to plan
    planning_time_delta = datetime.timedelta(days=int(planning_days))
    aiming_date = next_birth - planning_time_delta
    print(f"The planned date for the next birthday is {aiming_date}.")

    # Calculating the week_day then find next Saturday named aiming_date
    week_day = aiming_date.isoweekday()
    revise_number = week_day - 6
    aiming_saturday = aiming_date

    date1 = aiming_date.replace(month=5, day=1)
    date2 = aiming_date.replace(month=5, day=3)
    date3 = aiming_date.replace(month=10, day=1)
    date4 = aiming_date.replace(month=10, day=7)

    if date1 <= aiming_date <= date2:
        aiming_saturday = aiming_date - datetime.timedelta(days=0)
    elif date3 <= aiming_date <= date4:
        aiming_saturday = aiming_date - datetime.timedelta(days=0)
    elif week_day == 6 or week_day == 7:
        aiming_saturday = aiming_date - datetime.timedelta(days=0)
    elif week_day == 1 or week_day == 2:
        aiming_saturday = aiming_date - datetime.timedelta(days=week_day+1)
    elif week_day == 3 or week_day == 4 or week_day == 5:
        aiming_saturday = aiming_date - datetime.timedelta(days=revise_number)

    # print(f">>>The aiming_date is a {aiming_saturday}\n")
    # print(f">>>The revise_delta is a {revise_delta}\n")

    # In order to minus the using of global variables, call outcome here.
    # 应分项显示：下次生日日期、下次生日距离今天的天数、距离下次生日前n天的日期、预计准备制定生日计划的日期
    outcome(next_birth, distance_days, aiming_date, aiming_saturday)
    final_outcome(next_birth, distance_days, aiming_date, aiming_saturday)
    # print(">>> end calculation\n")


def outcome(next_birth, distance_days, aiming_date, aiming_saturday):
    print(f"The date of {person.name}'s next birthday is {next_birth}.\n")
    print(f"From today to this date, there are still {distance_days} days.\n")
    print(f"And as you want to plan the party {planning_days} days in advance,"
          f"we find {aiming_date} is exactly the date you need.")
    print(f"Since you may want to find a Saturday or Sunday to start planning, we recommend {aiming_saturday} as the proper day.\n")


def remind(aiming_saturday):
    print(f"Thanks for using this program\n")
    print(f"The date to make your birthday plans is {aiming_saturday}")


def find_nth_(string, n):
    """
    找到字符串中的第 n 个 ' '
    这里假定 n 从 1 开始

    如果存在第 n 个 ' '，返回索引，否则返回 -1
    """
    indexes = (idx for idx, char in enumerate(string) if char == " ")
    target_index = -1
    for _ in range(n):
        target_index = next(indexes, -1)

    return target_index


def final_outcome(next_birth, distance_days, aiming_date, aiming_saturday):
    text1 = f"The date of {person.name}'s next birthday is {next_birth}.\n"
    text2 = f"From today to this date, there are still {distance_days} days.\n"
    text3 = f"And as you want to plan the party {planning_days} days in advance,"
    text4 = f"we find {aiming_date} is exactly the date you need."
    text5 = f"Since you may want to find a Saturday or Sunday to start planning, we recommend {aiming_saturday} as the proper day.\n"

    root = Tk()
    frm = ttk.Frame(root, padding=100)
    frm.grid()
    ttk.Label(frm, text=text1).grid(column=0, row=0)
    ttk.Label(frm, text=text2).grid(column=0, row=1)
    ttk.Label(frm, text=text3).grid(column=0, row=2)
    ttk.Label(frm, text=text4).grid(column=0, row=3)
    ttk.Label(frm, text=text5).grid(column=0, row=4)

    ttk.Button(frm, text="Quit", command=root.deiconify()).grid(column=0, row=5)
    root.mainloop()


def main():
    welcome()
    insert()
    enter_info()
    while 1:
        calculation()
        flag_n = False
        print(f"Whether the plan needs to be reinvented(y/n)\n")
        while 1:
            flag_reinvent = input()
            if flag_reinvent == 'y':
                break
            elif flag_reinvent == 'n':
                flag_n = True
                break
            else:
                print(f"The word entered is wrong, please enter again\n")
        if flag_n:
            break
    # outcome has been called in the end of calculation()
    remind(aiming_saturday)




main()