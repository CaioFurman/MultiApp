import tkinter
import customtkinter
import counterFunctions
from calculatorFunctions import add, subtract, multiply, divide

# Tried to short and improve the code quality using loops to create the CustomTkinter buttons
# But because the button creation and placement are two separate things I didn't find a way to fix it

#================== App Setup
# Basic settings for the app
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
    command=lambda:app.destroy()
)


# Placement
counterButton.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
calculatorButton.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
closeButton.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)


#================== Counter
# Code for the counter and frame appearance.

# Button Functions
def incrementButton():
    clickCounterLabel.configure(text=f"{counterFunctions.increment_count()}")

def decrementButton():
    clickCounterLabel.configure(text=f"{counterFunctions.decrement_count()}")

def clearButton():
    clickCounterLabel.configure(text=f"{counterFunctions.clear_count()}")

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
    command=incrementButton
)

decrementButton = customtkinter.CTkButton(
    clickCounter,
    width=100,
    height=60,
    font=(tuple, 20),
    text="Subtract",
    command=decrementButton
)

clearButton = customtkinter.CTkButton(
    clickCounter,
    width=100,
    height=60,
    font=(tuple, 20),
    text="Clear",
    command=clearButton
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


#================== Calculator
# Code for the calculator and frame appearance.

# Result Functions
def operatorLabel(choice):
    operationLabel.configure(text=f"{choice}")

def calculate():
    x = int(firstEntry.get())
    y = int(secondEntry.get())
    choice = operatorChoice.get()
    result = "0"

    if (choice == '+'):
        result = str(add(x, y))
        resultEntry.configure(placeholder_text = result)
        print(f'{x} {choice} {y} = {result}')

    elif (choice == '-'):
        result = str(subtract(x, y))
        resultEntry.configure(placeholder_text=result)
        print(f'{x} {choice} {y} = {result}')

    elif (choice == 'x'):
        result = str(multiply(x, y))
        resultEntry.configure(placeholder_text=result)
        print(f'{x} {choice} {y} = {result}')

    elif (choice == '÷'):
        if(y == 0):
            resultEntry.configure(placeholder_text='0')

        else:
            result = str(divide(x, y))
            resultEntry.configure(placeholder_text=result)
            print(f'{x} {choice} {y} = {result}')

    else:
        print('error')


# Components
resultEntry = customtkinter.CTkEntry(
    calculator,
    width=330,
    height=100,
    placeholder_text='Result',
    font=(tuple,40),
    border_width=1,
    corner_radius=5
    # status = 'readonly'
    # customtkinter doesn't allow you to change the value so read-only breaks the result screen
    # resultEntry.set("value") also doesn't work.
)

firstEntry = customtkinter.CTkEntry(
    calculator,
    placeholder_text="",
    width=120,
    height=60,
    font=(tuple,20),
    border_width=1,
    corner_radius=5
)

secondEntry = customtkinter.CTkEntry(
    calculator,
    placeholder_text="",
    width=120,
    height=60,
    font=(tuple,20),
    border_width=1,
    corner_radius=5
)

operationLabel = customtkinter.CTkLabel(
    calculator,
    font=(tuple, 40),
    text="+"
)

operatorChoice = customtkinter.CTkOptionMenu(
    calculator,
    width=125,
    height=60,
    font=(tuple, 40),
    values=["+", "-", "x", "÷"],
    command=operatorLabel
)
operatorChoice.set("+")

calculateButton = customtkinter.CTkButton(
    calculator,
    width=120,
    height=60,
    font=(tuple, 20),
    text="Calculate",
    command=calculate
)

homeButtonC = customtkinter.CTkButton(
    calculator,
    width=330,
    height=60,
    font=(tuple, 20),
    text="Return to Home",
    command=lambda:show_frame(home)
)


#Placement
resultEntry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
firstEntry.place(relx=0.3, rely=0.45, anchor=tkinter.CENTER)
secondEntry.place(relx=0.7, rely=0.45, anchor=tkinter.CENTER)
operationLabel.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
operatorChoice.place(relx=0.3, rely=0.65, anchor=tkinter.CENTER)
calculateButton.place(relx=0.7, rely=0.65, anchor=tkinter.CENTER)
homeButtonC.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

app.mainloop()