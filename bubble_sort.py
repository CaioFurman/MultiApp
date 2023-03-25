import customtkinter
import tkinter
import random


# =========================== #
# ####### Bubble Sort ####### #
# =========================== #
def showBubble(bubbleFrame):
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            # Last i elements are already sorted
            for j in range(0, n - i - 1):
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    bubbleLabel.configure(text=str(arr))
                    bubbleLabel.update()
                    bubbleLabel.after(100)  # pause for 100 milliseconds

        return arr

    def randomize():
        # Generate a random array of numbers between 1 and 100
        arr = [random.randint(1, 100) for _ in range(10)]
        print("Unsorted:", arr)
        bubble_sort(arr)

    # =========================== #
    # ########## Style ########## #
    # =========================== #

    bubbleLabel = customtkinter.CTkLabel(
        bubbleFrame,
        font=(tuple, 25),
        text='Bubble sort random numbers'
    )
    randomizeButton = customtkinter.CTkButton(
        bubbleFrame,
        width=200,
        height=60,
        font=(tuple, 20),
        text="Randomize",
        command=randomize
    )

    randomizeButton.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    bubbleLabel.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
