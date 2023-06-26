#print("Let's find out your BMI ")
#print("Press E for Europe and A for Asia")
region = str(input("Which region do you live in ").lower())

length = input("Do you know your height in meters? ")

if length == 'n':
    ft =input("please enter your height in Feet ")
    ft = float(ft)
    length = ft
    height_in_ft= length/3.3
    print("your height in meters is " + str(height_in_ft))
weight = input("Do you know your weight in Kg ")
if weight == 'n':
    wt = float(input("Please enter your weight in Lbs "))

    weight = wt
    weight_in_lbs = wt*.4
    print("Your weight in Lbs is " , weight)
message = float(input("Enter your wight in Kg "))

height = float(input("Enter your height in meters "))

BMI = message/(height**2)
BMI = float(BMI)
print("Your BMI is ", BMI)
if region == 'E':
    if BMI <= 18.5:
        print("you are under weight")
    elif BMI >= 18.5 and BMI <= 24.9:
        print("Your BMI is normal")
    elif BMI >=25 and BMI <=29.9:
        print(" you are over weight")
    else:
        print("you are obese")
elif BMI <=18.5:
    print("you are under weight")
elif BMI >=18.5 and BMI <= 22:
    print("Your weight is normal")
elif BMI >= 23 and BMI <= 25:
    print("You are over weight")
else:
    print("You are obese")