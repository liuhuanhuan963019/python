import json

numbers = [2,3,5,7,11,13]

# filename = "number.json"

# with open(filename,'w') as f_obj:
#     json.dump(numbers,f_obj)

# username = input("what is your name")
# filename = "username.json"
#
# with open(filename,"w") as f_obj:
#     json.dump(username,f_obj)


filename = "username.json"

with open(filename) as f_obj:
    content = json.load(f_obj)
    print(content)


