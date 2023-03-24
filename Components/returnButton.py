import customtkinter
import tkinter

def returnButton(presentFrame, homeFrame):
    def return_home():
        homeFrame.tkraise()

    homeButton = customtkinter.CTkButton(
        presentFrame,
        width=300,
        height=60,
        font=(tuple, 20),
        text="Return to Home",
        command=lambda:return_home()
    )

    homeButton.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)