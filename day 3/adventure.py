hook = "You are walking through the woods with the Queen's precious cargo. You hear a loud noise in front of you. What do you do?\n" \
        "A. Run and hide \n" "B. Turn around couragously \n" "C. Run towards the noise \n"

decision_a = "You hide behind a tree and fall into a reality warping hole. You land on Tatooine. What do you do? \n" \
    "D. Get on the pod racer \n" "E. Call for help \n" "F. Cry \n"

decision_b = "You face a giant snaggletoothed rat. It is hungry. What do you do? \n" \
    "G. Fight the fat \n" "H. Run and hide \n" "I. Befriend the rat \n"

decision_c = "You find a kind old man who tripped on the path. He offers you a wish. What do you do? \n" \
    "J. Run and hide \n" "K. Ask about the condiitons of the wish \n" "L. Wish for BYU creamery chocolate milk \n"

decision_d = "You are challenged to a race. What do you do? \n" "M. Win the race \n" "N. Lose the race \n"

decision_e = "Sand people come to eat you. What do you do? \n" "O. Fight \n" "P. Run and hide \n"

decision_f = "You keep crying. What do you do? \n" "Q. Cry more \n" "R. Stop crying \n"

decision_g = "The rat kills you."

decision_h = decision_a

decision_i = "The rat is now your bestie. You win!"

decision_j = decision_a

decision_k = "The old man gets angry and kills you."

decision_l = "The old man gives you a gallon of BYU creamery chocolate milk. You win!"

decision_m = "You win!"

decision_n = "You die."

decision_o = decision_n

decision_p = decision_a

decision_q = "You die from dehydration."

decision_r = decision_m

decision = input(hook)      # collect decision from the user
decision = decision.upper()

# write what happens when you make your decision
decision2 = ""

if decision == "A":
    decision2 = input(decision_a)
elif decision == "B":
    decision2 = input(decision_b)
elif decision == "C":
    decision2 = input(decision_c)
else:
    print("You are dead.")

if decision == "A" or decision == "B" or decision == "C":
    decision2 = decision2.upper()

    if decision2 == "D":
        decision3 = input(decision_d)
    elif decision2 == "E":
        decision3 = input(decision_e)
    elif decision2 == "F":
        decision3 = input(decision_f)
    elif decision2 == "G":
        decision3 == input(decision_g)
    elif decision2 == "H":
        decision3 = input(decision_h)
    elif decision2 == "I":
        decision3 = input(decision_i)
    elif decision2 == "J":
        decision3 = input(decision_j)
    elif decision2 == "K":
        decision3 = input(decision_k)
    elif decision2 == "L":  
        decision3 = input(decision_l)
    elif decision2 == "M":
        decision3 = input(decision_m)
    elif decision2 == "N":
        decision3 = input(decision_n)
    elif decision2 == "O":
        decision3 = input(decision_o)
    elif decision2 == "P":
        decision3 = input(decision_p)
    elif decision2 == "Q":
        decision3 = input(decision_q)
    elif decision2 == "R":
        decision3 = input(decision_r)
    else:
        print("You are dead.")
   