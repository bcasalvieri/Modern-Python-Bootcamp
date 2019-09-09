# ask for age
age = input("How old are you? ")

if age:
    age = int(age)
    if age >= 21:
        print("You are good to enter and drink!")
    elif age >= 18:
        print("You can enter, but you need a wristband!")
    else:
        print("You can't come in, little one! :(")
else:
    print("Please enter a valid age")
