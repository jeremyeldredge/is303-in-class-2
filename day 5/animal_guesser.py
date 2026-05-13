"""
Animal Guessing Game

Inputs:
- User types a string containing an attribute guess or the guess of the animal's name.

Processes:
- Randomly select an animal
- Allow the user to guess until they guess the correct animal
- When they guess, tell them if the animal has the attribute or not
- Tell the user when they guess correctly

Outputs:
- Attribute guess correctness
- Congratulatory message

"""

import random   # teaches python how to do random stuff

# static variables

# Each animal uses these categories in this order.
ATTRIBUTE_CATEGORIES = ["Animal type", "Number of legs", "General color", "Diet", "Body covering", "Habitat", "Social group", "Special feature"]

ANIMALS = {
    "Lion" : ["Mammal","Four legs","Tan","Carnivore","Fur","Grassland","Pride","Has a mane"],
    "Hyena" : ["Mammal","Four legs","Brown","Carnivore","Fur","Grassland","Clan","Laughs"],
    "Cheetah" : ["Mammal","Four legs","Tan","Carnivore","Fur","Grassland","Coalition","Has tear marks"],
    "Giraffe" : ["Mammal","Four legs","Tan","Herbivore","Fur","Grassland","Tower","Has a long neck"],
    "Zebra" : ["Mammal","Four legs","Black and white","Herbivore","Fur","Grassland","Dazzle","Has stripes"],
    "Elephant" : ["Mammal","Four legs","Gray","Herbivore","Skin","Grassland","Herd","Has a trunk"],
    "Crocodile" : ["Reptile","Four legs","Green","Carnivore","Scales","Wetland","Bask","Has a long snout"],
    "Kangaroo" : ["Mammal","Two legs","Brown","Herbivore","Fur","Grassland","Mob","Has a pouch"],
    "Penguin" : ["Bird","Two legs","Black and white","Carnivore","Feathers","Coast","Colony","Cannot fly"]
}

WELCOME_MESSAGE = """Animal guessing game:
I have picked a random animal.
Guess an attribute or the name of the animal.
"""

CONGRATS_MESSAGE = "You win!"

# processes

list_of_animal_names = list(ANIMALS.keys())
random_animal = random.choice(list_of_animal_names)

print(WELCOME_MESSAGE)

guess = ""

while guess != random_animal:
    guess = input("Please guess an attribute or an animal name: ").capitalize()
    random_animal_attributes = ANIMALS[random_animal]
    if guess in random_animal_attributes:
        print(f"Yes, {guess} is an attibute of the animal.")
    elif guess == random_animal:
        print(CONGRATS_MESSAGE)
    else:
        print(f"No, {guess} is not an attribute of the animal.")
