guessed = False
while not guessed:
    guessed = input("Pick a number")
    if int(guessed) == 50:
         guessed = True

         print("You win")
