import customtkinter
import random
from Style.homeButtons import counterButton, calculatorButton, bubbleButton
from Style.returnButton import returnButton
from counter import showCounter
from calculator import showCalculator
from bubble_sort import showBubble

# =========================== #
# ######## App Setup ######## #
# =========================== #
# Basic settings for the app
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("500x500")
app.title("Python-based App")
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

home = customtkinter.CTkFrame(app)
clickCounter = customtkinter.CTkFrame(app)
calculator = customtkinter.CTkFrame(app)
bubble = customtkinter.CTkFrame(app)

for frame in (home, clickCounter, calculator, bubble):
    frame.grid(row=0, column=0, sticky='nsew')


# =========================== #
# ########## Home ########### #
# =========================== #
home.tkraise()

# Home frame selection buttons
counterButton(home, clickCounter)
calculatorButton(home, calculator)
bubbleButton(home, bubble)

# =========================== #
# ######### Counter ######### #
# =========================== #

showCounter(clickCounter)
returnButton(clickCounter, home)

# =========================== #
# ####### Calculator ######## #
# =========================== #

showCalculator(calculator)
returnButton(calculator, home)

# =========================== #
# ####### Bubble Sort ####### #
# =========================== #

showBubble(bubble)
returnButton(bubble, home)

app.mainloop()
