import dearpygui.dearpygui as dpg
import random

chars = list("abcdefghijklmonpqrstuvqyz")
chars_upper = list("ABCDEFGHIJKLMONPQRSTUVWXYZ")
nums = list(range(0, 10))
syms = list("!\"£$%^&*()_+-=[]{};':@',./<>?")
options = [chars, chars_upper, nums, syms]

def append_listbox(name, item):
    items = dpg.get_item_configuration(name)["items"]
    items.insert(0, item)
    dpg.configure_item(name, items=items)

def generate(max_len):
    out = ""

    while len(out) <= max_len:
        type_of_char = random.choice(options)
        out += str(random.choice(type_of_char))

    return out

dpg.create_context()

with dpg.window(tag="Primary Window"):
    with dpg.group(horizontal=True):
        def do_gen():
            pwd = generate(dpg.get_value("pwd_len"))
            append_listbox("outputs", pwd)

        def copy_pwd(_, i):
            print(i)
            dpg.set_clipboard_text(i)
        dpg.add_text("Length: ")
        dpg.add_input_int(tag="pwd_len", width=400, default_value=20)
        dpg.add_button(tag="gen_pass", label="Generate", callback=do_gen)
        dpg.add_button(tag="del_pass", label="Clear")
    dpg.add_listbox(tag="outputs", width=580, num_items=9, callback=copy_pwd)
    dpg.add_text("Choose the password length, click generate, then click on the password to \ncopy it to clipboard!")

dpg.create_viewport(title='Kyle\'s Password Generator', width=600, height=230)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
