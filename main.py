import tkinter as tk
#from tkinter import ttk
from tkinter.font import Font

s = tk.Tk()
s.title("Pages test")
s.geometry("300x300")
#s.grid_rowconfigure(0, weight=1)
s.grid_columnconfigure(0, weight=1)
s.option_add("*Font", ("Arial", 14))



def showPage(prev, next):
    prev.grid_forget()
    next.grid()

def showMain(): 
    page1.grid_forget()
    mainPage.grid()
def showPage1():
    mainPage.grid_forget()
    page1.grid()




# Page 1
page1 = tk.Frame(s)
page1.grid()
page1.grid_forget()

label = tk.Label(page1, text="Page 1")
label.grid()
button = tk.Button(page1, text="Go back", bg="red", command=lambda:showPage(page1, mainPage))
button.grid()



# Page 2
page2 = tk.Frame(s)
page2.grid()
page2.grid_forget()

label = tk.Label(page2, text="Page 2")
label.grid()
button = tk.Button(page2, text="Go back", bg="red", command=lambda:showPage(page2, mainPage))
button.grid()



# Page 3
page3 = tk.Frame(s)
page3.grid()
page3.grid_forget()

label = tk.Label(page3, text="Page 3")
label.grid()
button = tk.Button(page3, text="Go back", bg="red", command=lambda:showPage(page3, mainPage))
button.grid()



# Main page
mainPage = tk.Frame(s)
mainPage.grid()

label = tk.Label(mainPage, text="Main page")
label.grid(row = 0, column = 0, columnspan=3)

button = tk.Button(mainPage, text="Page 1", bg="blue", command=lambda:showPage(mainPage, page1))
button.grid(row = 1, column = 0)
button2 = tk.Button(mainPage, text="Page 2", bg="green", command=lambda:showPage(mainPage, page2))
button2.grid(row = 1, column = 1)
button3 = tk.Button(mainPage, text="Page 3", bg="yellow", command=lambda:showPage(mainPage, page3))
button3.grid(row = 1, column = 2)




s.mainloop()