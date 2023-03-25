import customtkinter
counterValue = 0

# Modification of the counter values
def increment_count():
    global counterValue
    counterValue += 1
    return counterValue


def decrement_count():
    global counterValue
    counterValue -= 1
    return counterValue


def clear_count():
    global counterValue
    counterValue = 0
    return counterValue
