'''
d = {}

size = int(input("Enter the size of nested dictionary: "))
for i in range(size):
    
    dict_name = input("Enter the name of child dictionary: ")
    d[dict_name] = {}
    Name = input("Enter name: ")
    Age = input("Enter Age: ")
    d[dict_name]["Name"] = Name
    d[dict_name]["Age"] = Age
    
print(d)
'''

name_lists=[]
flag = ""
while(flag != "N"):
    d = {}
    d["name"] = input("Enter a name: ")
    d["surname"] = input("Enter a surname: ")
    d["patronmic"] = input("Enter a patronmic: ")
    d["id_number"] = input("Enter a worker's id number: ")
    name_lists.append(d)
    flag = input("Continue inputting data Y/N: ")
print(name_lists)