import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def show_frame(frame):
    frame.tkraise()

app = customtkinter.CTk()
app.geometry("500x500")
app.title("Python-based Calculator")
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

home = customtkinter.CTkFrame(app)
clickCounter = customtkinter.CTkFrame(app)
calculator = customtkinter.CTkFrame(app)

for frame in (home, clickCounter, calculator):
    frame.grid(row=0, column=0, sticky='nsew')

#================== Home
# Main page
show_frame(home)

# Components
counterButton = customtkinter.CTkButton(
    home,
    text="Counter",
    width=300,
    height=100,
    font=(tuple, 30),
    command=lambda:show_frame(clickCounter)
)

calculatorButton = customtkinter.CTkButton(
home,
    width=300,
    height=100,
    font=(tuple, 30),
    text="Calculator",
    command=lambda:show_frame(calculator)
)

closeButton = customtkinter.CTkButton(
    home,
    width=300,
    height=100,
    font=(tuple, 30),
    text="Close",
    command=lambda:show_frame(calculator)
)

# Placement
counterButton.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
calculatorButton.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
closeButton.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

#================== Calculator
# Code for the calculator and frame appearance.
clickAmount = 0

# Functions
def increment_count():
    global clickAmount
    clickAmount += 1
    return clickAmount

def decrement_count():
    global clickAmount
    clickAmount -= 1
    return clickAmount
def clear_count():
    global clickAmount
    clickAmount = 0
    return clickAmount

def incrementButton_function():
    clickCounterLabel.configure(text=f"{increment_count()}")

def decrementButton_function():
    clickCounterLabel.configure(text=f"{decrement_count()}")

def clearButton_function():
    clickCounterLabel.configure(text=f"{clear_count()}")

# Components
clickCounterLabel = customtkinter.CTkLabel(
    clickCounter,
    font=(tuple, 40),
    text='Try adding or subtracting!'
)

incrementButton = customtkinter.CTkButton(
    clickCounter,
    width=100,
    height=60,
    font=(tuple, 20),
    text="Add",
    command=incrementButton_function
)

decrementButton = customtkinter.CTkButton(
    clickCounter,
    width=100,
    height=60,
    font=(tuple, 20),
    text="Subtract",
    command=decrementButton_function
)

clearButton = customtkinter.CTkButton(
    clickCounter,
    width=100,
    height=60,
    font=(tuple, 20),
    text="Clear",
    command=clearButton_function
)

homeButtonCC = customtkinter.CTkButton(
    clickCounter,
    width=300,
    height=60,
    font=(tuple, 20),
    text="Return to Home",
    command=lambda:show_frame(home)
)

# Placement
clickCounterLabel.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
incrementButton.place(relx=0.28, rely=0.2, anchor=tkinter.CENTER)
decrementButton.place(relx=0.72, rely=0.2, anchor=tkinter.CENTER)
clearButton.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
homeButtonCC.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

app.mainloop()