player_age = 12

if player_age >= 18:
    print("You could be in college")
elif player_age >= 13 and player_age < 18:
    print("You can also attend iD Academies!")
elif player_age >= 7 and player_age < 13:
    print("You can attend iD Tech Camps!")
else:
    print("You're young.")

 player_has_item = False
 score = 50
 won = False

 if player_has_item and score > 100:
    won = True

 if not won:
    print("You haven't beaten the game yet.")
 elif won:
    print("You won the game!")