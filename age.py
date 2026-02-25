# Import required libraries to build the GUI and get the current system's date.
import datetime as dt
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


# Get the current date (Day - Month - Year).
currentDate = str(dt.date.today()).split("-")
currentDay = int(currentDate[2])
currentMonth = int(currentDate[1])
currentYear = int(currentDate[0])



# Prepare valid inputs for the drop-down lists.
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
months = [1,2,3,4,5,6,7,8,9,10,11,12]
years = []
counter = 1900
while counter != currentYear + 1:   # A while-loop to prepare the years for the drop-down list (I am NOT typing out 100+ years by hand).
    years.append(counter)
    counter += 1



# Function to calculate the user's age and how many months are left till their birthday.
def setAge(birthDay, birthMonth, birthYear):
    age = currentYear - birthYear
    monthsTillBirthday = 0

    if currentMonth < birthMonth:
        age -= 1
        monthsTillBirthday = birthMonth - currentMonth
    elif currentMonth > birthMonth:
        monthsTillBirthday = 12 - birthMonth
    elif currentMonth == birthMonth and currentDay < birthDay:
        age -= 1

    # Show the calculated age and months till birthday to the user.
    ageLabel.config(text=age)
    monthsTillBirthdayLabel.config(text=monthsTillBirthday)



# Start the GUI (Show the window to the user).
root = tk.Tk()
root.title("Age Calculator")
root.columnconfigure(0, weight=1)   # Used to help center the widgest between empty columns.
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.option_add("*TCombobox*Listbox*Font", Font(family="Helvetica",size=15))   # Used to give the drop-down lists options a bigger font size.


# Show current Date to the user.
currentDateTitle = tk.Label(root, text="Current Date:", font=("", 30), pady=10)
currentDateTitle.grid(row = 0, column = 0, columnspan=3)
currentDateLabel = tk.Label(root, text=(str(currentDate[2])+"-"+str(currentDate[1])+"-"+str(currentDate[0])), font=("", 25))
currentDateLabel.grid(row = 1, column = 0, columnspan=3)



# A line to separate.
line = tk.Frame(root, height=2, bg="black")
line.grid(row=2, column=0, columnspan=3, sticky="ew", pady=(0, 35))



# Show the drop-down lists to the user.
listsTitle = tk.Label(root, text="When is your birthday?", font=("", 30), pady=10)
listsTitle.grid(row = 3, column = 0, columnspan=3)

daysTitle = tk.Label(root, text="Day:", font=("", 20), padx=5, pady=5)
daysTitle.grid(row = 4, column = 0, sticky='e')
daysDrop = ttk.Combobox(root, state="readonly", values=days, width=5, font=("", 15))
daysDrop.set(1)
daysDrop.grid(row = 4, column = 1, padx=5, pady=5)

monthsTitle = tk.Label(root, text="Month:", font=("", 20), padx=5, pady=5)
monthsTitle.grid(row = 5, column = 0, sticky='e')
monthsDrop = ttk.Combobox(root, state="readonly", values=months, width=5, font=("", 15))
monthsDrop.set(1)
monthsDrop.grid(row = 5, column = 1, padx=5, pady=5)

monthsTitle = tk.Label(root, text="Year:", font=("", 20), padx=5, pady=5)
monthsTitle.grid(row = 6, column = 0, sticky='e')
yearsDrop = ttk.Combobox(root, state="readonly", values=years, width=5, font=("", 15))
yearsDrop.set(2026)
yearsDrop.grid(row = 6, column = 1, padx=5, pady=5)



# A line to separate.
line = tk.Frame(root, height=2, bg="black")
line.grid(row=7, column=0, columnspan=3, sticky="ew", padx=30, pady=(35, 20))



# Show the resaults to the user (Empty (0) at startup).
ageTitle = tk.Label(root, text="Your age is:", font=("", 30), padx=5, pady=5)
ageTitle.grid(row = 8, column = 0)
ageLabel = tk.Label(root, text=0, font=("", 20))
ageLabel.grid(row = 8, column = 1)

monthsTillBirthdayTitle = tk.Label(root, text="Months until \n your birthday:", font=("", 20), padx=5, pady=5)
monthsTillBirthdayTitle.grid(row = 9, column = 0)
monthsTillBirthdayLabel = tk.Label(root, text=0, font=("", 15))
monthsTillBirthdayLabel.grid(row = 9, column = 1)



# Functions to change the button's background color on hover.
def enter(e):
    e.widget.config(bg='darkgray')
def leave(e):
    e.widget.config(bg='black')

# Button to call the function that calculates the user's age.
button = tk.Button(root, text="Start", font=("", 22), bg="black", fg="white", activebackground="white", cursor="hand2", command=lambda: setAge(int(daysDrop.get()), int(monthsDrop.get()), int(yearsDrop.get())))
button.bind("<Enter>", enter)
button.bind("<Leave>", leave)
button.grid(row = 8, rowspan=2, column = 2, padx=10)

root.mainloop()