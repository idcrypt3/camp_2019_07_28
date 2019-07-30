a=6
b=3
if a>b:
    print("a is greater than b")

x=2
if x>1:
    x+=2

print(x)

has_key=False
if has_key==True:
    print("You won! Unlock the door!")

print(5>4)
print(10==10)
print(5<10)

player_age=12

if player_age>=18:
    print("You coul be in college")
elif player_age>=13 and player_age<18:
    print("You can also attend iD Academies!")
elif player_age>=7 and player_age<13:
    print("You can attend iD Tech Camps!")
else:
    print("You're young.")

player_has_item=False
score=50
won=False

if player_has_item and score>100:
    won=True

if not won:
    print("You haven't beaten the game yet.")
elif won:
    print("You won the game!")

player_has_item=False
score=100
won=False

if player_has_item or score>200:
    won=True

if not won:
    print("You haven't beaten the game yet.")
elif won:
    print("You won the game"!)

import random
computer_number=random.randrage(0,101)
    print(computer_number)

guessed=False

while True:
    if guessed:
        answer=input("Guess the number")
        if int(answer)==computer_number:
            guessed=True
            print("You got it!")
            break
    elif int(answer)==computer_nmumber:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")

else:
    break