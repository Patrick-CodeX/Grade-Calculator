

amount = True
Sgrades = []
Fgrades = []
Savg = 0.0
Favg = 0.0
averageCourseGrade = None
inputted = None
while amount == True:
    done = input("Summative Done? y/n ")
    if done.lower() != "y":
        if amount:
            Sgrades.append(float(input("Input a Grade ")))
    else:
        amount = False
amount = True
while amount == True:
    done = input("Formative Done? y/n ")
    if done.lower() != "y":
        if amount:
            Fgrades.append(float(input("Input a Grade ")))
    else:
        amount = False
for x in Sgrades:
    Savg += x
for x in Fgrades:
    Favg += x
Savg/=len(Sgrades)
Favg/=len(Fgrades)

averageCourseGrade = (Savg * 0.75) + (Favg * 0.25)

print("Your course average is", averageCourseGrade)
