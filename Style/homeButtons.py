import customtkinter
import tkinter

def counterButton(presentFrame, counterFrame):
    def show_counterFrame():
        counterFrame.tkraise()

    counterButton = customtkinter.CTkButton(
        presentFrame,
        text="Counter",
        width=300,
        height=100,
        font=(tuple, 30),
        command=lambda: show_counterFrame()
    )

    counterButton.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

def calculatorButton(presentFrame, calculatorFrame):
    def show_calculatorFrame():
        calculatorFrame.tkraise()

    calculatorButton = customtkinter.CTkButton(
        presentFrame,
        width=300,
        height=100,
        font=(tuple, 30),
        text="Calculator",
        command=lambda: show_calculatorFrame()
    )

    calculatorButton.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def exitButton(presentFrame, app):
    exitButton = customtkinter.CTkButton(
        presentFrame,
        width=300,
        height=100,
        font=(tuple, 30),
        text="Close",
        command=lambda: app.destroy()
    )

    exitButton.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)