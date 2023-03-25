import customtkinter
import tkinter
from Functions.calculatorFunctions import add, subtract, multiply, divide

# =========================== #
# ####### Calculator ######## #
# =========================== #

def showCalculator(calculatorFrame):
    # Operation selected label
    def operator_label(choice):
        operationLabel.configure(text=f"{choice}")

    # Equation calculation
    def calculate():
        x = int(firstEntry.get())
        y = int(secondEntry.get())
        choice = operatorChoice.get()
        result = "0"

        if (y == 0) and (choice == '÷'):
            resultLabel.configure(text=result)

        else:
            operator = {
                '+': add,
                '-': subtract,
                'x': multiply,
                '÷': divide,
            }

            if choice in operator:
                result = str(operator[choice](x, y))
                resultLabel.configure(text=result)

    # =========================== #
    # ########## Style ########## #
    # =========================== #

    # Calculator buttons
    resultLabel = customtkinter.CTkLabel(
        calculatorFrame,
        font=(tuple, 60),
        text="0"
    )
    firstEntry = customtkinter.CTkEntry(
        calculatorFrame,
        placeholder_text="",
        width=120,
        height=60,
        font=(tuple, 20),
        border_width=1,
        corner_radius=5
    )
    secondEntry = customtkinter.CTkEntry(
        calculatorFrame,
        placeholder_text="",
        width=120,
        height=60,
        font=(tuple, 20),
        border_width=1,
        corner_radius=5
    )
    operationLabel = customtkinter.CTkLabel(
        calculatorFrame,
        font=(tuple, 40),
        text="+"
    )
    operatorChoice = customtkinter.CTkOptionMenu(
        calculatorFrame,
        width=125,
        height=60,
        font=(tuple, 40),
        values=["+", "-", "x", "÷"],
        command=operator_label
    )
    calculateButton = customtkinter.CTkButton(
        calculatorFrame,
        width=120,
        height=60,
        font=(tuple, 20),
        text="Calculate",
        command=calculate
    )

    # Dropdown default value
    operatorChoice.set("+")

    # Placement
    resultLabel.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
    firstEntry.place(relx=0.3, rely=0.45, anchor=tkinter.CENTER)
    secondEntry.place(relx=0.7, rely=0.45, anchor=tkinter.CENTER)
    operationLabel.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
    operatorChoice.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER)
    calculateButton.place(relx=0.7, rely=0.6, anchor=tkinter.CENTER)
