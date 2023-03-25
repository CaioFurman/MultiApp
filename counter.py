import customtkinter
import tkinter
from Components.counterButtons import incrementButton, decrementButton, clearButton
from Components.returnButton import returnButton
from Functions.counterFunctions import increment_count, decrement_count, clear_count

# =========================== #
# ######### Counter ######### #
# =========================== #
def showCounter(counterFrame):

    # Modification of the counter values
    def incrementFunction():
        clickCounterLabel.configure(text=f"{increment_count()}")

    def decrementFunction():
        clickCounterLabel.configure(text=f"{decrement_count()}")

    def clearFunction():
        clickCounterLabel.configure(text=f"{clear_count()}")

    # Counter label
    clickCounterLabel = customtkinter.CTkLabel(
        counterFrame,
        font=(tuple, 40),
        text='Try adding or subtracting!'
    )
    clickCounterLabel.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # Counter buttons
    incrementButton(counterFrame, incrementFunction)
    decrementButton(counterFrame, decrementFunction)
    clearButton(counterFrame, clearFunction)
