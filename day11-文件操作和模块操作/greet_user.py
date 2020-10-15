import json

def greet_json():
    file_name = 'username.json'
    try:
        with open(file_name) as f_obj:
            user_name = json.load(f_obj)
    except FileNotFoundError:
        user_name = input('please input a name')
        with open(file_name,'w') as f_obj:
            json.dumps(user_name,f_obj)
            print('name is ',user_name)
    else:
        print('ok')

greet_json()



