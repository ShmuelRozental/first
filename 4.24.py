import calendar
#ask date from the user
date = input("enter deta")
#create a loop to get correct date whit six numbers
while len(date) < 8:
    print("please enter date whit 6 numbers! for example(01/01/2023)")
    date = input("enter deta")
# Extract day, month, and year from the entered date
days= int(date[0:2])
months = int(date[3:5])
years = int(date[6:])
#Uses the calendar function
day_of_week = calendar.weekday(years, months, days)
#Creating a list of the days of the week according to the order of the function.
#Converts the function output from a number/ to a day of the week
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"The day of the week for {date} is {day_names[day_of_week]}.")