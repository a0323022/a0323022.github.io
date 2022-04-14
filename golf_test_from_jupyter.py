# Introduction
'''
**Instructions**

Create an empty list called `players`. This will be your list of people who are playing golf.
'''
players = []
emails = {
    "Fogel": "davefogel59@gmail.com",
    "Huebsch": "j.huebsch@comcast.net",
    "Newman": "newmbo@comcast.net",
    "Smith": "a0323022@gmail.com",
    "Fritz": "richdogf@aol.com",
    "Adams": "dadams7524@gmail.com",
    "Hunt": "highroad2@aol.com",
    "Mutters": "mutters063090@gmail.com",
    "Wilson": "jim@jimandharriet.com",
    "Dozier": "rjdoz@hotmail.com",
    "Heneghan": "bob.heneghan@yahoo.com",
    "Durflinger": "cadurflinger@yahoo.com",
    "Crumrine": "jtcrumrine@gmail.com",
    "Sheppard": "gsheppard27@gmail.com",
    "Gilpin": "jonathan.d.gilpin@gmail.com"
}

'''
Now we want to create a function that will update this list and add a new player to the this `players`
list. Each `player` should be a dictionary with the following keys:
 - `"name"`: a string that contains the player's full or presumed name. E.g., "Vicky Very"
 - `"availability"`: a list of strings containing the names of the days of the week that the player
 is playing. E.g., ["Monday", "Thursday",
  "Sunday"]
 
**Instructions**

Create a function called `add_player` that takes two parameters: `player` and `players_list`. The
function should check that the argument passed to the `player` parameter has both `"name"` and a
`"availability"` as keys and if so add `player` to `players_list`.
'''
def add_player(player, players_list):
    if player.get("name") and player.get("availability"):
        players_list.append(player)
    else:
        print("player missing critical information")
'''
Next we want to add our first player! Her name is Kimberly Warner and she's available on Mondays, Tuesdays, and Fridays.

**Instructions**

1. Create a dictionary called `kimberly` with the name and availability given above.
2. Call `add_player` with `kimberly` as the first argument and `players` as the second.

'''
kimberly = {
    'name': "Kimberly Warner",
    'availability': ["Monday", "Tuesday", "Friday"]
}

add_player(kimberly, players)

print(players)
'''
[{'name': 'Kimberly Warner', 'availability': ['Monday', 'Tuesday', 'Friday']}]

Great! Let's add a couple more players to the list!
'''

