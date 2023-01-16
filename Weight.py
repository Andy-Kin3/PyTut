weight = float(input("Enter your weight: "))
weightType = input("Enter type either lbs(Pounds) or kg(kilograms): ")

if weightType == "lbs":
    print(f"Your weight is {weight} in lbs")
    print(f"{weight / 2.205} in kg")
elif weightType == "kg":
    print(weight)
    print(f"{weight * 2.205}")
else:
    print("This is not a valid weight type")