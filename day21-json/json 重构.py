import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
           username= json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    username = get_stored_username()
    if username:
        print("welcome back " + username)
    else:
        username = input("what is your name?")
        filename = "username.json"
        with open(filename,"w") as f_obj:
            json.dump(username,f_obj)


greet_user()