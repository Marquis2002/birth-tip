
import datetime
from dateutil import parser
from tkinter import *
from tkinter import messagebox

# date = datetime.date.today()
planning_days = 0

distance = 0


class Person(object):
    def __init__(self, name, rel, birthday):
        self.name = name
        self.rel = rel
        self.birthday = birthday


person = Person('', '', '')


def form1():  # 第1个窗体：登录窗体
    def ok():
        root1.destroy()
        form_ini()
    root1 = Tk()
    root1.title('登录窗口')
    root1.geometry('400x250+550+250')
    la0 = Label(root1, text='欢迎使用生日计划便签')
    la0.pack()
    but1 = Button(root1, text=" 按此处以继续 ", command=ok)
    but1.pack(pady=5)
    but2 = Button(root1, text=" 退 出 ", command=root1.destroy)
    but2.pack(pady=5)

    root1.mainloop()


def form_ini():

    def ok1():
        with open("members_gui.txt", "w") as inif:
            pass
        with open("members_gui_plan.txt", "w") as inifp:
            pass
        root_ini.destroy()

    def ok2():
        with open("members_gui_plan.txt", "w") as inifp:
            pass
        root_ini.destroy()

    root_ini = Tk()
    root_ini.title('初始化信息')
    root_ini.geometry('400x250+550+250')
    la0 = Label(root_ini, text='是否需要初始化成员信息')
    la0.pack()
    but1 = Button(root_ini, text=" 初始化所有信息 ", command=ok1)
    but1.pack(pady=5)
    but2 = Button(root_ini, text=" 仅初始化生日计划信息 ", command=ok2)
    but2.pack(pady=5)
    but3 = Button(root_ini, text=" 否 ", command=root_ini.destroy)
    but3.pack(pady=5)

    root_ini.mainloop()
    form2()


def form2():  # 第2个窗体:添加成员确认
    def ok():
        root2.destroy()
        form3()
    root2 = Tk()
    root2.title('添加成员信息确认')
    root2.geometry('400x250+550+250')
    la0 = Label(root2, text='是否需要添加新成员')
    la0.pack()
    but1 = Button(root2, text=" 是 ", command=form_inf)
    but1.pack(pady=5)
    but2 = Button(root2, text=" 否 ", command=ok)
    but2.pack(pady=5)
    root2.mainloop()


def form_inf():  # 第2.1个窗体:添加成员
    def ok():
        flag_ins = True
        try:
            birth_try = datetime.datetime.strptime(birth.get(), "%Y.%m.%d")
        except ValueError:
            print("The date format is incorrect, please enter again")
            flag_ins = False
            form_err()

        if flag_ins:
            with open("members_gui.txt", "a") as f:
                f.write(name.get())
                f.write(" _")
                f.write(rel.get())
                f.write(" _")
                f.write(birth.get())
                f.write("\n")
        root_inf.destroy()

    root_inf = Tk()
    root_inf.title('添加成员信息')
    root_inf.geometry('400x250+550+250')
    la0 = Label(root_inf, text='姓名：')
    la0.pack()
    name = Entry(root_inf)
    name.pack()
    la1 = Label(root_inf, text='关系：')
    la1.pack()
    rel = Entry(root_inf)
    rel.pack()
    la2 = Label(root_inf, text='生日：(eg.1999.12.13)')
    la2.pack()
    birth = Entry(root_inf)
    birth.pack()

    but1 = Button(root_inf, text=" 确定 ", command=ok)
    but1.pack(pady=5)

    root_inf.mainloop()
    la0 = Label(root_inf, text='姓名：')
    la0.pack()


def form_err():
    root_err = Tk()
    root_err.title('警告')
    root_err.geometry('400x250+550+250')
    la0 = Label(root_err, text='输入有误！')
    la0.pack()
    but1 = Button(root_err, text=" 确定 ", command=root_err.destroy)
    but1.pack(pady=5)


def form3():  # 第3个窗体:输出members信息
    global person

    def ok():
        f2 = open("members_gui.txt", "r")
        lines = f2.readlines()
        name = name_en.get()
        name_find = name + " _"
        flag_find = False
        for line in lines:
            if line.find(name_find) != -1:
                flag_find = True
        if flag_find:
            for line in lines:
                if line.find(name) != -1:
                    birthday = line[find_nth_(line, 2) + 1:]
                    birthday = birthday.strip('\n')
                    relation = line[find_nth_(line, 1) + 1:find_nth_(line, 2)]
                    relation = relation.strip('\n')
            person = Person(name, relation, birthday)
            root3.destroy()
            form4(person)
        else:
            form_err()

    global date
    root3 = Tk()
    root3.title('成员信息')
    root3.geometry('400x250+550+250')
    la0 = Label(root3, text='成员信息：')
    la0.pack()
    information = ''
    with open("members_gui.txt", "r") as f1:
        for line in f1.readlines():
            information += line

    la1 = Label(root3, text=information)
    la1.pack()
    la2 = Label(root3, text='请选择为谁进行生日计划：')
    la2.pack()

    name_en = Entry(root3)
    name_en.pack()

    but1 = Button(root3, text=" 确定 ", command=ok)
    but1.pack(pady=5)
    # but2 = Button(root3, text=" 否 ", command=root3.destroy)
    # but2.pack(pady=5)

    root3.mainloop()


