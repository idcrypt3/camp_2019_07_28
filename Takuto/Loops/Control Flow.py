guessed=False
guess=input("Pick a number")
if int(guess)==14:
    guessed=True

print("You win!")

guessed=False
guess=input("Pick a number")
if int(guess)==50:
    guessed=True

print("You guessed the right number")

number_of_leaves=14
for x in range(0,number_of_leaves):
    print("A leaf fell to the ground"+ str(x)+" leaves have fallen.")

print("All the leaves fell. For loop complete.")