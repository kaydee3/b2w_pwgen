# Import everything from tkinter, our graphics library
# importing * takes everything from the tkinter module and stores them in our script
from tkinter import *
# Import the ttk object from GUI library, which provides some extra functionality
# importing this object creates a variable ttk in this script that we can use to access it
from tkinter import ttk

# Import Python's Random module, which provides the functionality we will use to generate randomness.
import random

# Constants
# Python itself doesn't have the concept of constants natively
# But common practice is to identify variables that should not be changed as capitalised
LETTERS = list("abcdefghijklmonpqrstuvqyz") # List function splits a string by each character.
UPPERCASE_LETTERS = list("ABCDEFGHIJKLMONPQRSTUVWXYZ")
NUMBERS = list(range(0, 10)) # List can also convert a range, which will create a list of numbers 0 to 9
SYMBOLS = list("!\"Â£$%^&*()_+-=[]{};':@',./<>?")

# Variables
# My methodology here is, storing the lists within a list lets me easily randomly select each character
# by first selecting the type from this list, selecting the character from the list we've just selected
options = [LETTERS, UPPERCASE_LETTERS, NUMBERS, SYMBOLS] # List of lists, listception!

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

# def is short for define; this statement defines a new function called generate, which takes a value called max_len when called
def generate(max_len):
    # Everything indented to this level is part of this function

    # Create the container for our password we're making
    out = ""

    # Loop while length of output is under our desired maximum
    while len(out) < max_len:
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

    # Get the text from our input box and save it as variable named l
    l = pwdlen_input.get()

    # Checking if input is a valid number.
    # isdigit returns true if l is only a number.
    # `if not` checks if the following statement is false, then executes the indented block if it is.
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

    # SANITY CHECK: If number is 0, set to 1
    if new_len == 0: new_len = 1
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