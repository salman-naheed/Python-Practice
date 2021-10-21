input_year = int(input(" Enter the year:"))


def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and 100 != 0):
        return 1
    else:
        return 0


if is_leap(input_year):
    print("is a leap year")
else:
    print("it is not a leap year")


def month():
    month = int(input("Enter your number :"))
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("month%d" % month + "has 31 days")
    elif month == 2:
        if is_leap(input_year):
            print(f'month {month} has 29 days')
        else:
            print(f'month {month} has 28 days')
    else:
        print("month%d" % month + "has 30 days")


month()

def month_name(months):
    name=["january","February","March","April","May","June","July","August","September","October","November","December"]
    print(name[months-1])
    return(name[months-1])