add_player({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, players)
add_player({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, players)
add_player({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, players)
add_player({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, players)
add_player({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, players)
add_player({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, players)
add_player({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, players)
add_player({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, players)
add_player({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, players)

'''
## Finding the perfect availability

Now that we have a list of all of the people interested in game night, we want to be able to calculate
which nights would have the most participation. First we need to create a frequency table which 
correlates each day of the week with player availability.

**Instructions**

Create a function called `build_daily_frequency_table` that takes no argument returns a dictionary with
the days of the week as keys and `0`s for values. We'll be using this to count the availability per night. 
Call `build_daily_frequency_table` and save the results to a variable called `count_availability`.
'''

def build_daily_frequency_table():
    return {
        "Monday":    0,
        "Tuesday":   0,
        "Wednesday": 0,
        "Thursday":  0,
        "Friday":    0,
        "Saturday":  0,
        "Sunday":    0,
    }

count_availability = build_daily_frequency_table()

'''
Next we need to count the number of people every night.

**Instructions**

Write a function called `calculate_availability` that takes a list of players as an argument `players_list`
and a frequency table `available_frequency`. The function should iterate through each player in
`players_list` and iterate through each day in the player's availability. For each day in the player's 
availability, add one to that date on the frequency table.
'''
def calculate_availability(players_list, available_frequency):
    for player in players_list:
        for day in player['availability']:
            available_frequency[day] += 1

'''
Now let's use these tools to find the best night to run Abruptly Goblins!

**Instructions**

Call `calculate_availability` with `players` and `count_availability`. Print out `count_availability` 
afterwards.
'''

calculate_availability(players, count_availability)
print(count_availability)


'''{'Monday': 5, 'Tuesday': 4, 'Wednesday': 4, 'Thursday': 6, 'Friday': 3, 'Saturday': 4, 'Sunday': 3}'''

'''
Lastly we need a way to pick the day with the most available people to attend so that we can schedule
game night on that night.

**Instructions**

Write a function `find_best_night` that takes a dictionary `availability_table` and returns the key 
with the highest number.
'''

def find_best_night(availability_table):
    best_availability = 0
    for day, availability in availability_table.items():
        if availability > best_availability:
            best_night = day
            best_availability = availability
    return best_night

game_night = find_best_night(count_availability)
print(game_night)

def available_on_night(players_list, day):
    return [player for player in players_list if day in player['availability']]

attending_game_night = available_on_night(players, game_night)

print(attending_game_night)

form_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week}
and have a blast!

Magically Yours,
the Sorcery Society
"""

def send_email(players_who_can_attend, day, game):
    for player in players_who_can_attend:
        print(form_email.format(name=player['name'], day_of_week=day, game=game))
        
send_email(attending_game_night, game_night, "Abruptly Goblins!")

unable_to_attend_best_night = [player for player in players if game_night not in player['availability']]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)




















'''

[{'name': 'Kimberly Warner', 'availability': ['Monday', 'Tuesday', 'Friday']}]
{'Monday': 5, 'Tuesday': 4, 'Wednesday': 4, 'Thursday': 6, 'Friday': 3, 'Saturday': 4, 'Sunday': 3}
Thursday
[{'name': 'Thomas Nelson', 'availability': ['Tuesday', 'Thursday', 'Saturday']}, {'name': 'Michelle Reyes', 'availability': ['Wednesday', 'Thursday', 'Sunday']}, {'name': 'Stephen Adams', 'availability': ['Thursday', 'Saturday']}, {'name': 'Joanne Lynn', 'availability': ['Monday', 'Thursday']}, {'name': 'Crystal Brewer', 'availability': ['Thursday', 'Friday', 'Saturday']}, {'name': 'James Barnes Jr.', 'availability': ['Tuesday', 'Wednesday', 'Thursday', 'Sunday']}]


**Instructions**

Create a function `send_email` with three parameters: `players_who_can_attend`, `day`, and `game`. Print `form_email` for each player in `players_who_can_attend` with the appropriate `day` and `game`.
Call `send_email` with `attending_game_night`, `game_night`, and `"Abruptly Goblins!"`.

def send_email(players_who_can_attend, day, game):
    for player in players_who_can_attend:
        print(form_email.format(name=player['name'], day_of_week=day, game=game))
        
send_email(attending_game_night, game_night, "Abruptly Goblins!")



Output exceeds the size limit. Open the full output data in a text editor

Dear Thomas Nelson,

The Sorcery Society is happy to host "Abruptly Goblins!" night and wishes you will attend. Come by on Thursday and have a blast!

Magically Yours,
the Sorcery Society


Dear Michelle Reyes,

The Sorcery Society is happy to host "Abruptly Goblins!" night and wishes you will attend. Come by on Thursday and have a blast!

Magically Yours,
the Sorcery Society


Dear Stephen Adams,

The Sorcery Society is happy to host "Abruptly Goblins!" night and wishes you will attend. Come by on Thursday and have a blast!

Magically Yours,
the Sorcery Society



Magically Yours,
the Sorcery Society

Output exceeds the size limit. Open the full output data in a text editor

Dear Kimberly Warner,

The Sorcery Society is happy to host "Abruptly Goblins!" night and wishes you will attend. Come by on Monday and have a blast!

Magically Yours,
the Sorcery Society


Dear Joyce Sellers,

The Sorcery Society is happy to host "Abruptly Goblins!" night and wishes you will attend. Come by on Monday and have a blast!

Magically Yours,
the Sorcery Society


Dear Joanne Lynn,

The Sorcery Society is happy to host "Abruptly Goblins!" night and wishes you will attend. Come by on Monday and have a blast!

Magically Yours,
the Sorcery Society

Magically Yours,
the Sorcery Society

'''