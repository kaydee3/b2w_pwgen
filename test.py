from cryptography.fernet import Fernet

key = "eKPqoLhrx-J4ZVWd2gqZPBOsQHABcOEyjZJn7DoAnLM=" #Fernet.generate_key()
print(key)

f = Fernet(key)

token = f.decrypt(bytes("gAAAAABiJpI890DNF2wmBZPten5_tEJLmzCcHHagZApIQAjB2LiOCh6lVW1TJPzN2iDKIic9teyEksyM060aHHKwPO0Yxc_mPqtbJHtqCjDPqowZaycc66s=", "utf-8"))
print(token)

