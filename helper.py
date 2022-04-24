import json
import os.path

main_list=[]
flag = ""
while(flag != "N"):
    print("flag", flag)
    d = {}
    d["date"] = input("Enter a date to play: ")
    d["name"] = input("Enter first name: ")
    d["email"] = input("Enter email address: ")
    d["Answer"] = input("Enter an answer (y or n): ")
    main_list.append(d)
    flag = input("Continue inputting data Y/N: ")
print(d['date'])
filename=d['date'] + '.json'
with open(filename, 'w') as file:
        file.seek(0)
        # convert back to json.
        json.dump(main_list, file, indent = 2)