import tkinter
import customtkinter
from Components.homeButtons import counterButton, calculatorButton, exitButton
from Components.counterButtons import incrementButton, decrementButton, clearButton
from Components.returnButton import returnButton
from Functions.counterFunctions import increment_count, decrement_count, clear_count
from Functions.calculatorFunctions import add, subtract, multiply, divide

# Tried to short and improve the code quality using loops to create the CustomTkinter buttons
# But because the button creation and placement are two separate things I didn't find a way to fix it

# =========================== #
# ######## App Setup ######## #
# =========================== #
# Basic settings for the app
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

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
def show_frame(frame):
    frame.tkraise()


# =========================== #
# ########## Home ########### #
# =========================== #
show_frame(home)


# Home buttons
counterButton(home, clickCounter)
calculatorButton(home, calculator)
exitButton(home, app)


# =========================== #
# ######### Counter ######### #
# =========================== #
clickAmount = 0


# Modification of the counter values
def incrementFunction():
    clickCounterLabel.configure(text=f"{increment_count()}")

def decrementFunction():
    clickCounterLabel.configure(text=f"{decrement_count()}")

def clearFunction():
    clickCounterLabel.configure(text=f"{clear_count()}")

# Counter
clickCounterLabel = customtkinter.CTkLabel(
    clickCounter,
    font=(tuple, 40),
    text='Try adding or subtracting!'
)
clickCounterLabel.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# Counter buttons
incrementButton(clickCounter, incrementFunction)
decrementButton(clickCounter, decrementFunction)
clearButton(clickCounter, clearFunction)


# Return button
returnButton(clickCounter, home)



# =========================== #
# ####### Calculator ######## #
# =========================== #


# Operation choice
def operatorLabel(choice):
    operationLabel.configure(text=f"{choice}")


# Equation calculation
def calculate():
    x = int(firstEntry.get())
    y = int(secondEntry.get())
    choice = operatorChoice.get()
    result = "0"

    if (y == 0) and (choice == '÷'):
        resultEntry.configure(placeholder_text=result)

    else:
        operator = {
            '+': add,
            '-': subtract,
            'x': multiply,
            '÷': divide,
        }

        if choice in operator:
            result = str(operator[choice](x, y))
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
    # status='readonly'
    # customtkinter doesn't allow you to change the value so read-only breaks the result screen
    # because resultEntry.set(value) doesn't work.
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

calculateButton = customtkinter.CTkButton(
    calculator,
    width=120,
    height=60,
    font=(tuple, 20),
    text="Calculate",
    command=calculate
)


# Return button
returnButton(calculator, home)


# Dropdown default value
operatorChoice.set("+")


# Placement
resultEntry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
firstEntry.place(relx=0.3, rely=0.45, anchor=tkinter.CENTER)
secondEntry.place(relx=0.7, rely=0.45, anchor=tkinter.CENTER)
operationLabel.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
operatorChoice.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER)
calculateButton.place(relx=0.7, rely=0.6, anchor=tkinter.CENTER)

app.mainloop()