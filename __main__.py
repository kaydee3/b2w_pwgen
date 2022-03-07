import dearpygui.dearpygui as dpg
import random

chars = list("abcdefghijklmonpqrstuvqyz")
chars_upper = list("ABCDEFGHIJKLMONPQRSTUVWXYZ")
nums = list(range(0, 10))
syms = list("!\"£$%^&*()_+-=[]{};':@',./<>?")
options = [chars, chars_upper, nums, chars]

def append_listbox(name, item):
    items = dpg.get_item_configuration(name)["items"]
    items.append(item)
    dpg.configure_item(name, items=items)

dpg.create_context()

with dpg.window(tag="Primary Window"):
    with dpg.group(horizontal=True):
        def do_gen():
            pwd = generate()
            append_listbox("outputs", pwd)
        dpg.add_text("Length: ")
        dpg.add_input_int(tag="pwd_len", width=400, min_value=5, max_value=50)
        dpg.add_button(tag="gen_pass", label="Generate", callback=do_gen)
        dpg.add_button(tag="del_pass", label="Clear")
    dpg.add_listbox(tag="outputs", width=600, num_items=10)

dpg.create_viewport(title='Kyle\'s Password Generator', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

def generate(max_len):
    out = ""

    while len(out) <= max_len:
        type_of_char = random.choice(options)
        out += random.choice(type_of_char)

    return out