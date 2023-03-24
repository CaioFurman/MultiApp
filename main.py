import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def show_frame(frame):
    frame.tkraise()

app = customtkinter.CTk()
app.geometry("650x500")
app.title("Python-based Calculator")
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

home = customtkinter.CTkFrame(app)
calculator = customtkinter.CTkFrame(app)
frame3 = customtkinter.CTkFrame(app)

for frame in (home, calculator, frame3):
    frame.grid(row=0, column=0, sticky='nsew')

#================== Home
# Main page
show_frame(home)

button = customtkinter.CTkButton(home, text="Show Calculator", command=lambda:show_frame(calculator))
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


#================== Calculator
# Code for the calculator and frame appearance.
clickAmount = 0
def increment_count():
    global clickAmount
    clickAmount += 1
    return clickAmount

def button_function():
    label.configure(text=f"Click counter: {increment_count()}")

label = customtkinter.CTkLabel(calculator, text='Calculator')
label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
button2 = customtkinter.CTkButton(calculator, text="Return to Home", command=lambda:show_frame(home))
button2.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
button3 = customtkinter.CTkButton(calculator, text="Click Counter", command=button_function)
button3.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

app.mainloop()