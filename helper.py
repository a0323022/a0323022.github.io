import json
date = "042422"

# function to create JSON

def new_json(data, filename=date + ".json"):
    with open(filename, 'w') as file:
        file.seek(0)
        # convert back to json.
        json.dump(data, file, indent = 4)

'''
# function to add to JSON
def add_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended
y = {"emp_name":"Nikhil",
     "email": "nikhil@geeksforgeeks.org",
     "job_profile": "Full Time"
    }
     
add_json(y)
'''
x = {"emp_name":"Nikhil",
     "email": "nikhil@geeksforgeeks.org",
     "job_profile": "Full Time"
    }
new_json(x)

'''
# JSON data:
x =  '{ "organization":"GeeksForGeeks",
        "city":"Noida",
        "country":"India"}'
 
# python object to be appended
y = {"pin":110096}
 
# parsing JSON string:
z = json.loads(x)
  
# appending the data
z.update(y)
 
# the result is a JSON string:
print(json.dumps(z))
jfile = 
'''
'''
emails = {
    "Dave Fogel": "davefogel59@gmail.com",
    "John Huebsch": "J.huebsch@comcast.net",
    "Larry Newman": "newmbo@comcast.net",
    "Trey Smith": "a0323022@gmail.com",
    "Rich Fritz": "richdogf@aol.com",
    "Don Adams": "dadams7524@gmail.com",
    "Dave Hunt": "highroad2@aol.com",
    "Rick Mutters": "mutters063090@gmail.com",
    "Jim Wilson": "jim@jimandharriet.com",
    "Bob Dozier": "rjdoz@hotmail.com",
    "Bob Hanegan": "bob.heneghan@yahoo.com",
    "Chad Durflinger": "cadurflinger@yahoo.com",
    "Jeff Crumrine": "jtcrumrine@gmail.com",
    "Gary Sheppard": "gsheppard27@gmail.com",
    "Del Gilpin": "Jonathan.d.gilpin@gmail.com",
    "John Blessent": "jblessent@msn.com"
}

responses = {
    '041722': [
        {
            'a0323022@gmail.com': 'yes',
            'davefogel59@gmail.com': 'yes',
            'J.huebsch@comcast.net': 'yes',
            'newmbo@comcast.net': 'no',
            'richdogf@aol.com': 'no',
            'dadams7524@gmail.com': 'yes',
            'highroad2@aol.com': 'no',
            'mutters063090@gmail.com': 'no',
            'jim@jimandharriet.com': 'yes',
            'rjdoz@hotmail.com': 'yes',
            'bob.heneghan@yahoo.com': 'yes',
            'cadurflinger@yahoo.com': 'yes',
            'jtcrumrine@gmail.com': 'no',
            'gsheppard27@gmail.com': 'yes',
            'Jonathan.d.gilpin@gmail.com': 'yes'
         }
    ],
}
 
# Prints value corresponding to key 'name' in Dict1
#print(Dict['Dict1']['name'])
print(emails["041722"]["Dave Fogel"])
# Prints value corresponding to key 'age' in Dict2
#print(Dict['Dict2']['age'])
#print(emails)
'''
'''
types = {1: "Breakfast", 2: "Breakfast"}
descriptions = {1: "Egg fried in butter", 2: "Toasted bread spread with butter"}
ingredients = {1: ["1 pad of butter", "1 Egg", "A pinch of salt"], 2: ["1 pad of salted butter", "1 slice of bread"]}
instructions = {1: {"Step 2": "Crack the egg into the buttered pan", "Step 5": "Serve egg after about a minute and a half", "Step 1": "Melt butter in pan over medium-low heat", "Step 4": "Flip egg after about a minute and a half", "Step 3": "Sprinke the pinch of salt onto cooking egg",},
                2: {"Step 3": "Put the pad of butter on the toasted bread", "Step 4": "After a minute spread the melted butter onto the bread", "Step 1": "Put the bread in the toaster", "Step 2": "Take the toast out of the toaster"}}
comments = {1: ["Yummy!!", "Egg-cellent ;-"], 2: ["Toasty", "What a great recipe!"]}

def add_ingredients(recipe_id=None, text=None):
  if recipe_id and text:
    text_list = text.split("\n")
    ingredients[recipe_id] = text_list

def add_instructions(recipe_id=None, text=None):
  if recipe_id and text:
    text_list = text.split("\n")
    instructions_dict = {}
    for i, instruction in enumerate(text_list):
      instructions_dict["Step {}".format(i+1)] = instruction

    instructions[recipe_id] = instructions_dict

    '''
    