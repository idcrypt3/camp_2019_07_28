life=3
life-=1
print(life)
life-=1
life-=1
if life>0:
    life-=1
elif life==0:
    print("The player has zero life")
else:
    print("The player ran out of life!")
print(life)