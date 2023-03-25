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

def bubbleButton(presentFrame, bubbleFrame):
    def show_calculatorFrame():
        bubbleFrame.tkraise()

    bubbleButton = customtkinter.CTkButton(
        presentFrame,
        width=300,
        height=100,
        font=(tuple, 30),
        text="Bubble Sort",
        command=lambda: show_calculatorFrame()
    )

    bubbleButton.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)