import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("425x600")

clickAmount = 0
def increment_count():
    global clickAmount
    clickAmount += 1
    return clickAmount

def button_function():
    print(f"This button has been clicked {increment_count()} times.")

button = customtkinter.CTkButton(master=app, text="Click me", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()