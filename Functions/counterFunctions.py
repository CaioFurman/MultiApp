import customtkinter

clickAmount = 0

# Counter Functions
def increment_count():
    global clickAmount
    clickAmount += 1
    return clickAmount

def decrement_count():
    global clickAmount
    clickAmount -= 1
    return clickAmount
def clear_count():
    global clickAmount
    clickAmount = 0
    return clickAmount
