"""
inputs:
-  player level (int)
-  player class (str)

processes:
-  sugguest a quest type based on player level and class
-  different quests for level ranges (1-10, 11-25, 26+), modified by class

outputs:
-  print a recommended quest

"""

class_types = {
    "Wizard" : ["Find a wand", "Find a spellbook","Duel your professor"],
    "Fighter" : ["Find a sword","Find a shield","Defend your professor from the evil wizard"]
}

player_class = input("Player class: ").capitalize()
player_level = ""
while not player_level.isdigit():
    player_level = input("Current level (enter a number): ")

player_level = int(player_level)

# calculate quest level bsaed on the player level
quest_level = 0
if player_level >= 26:
    quest_level = 2
elif player_level >= 11:
    quest_level = 1

recommended_quest = class_types[player_class][quest_level]

print(f"You should do this quest: {recommended_quest}.")