def form4(person):  # 输入今天日期以及需要提前的时间
    # global distance_days
    # global next_birth

    def ok():
        flag_ins = True
        date = today.get()
        planning_days = adv_day.get()
        date1 = parser.parse(date).date()
        calculation(person, date1, planning_days)
        try:
            birth_try = datetime.datetime.strptime(date, "%Y.%m.%d")
        except ValueError:
            print("The date format is incorrect, please enter again")
            flag_ins = False
            form_err()

        if int(planning_days) < 0 or int(planning_days) > distance_days:
            print("The number entered is wrong, please enter again\n")
            flag_ins = False
            form4_1(distance_days)

        if flag_ins:
            txt_change(aiming_saturday, person)
            root4.destroy()
            form5(distance_days, aiming_date, aiming_saturday, person)

    root4 = Tk()
    root4.title('制定日期')
    root4.geometry('400x250+550+250')
    la0 = Label(root4, text='请输入今天的日期：(eg.1999.1.1)')
    la0.pack()
    today = Entry(root4)
    today.pack()
    la1 = Label(root4, text='需要提前多少天：')
    la1.pack()
    adv_day = Entry(root4)
    adv_day.pack()

    but1 = Button(root4, text=" 确定 ", command=ok)
    but1.pack(pady=5)

    root4.mainloop()


def form4_1(distance):
    root_err = Tk()
    root_err.title('警告')
    root_err.geometry('400x250+550+250')
    la0 = Label(root_err, text='输入有误！')
    la0.pack()
    text = "离下次生日还有" + str(distance) + "天"
    la0 = Label(root_err, text=text)
    la0.pack()
    but1 = Button(root_err, text=" 确定 ", command=root_err.destroy)
    but1.pack(pady=5)


def form5(distance_days, aiming_date, aiming_saturday, person):   # 结果显示
    def ok():
        root5.destroy()
        form6()

    root5 = Tk()
    root5.title('结果显示')
    root5.geometry('400x250+550+250')
    la0 = Label(root5, text='结果显示：')
    la0.pack()
    text1 = "姓名：" + str(person.name) + " 关系：" + str(person.rel) + " 生日：" + str(person.birthday)
    la1 = Label(root5, text=text1)
    la1.pack()
    la2 = Label(root5, text='生日计划信息：')
    la2.pack()
    text3 = "下次生日距离今天：" + str(distance_days) + "天"
    la3 = Label(root5, text=text3)
    la3.pack()
    text4 = "原预定计划日期：" + str(aiming_date)
    la4 = Label(root5, text=text4)
    la4.pack()
    text5 = "改进制定计划日期：" + str(aiming_saturday)
    la4 = Label(root5, text=text5)
    la4.pack()
    but1 = Button(root5, text=" 确定 ", command=ok)
    but1.pack(pady=5)
    root5.mainloop()


def form6():   # 最终结果
    root6 = Tk()
    root6.title('结果显示')
    root6.geometry('400x250+550+250')
    information = ''
    with open("members_gui_plan.txt", 'r') as fp:
        for line in fp.readlines():
            information += line
    la0 = Label(root6, text="成员信息（‘~’后代表生日计划日期）")
    la0.pack()
    la1 = Label(root6, text=information)
    la1.pack()

    but1 = Button(root6, text=" 感谢使用生日计划便签 ", command=root6.destroy)
    but1.pack(pady=5)
    root6.mainloop()


def find_nth_(string, n):  # 功能函数，找到字符串内第n个_字符
    indexes = (idx for idx, char in enumerate(string) if char == "_")
    target_index = -1
    for _ in range(n):
        target_index = next(indexes, -1)

    return target_index


def txt_change(aiming_saturday, person):  # 更改txt文档
    ff = open('members_gui_plan.txt', 'w')  # 打开plan文件，可写模式
    with open('members_gui.txt', 'r') as f:  # 打开原文件只读模式
        lines = f.readlines()
        i = 0
        for line_list in lines:
            if line_list.find(person.name) != -1:
                if line_list.find('~') != -1:
                    line_new = line_list[1:line_list.find('~')] + str(aiming_saturday) + '\n'
                else:
                    line_new = line_list.replace('\n', ' ~')  # 将换行符替换为空('')
                    line_new = line_new + str(aiming_saturday) + '\n'
            else:
                line_new = line_list
            ff.write(line_new)  # 写入一个新文件中


def calculation(person, date, planning_days):
    global distance_days
    global aiming_date
    global aiming_saturday
    global flag_ex

    to_date = date
    # At the very beginning, resolve the person's information.
    birth_date = parser.parse(person.birthday)
    flag_ex = True

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

    # print(f"The next birthday date is {next_birth}.")
    # print(f"Today is {distance_days} days until the next birthday.")
    #
    # print(f"\tHow many days do you want to cost planning the party in advance?\nPlease enter here\n")
    # while 1:
    #     planning_days = input("planning_days > ")
    #     if int(planning_days) < 0:
    #         print("The number entered is wrong, please enter again\n")
    #     elif int(planning_days) > distance_days:
    #         print(f"The time entered is longer than the time interval, please enter again\n")
    #     else:
    #         break

    # Now calculating the exact date when we start to plan
    planning_time_delta = datetime.timedelta(days=int(planning_days))
    aiming_date = next_birth - planning_time_delta
    # print(f"The planned date for the next birthday is {aiming_date}.")

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
        flag_ex = False
    elif week_day == 1 or week_day == 2:
        aiming_saturday = aiming_date - datetime.timedelta(days=week_day+1)
    elif week_day == 3 or week_day == 4 or week_day == 5:
        aiming_saturday = aiming_date - datetime.timedelta(days=revise_number)

    # with open("members.txt", "a") as f:
    #     f.write(f"aiming Saturday is : {aiming_saturday}")
    #     f.write("\n")



form1()