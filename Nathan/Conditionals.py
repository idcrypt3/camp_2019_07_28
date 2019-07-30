life = 3
print(life)
if life > 0:
    life -= 1
    print(life)
elif life == 0:
    print("The player has zero life.")
else:
    print("The player ran out of life!")