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

ANIMALS = {
    "Lion" : ["Mammal","Four legs","Predator","King of the jungle","Big cat","Carnivore","Lives in a pride","Has a mane","Lives in a den"],
    "Hyena" : ["Mammal","Has spots","Four legs","Predator","Carnivore","Laughs","Scavenger","Lives in a clan"],
    "Cheetah" : ["Mammal","Has spots","Four legs","Predator","Carnivore","Fastest land animal","Lives in a coalition","Has tear marks"],
    "Giraffe" : ["Mammal","Has spots","Four legs","Herbivore","Tallest land animal","Lives in a tower","Has a long neck"],
    "Zebra" : ["Mammal","Has stripes","Four legs","Herbivore","Lives in a dazzle","Has a mane","Has hooves","Has a tail"],
    "Elephant" : ["Mammal","Has tusks","Four legs","Herbivore","Largest land animal","Lives in a herd","Has a trunk","Has big ears"],
    "Crocodile" : ["Reptile","Has scales","Four legs","Predator","Carnivore","Lives in a bask","Has a long snout","Has a powerful bite"],
    "Kangaroo" : ["Mammal","Has a pouch","Two legs","Herbivore","Lives in a mob","Can jump","Has a tail","Has strong hind legs"],
    "Penguin" : ["Bird","Has feathers","Two legs","Carnivore","Lives in a colony","Can swim","Has flippers","Cannot fly"],
    "Ostrich" : ["Bird","Has feathers","Two legs","Herbivore","Largest bird","Lives in a flock","Can run fast","Cannot fly"],
    "Shark" : ["Fish","Has scales","No legs","Predator","Carnivore","Lives in a school","Has sharp teeth","Can swim fast"],
    "Whale" : ["Mammal","Has blubber","No legs","Carnivore","Largest animal","Lives in a pod","Has a blowhole","Can swim fast"],
    "Spider" : ["Arachnid","Has eight legs","Has eight eyes","Predator","Carnivore","Lives in a web","Can spin silk","Can climb walls"],
    "Scorpion" : ["Arachnid","Has eight legs","Has pincers","Predator","Carnivore","Lives in a burrow","Can sting","Can survive in harsh environments"],
    "Whale" : ["Mammal","Has blubber","No legs","Carnivore","Largest animal","Lives in a pod","Has a blowhole","Can swim fast"],
    "Cobra:" : ["Reptile","Has scales","Four legs","Predator","Carnivore","Lives in a den","Has venom","Can hood"],
    "Frog" : ["Amphibian","Has smooth skin","Four legs","Carnivore","Lives in a pond","Can jump","Has a long tongue","Can croak"],
    "Turtle" : ["Reptile","Has a shell","Four legs","Herbivore","Lives in a bask","Can retract into its shell","Has a beak","Can live a long time"],
    "Bison" : ["Mammal","Has a hump","Four legs","Herbivore","Lives in a herd","Has a shaggy mane","Can run fast","Has hooves"],
    "Bear" : ["Mammal","Has fur","Four legs","Omnivore","Lives in a den","Can hibernate","Has sharp claws","Can climb trees"],
    "Wolf" : ["Mammal","Has fur","Four legs","Predator","Carnivore","Lives in a pack","Has sharp teeth","Can howl"],
    "Cow" : ["Mammal","Has fur","Four legs","Herbivore","Lives in a herd","Gives milk","Has hooves","Has a tail"],
    "Gorilla" : ["Mammal","Has fur","Four legs","Herbivore","Lives in a troop","Can climb trees","Has a strong build","Has a prominent brow ridge"],
    "Eagle" : ["Bird","Has feathers","Two legs","Carnivore","Lives in a nest","Can fly","Has sharp talons","Has a hooked beak","National bird"],
    "Dolphin" : ["Mammal","Has blubber","No legs","Carnivore","Lives in a pod","Can swim fast","Has a blowhole","Is intelligent"],
    "Octopus" : ["Mollusk","Has tentacles","No legs","Predator","Carnivore","Lives in a den","Can change color","Can squirt ink"]
}

WELCOME_MESSAGE = """Animal guessing game:
I have picked a random animal.
Guess an attribute or the name of the animal.
"""

CONGRATS_MESSAGE = "You win!"

# processes

list_of_animal_names = list(ANIMALS.keys())
random_animal = random.choice(list_of_animal_names)
random_animal_attributes = ANIMALS[random_animal]

print(WELCOME_MESSAGE)

guess = ""

while guess != random_animal:
    guess = input("Please guess an attribute or an animal name: ").capitalize()
    if guess in random_animal_attributes:
        print(f"Yes, {guess} is an attibute of the animal.")
    elif guess == random_animal:
        print(CONGRATS_MESSAGE)
    else:
        print(f"No, {guess} is not an attribute of the animal.")
