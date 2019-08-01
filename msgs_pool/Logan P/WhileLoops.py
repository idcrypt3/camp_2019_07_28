guessed = False
while not guessed:
    guess = input("Pick a number")
    if int(guess) == 14:
        guessed = True

print("You Win!")

number_of_leaves = 14
for x in range(0, number_of_leaves):#runs when variable: X is between 0 and the number of leaves
    print("A leaf fell to the ground " +str(x)+ "leaves have fallen.")

print("All the leaves fell. For loop complete.")


on_roller_coaster = True
while on_roller_coaster:
    print("Ahhh!")
    on_roller_coaster = False

times_to_repeat = 5
for x in range(0, times_to_repeat):
    print(x)

for x in range(0, 10):
    if x == 2:
        break
    print(x)

