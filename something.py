name = input("What's your name? ")
print(f"Hi {name}!")
given = input("Now give me an Integer!")
given = int(given)

nameLength = int(len(name))
if (nameLength<given):
    print("Your name has "+str(nameLength)+" characters, which is less than your given integer's value.")
elif (nameLength>given):
    print("Your name has "+str(nameLength)+" characters, which is more than your given integer's value.")
elif (nameLength==given):
    print("Your name has "+str(nameLength)+" characters, which is the same as your given integer's value.")
else:
    print("Oops, this isn't supposed to happen!")