import string
import datetime
from dateutil import parser


# Input Parameters
date = datetime.date.today()
planning_days = 0
# date_str1 = "2002.12.26"
# date1 = parser.parse(date_str1)


print(f">>>>>date is: {date}")


class Person(object):
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday


# Mediate Parameters
distance = 0


# Outcome Parameters


# Down from here, five functions are created by step.
def welcome():
    print("Welcome to the birthday tip. \nThis program will help you ")
    input("Enter anything to go on\n> ")


def enter_info():
    global person
    global date
    global planning_days
    print("\tPlease enter your friend's name and birthday.\n")
    name = input("name > ")
    birthday = input("birthday > ")
    person = Person(name, birthday)
    print(f"\tHow many days do you want to cost planning the party in advance?\nPlease enter here\n")
    planning_days = input("planning_days > ")


def calculation():
    # At the very beginning, resolve the person's information.
    print(f"{person.name}'s birthday is {person.birthday}")
    birth_date = parser.parse(person.birthday)
    flag = input("Enter 'y' if you want to use the date today.\n>  ")
    if flag == 'y':
        to_date = datetime.date.today()
    elif flag == 'n':
        print("n has been entered.\n")
    else:
        pass

    # Getting the nearest birthday named this_birth
    # Then calculate the days between those two dates
    # After that, decide which the next birth
    to_year = to_date.year
    this_birth = birth_date.replace(year=to_year).date()
    distance_1 = this_birth - to_date
    distance_days = distance_1.days

    if distance_days > 0:
        next_birth = this_birth
    elif distance_days <= 0:
        next_birth = this_birth.replace(year=to_year + 1)
    else:
        pass

    distance_1 = next_birth - to_date
    distance_days = distance_1.days
    # print(f">>>distance_days is :{distance_days}")

    # Now calculating the exact date when we start to plan
    planning_time_delta = datetime.timedelta(days=int(planning_days))
    aiming_date = next_birth - planning_time_delta

    # Calculating the week_day then find next Saturday named aiming_date
    week_day = aiming_date.isoweekday()
    revise_number = week_day - 6
    if week_day == 6 or week_day == 7:
        revise_delta = datetime.timedelta(days=0)
    elif week_day == 1 or week_day == 2:
        revise_delta = datetime.timedelta(days=week_day+1)
    elif week_day == 3 or week_day == 4 or week_day == 5:
        revise_delta = datetime.timedelta(days=revise_number)

    aiming_saturday = aiming_date - revise_delta

    # print(f">>>The aiming_date is a {aiming_saturday.isoweekday()}\n")

    # In order to minus the using of global variables, call outcome here.
    # 应分项显示：下次生日日期、下次生日距离今天的天数、距离下次生日前n天的日期、预计准备制定生日计划的日期
    outcome(next_birth, distance_days, aiming_date, aiming_saturday)
    # print(">>> end calculation\n")

def outcome(next_birth, distance_days, aiming_date, aiming_saturday):
    print(f"The date of {person.name}'s next birthday is {next_birth}.\n")
    print(f"From today to this date, there are still {distance_days} days.\n")
    print(f"And as you want to plan the party {planning_days} days in advance,"
          f"we find {aiming_date} is exactly the date you need.")
    print(f"Since you may want to find a Saturday to start planning, we recommend {aiming_saturday} as the proper day.")

def remind():
    pass


def main():
    welcome()
    enter_info()
    calculation()
    # outcome has been called in the end of calculation()
    remind()


main()