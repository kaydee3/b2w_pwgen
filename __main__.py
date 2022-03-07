# Core imports
import random, os, sys

# Update path so we can import local libraries
p = os.path.dirname(os.path.abspath(__file__)) # Get path to this file
sys.path.append(p) # Append to system PATH environment

# Import the GUI library
import dearpygui.dearpygui as dpg

# Constants
chars = list("abcdefghijklmonpqrstuvqyz") # Making the string a list splits it by each character.
chars_upper = list("ABCDEFGHIJKLMONPQRSTUVWXYZ")
nums = list(range(0, 10)) # Convert the 0..10 range in to a list
syms = list("!\"£$%^&*()_+-=[]{};':@',./<>?")

# Variables
options = [chars, chars_upper, nums, syms] # list of lists, listception!

# Functions
def append_listbox(name, item):
    "Utility function, append item to a listbox."
    items = dpg.get_item_configuration(name)["items"]
    items.insert(0, item)
    dpg.configure_item(name, items=items)

def generate(max_len):
    "Password generator."
    out = ""

    while len(out) <= max_len:
        type_of_char = random.choice(options)
        out += str(random.choice(type_of_char))

    return out


# Main

def main():
    # GUI library setup
    dpg.create_context()

    # Create our primary window which will contain the interface for the generator.
    with dpg.window(tag="Primary Window"):
        # Creating a group so we can display a few elements horizontally
        with dpg.group(horizontal=True):
            # Callback functions, used for the buttons
            def do_gen():
                pwd = generate(dpg.get_value("pwd_len"))
                append_listbox("outputs", pwd)

            def copy_pwd(_, i):
                print(i)
                dpg.set_clipboard_text(i)

            # Creating elements
            dpg.add_text("Length: ")
            dpg.add_input_int(tag="pwd_len", width=400, default_value=20)
            dpg.add_button(tag="gen_pass", label="Generate", callback=do_gen)
            dpg.add_button(tag="del_pass", label="Clear")

        # Remaining elements add vertically
        dpg.add_listbox(tag="outputs", width=580, num_items=9, callback=copy_pwd)
        dpg.add_text("Choose the password length, click generate, then click on the password to \ncopy it to clipboard!")

    # Remaining setup functions for the GUI.
    dpg.create_viewport(title='Kyle\'s Password Generator', width=600, height=230)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

# If this file is the main file, and not a library, execute main function loop
if __name__ == "__main__":
    main()
