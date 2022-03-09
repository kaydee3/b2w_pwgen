# Import tkinter, our graphics library
from tkinter import *
from tkinter import ttk

# Import Python's Random module
import random

# Constants
chars = list("abcdefghijklmonpqrstuvqyz") # List function splits a string by each character.
chars_upper = list("ABCDEFGHIJKLMONPQRSTUVWXYZ")
nums = list(range(0, 10)) # List can also convert a range, which will create a list of numbers 0 to 9
syms = list("!\"Â£$%^&*()_+-=[]{};':@',./<>?")

# Variables
options = [chars, chars_upper, nums, syms] # List of list,s listception!

# Defining our input and output boxes
# We're creating these here, even if the elements themselves are not being created yet, so the entire script can access them.
# Otherwise, because Python reads code sequentially, the variables would not be available in some cases.
# This is called forward declaration. 
pwdlen_input = None
pwdlen_output = None

# Create the core of our window
root = Tk()

# Give our window a title
root.title("pwdgen")

# Functions
def generate(max_len):
    # Create the container for our password we're making
    out = ""

    # Loop while length of output is under our desired maximum
    while len(out) <= max_len:
        # Choose the type of character, out of the options list we defined earlier
        type_of_char = random.choice(options)

        # Select a random entry from that list, ensure that it is a string, and append it to output
        out += str(random.choice(type_of_char))

    # Return our output
    return out

# This function is called when the button is clicked.
def clicked_button():
    # Clear our computers clipboard
    root.clipboard_clear()

    # Get the text from our input box
    l = pwdlen_input.get()

    # Checking if input is a valid number.
    if not l.isdigit():
        # This section executes if variable l is not a number.

        # Because we defined pwdlen_output above this line, this function can access it.
        # Otherwise, the variable would error as undefined, since it would be created below this line.
        pwdlen_output.delete(0, END)
        pwdlen_output.insert(0, "Length is not a valid number.")

        # Return here, which prevents the rest of the function from executing.
        return

    # Call our generate function and pass the value of the input box, now we know it is an int
    pwd = generate(int(l))

    # Add the result directly to clipboard
    root.clipboard_append(pwd)

    # Clear the output box
    pwdlen_output.delete(0, END)

    # Insert the password to the output box
    pwdlen_output.insert(0, pwd)

# Utility function to increment or decrement the input length
def modifier(m):
    l = pwdlen_input.get()
    
    if not l.isdigit():
        pwdlen_output.delete(0, END)
        pwdlen_output.insert(0, "Length is not a valid number.")
        return

    # Defining the variable for our new length, it's value does not matter at this point so using a default.
    new_len = 0

    # Set new_len to current content of len input, but increment or decrement by 1
    if m == "+": new_len = int(l) + 1
           
    if m == "-": new_len = int(l) - 1

    # Overwrite the input box value
    pwdlen_input.delete(0, END)
    pwdlen_input.insert(0, str(new_len))

# Add a frame to the window, a container that we can store elements in
# We save the created element to the variable frm for later use
frm = ttk.Frame(root, padding=10)

# Place it on the grid
frm.grid()

# If we don't need to store the element for later, we can just create and place all in one line
ttk.Label(frm, text="Length: ").grid(row=0, column=0)

# Create a text input field
# We created this variable earlier, now this is now adding a value to it, the entry box, rather than creating a brand new variable.
pwdlen_input = ttk.Entry(frm, width=30)
# Insert 20 in to the input as a default
pwdlen_input.insert(0, "20")

pwdlen_input.grid(column=1,row=0)

# Create our buttons

# The buttons take a `command` option, which is a function which will be called when the button is pressed.

ttk.Button(frm, text="Generate", command=clicked_button).grid(column=2, row=0)

# This time though, I want to re-use the same function for two buttons, 
# so we use a lambda instead of passing a function directly.
ttk.Button(frm, text="-", command=lambda: modifier("-")).grid(column=3, row=0)
ttk.Button(frm, text="+", command=lambda: modifier("+")).grid(column=4, row=0)

# Create the output box
pwdlen_output = ttk.Entry(frm, width=70)
pwdlen_output.grid(column=0,row=1, columnspan=5)

# Starts our GUI once we have finished placing everything.
root.mainloop()