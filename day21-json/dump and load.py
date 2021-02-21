import json

filename = "username.json"

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)

except FileNotFoundError:
    username = input("what is your name?")
    with open(filename,"w") as f_obj:
        json.dump(f_obj)

else:
    print("hello" + username)

finally:
    print("bye!!")
