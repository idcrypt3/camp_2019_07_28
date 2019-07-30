guessed=False
while not guessed:
    guess=input("Pick an number")
    if int(guess)==50:
        guessed=True
        print("correct!")