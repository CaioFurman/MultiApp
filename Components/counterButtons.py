import customtkinter
import tkinter

def incrementButton(presentFrame, function):
    incrementButton = customtkinter.CTkButton(
        presentFrame,
        width=100,
        height=60,
        font=(tuple, 20),
        text="Add",
        command=function
    )

    incrementButton.place(relx=0.28, rely=0.2, anchor=tkinter.CENTER)

def decrementButton(presentFrame, function):
    decrementButton = customtkinter.CTkButton(
        presentFrame,
        width=100,
        height=60,
        font=(tuple, 20),
        text="Subtract",
        command=function
    )

    decrementButton.place(relx=0.72, rely=0.2, anchor=tkinter.CENTER)

def clearButton(presentFrame, function):
    clearButton = customtkinter.CTkButton(
        presentFrame,
        width=100,
        height=60,
        font=(tuple, 20),
        text="Clear",
        command=function
    )

    clearButton.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)