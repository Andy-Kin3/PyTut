print("Pick a weighing unit between lbs(pounds) and kg(kilograms")
unit = input("Enter a unit: ")
weight = int(input("Enter your weight: "))
if unit == 'kg':
    print(f"You are {weight}kg and {weight / 0.454}lbs")
elif unit == 'lbs':
    print(f"You are {weight}lbs and {weight / 2.2046}kg")
else:
    print("You did not enter a correct value, run the program and try again.")