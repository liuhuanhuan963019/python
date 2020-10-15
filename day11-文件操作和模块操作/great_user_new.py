import json

def get_stored_name():
    pass

def get_new_username():
    username = input('please input a name')
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dumps(username,f_obj)
    return username

def greet_username():
    user_name = get_new_username()
    if user_name:
        print('welcome'+user_name)
    else:
        user_name = get_stored_name()
        print('please input a name')
