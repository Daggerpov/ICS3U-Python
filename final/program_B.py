#The items I've completed are: i, ii, iii, iv, v, vii, viii

import datetime as dt 

class Error(Exception):
    #base for other custom error classes
    pass

class NegativeValueError(Error):
    #raised when value entered is < 0
    pass

class MonthRangeError(Error):
    #raised when value is out of range
    pass

class DayRangeError(Error):
    #raised when day is out of range for its month
    #could also depend on year if it's February
    pass 

class YearRangeError(Error):
    #raised when year is out of range (hasn't happened
    #yet or is below 0)
    pass

#ii
def check_year():
    while True:
        try:
            year = int(input("Enter the year: "))

            if year < 0 or year > dt.date.today().year:
                raise YearRangeError 
            
            break
        
        except YearRangeError:
            print("Either the year has not occured yet or is below 0, please try again.")
            print()
        except ValueError:
            print("Input is not of type int, please try again.")
            print()
    return year

def check_month():
    while True:
        try:
            month = int(input("Enter the month number: "))

            if month < 1 or month > 12:
                raise MonthRangeError        
            
            break

        except MonthRangeError:
            print("Not a valid month number, since it's out of range (1-12)")
            print()
        except ValueError:
            print("Input is not of type int, please try again.")
            print()

    return month

def check_day():
    while True:
        try:
            day = int(input("Enter the month's day number: "))

            #month has 30 days if not February
            if (month % 2 == 0 and month != 2) and (day < 1 or day > 30):
                raise DayRangeError

            #month has 31 days
            elif (month % 2 == 0) and (day < 1 or day > 31):
                raise DayRangeError

            elif (month == 2) and (leap == True) and (day < 1 or day > 29):
                raise DayRangeError 

            elif (month == 2) and (leap == False) and (day < 1 or day > 28):
                raise DayRangeError
        
            break
                    
        except DayRangeError:
            print("Not a valid day number for its month during that year.")
            print()
        except ValueError:
            print("Input is not of type int, please try again.")
            print()
        
    return day

stored_dates = {}
stop = 'N'

while stop.lower() == 'n':
    #iv
    storing = input("Would you like to store a date? (Y/N) ")
    if storing.lower() == 'y':
        year = check_year()
        
        #i
        if year % 4 == 0:
            print("That year is a leap year.")
            leap = True
        else:
            print("That year is not a leap year.")
            leap = False

        month = check_month()
        day = check_day()
        #iii
        date = dt.datetime(year, month, day)
        spelled_date = date.strftime("%B %d, %Y")
        
        #viii
        days_of_week = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
        day_of_week = (list(days_of_week.keys())[list(days_of_week.values()).index(date.weekday())])
        print(f"\nThat date is {spelled_date} and was on a {day_of_week}.")
        
        #vii
        current_date = dt.date.today()
        diff_years = current_date.year - int(date.strftime("%Y"))
        diff_months = current_date.month - int(date.strftime("%m"))
        diff_days = current_date.day - int(date.strftime("%d"))
        print(f"\nThat date was {diff_years} years {diff_months} months, and {diff_days} days ago.")

        name = input("What would you like to name this date? ")

        stored_dates[name] = date
    
    
    #v
    searching = input("Would you like to search for a stored date? (Y/N) ")
    if searching.lower() == 'y':
        searched_date = input("Enter the name of the stored date: ")
        spelled_date = stored_dates[searched_date].strftime("%B %d, %Y")
        print(f"That date is: {spelled_date}")
    
    stop = input("Would you like to quit the program? (Y/N) ")









