import random

# Constants
chars = list("abcdefghijklmonpqrstuvqyz")
chars_upper = list("ABCDEFGHIJKLMONPQRSTUVWXYZ")
nums = list(range(0, 10))
syms = list("!\"£$%^&*()_+-=[]{};':@',./<>?")

# Variables
options = [chars, chars_upper, nums, syms]
max_len = 15

# Functions
def generate(max_len):
    out = ""

    while len(out) <= max_len:
        type_of_char = random.choice(options)
        out += str(random.choice(type_of_char))

    return out

if __name__ == "__main__":
    max_len = int(input("Input length of password > "))
    print(generate(max_len))
