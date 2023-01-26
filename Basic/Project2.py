# Random Number Gussing Game Using Random Module:-

import random
num  = random.randrange(1,101)
userInput = int(input("Enter Your Number: "))
if userInput > num:
    print("computer number",num)
    print("Your guess number is too High")
elif userInput < num:
    print("computer number",num)
    print("Your guess number is too Low")
else:
    print("computer number",num)
    print("Your guess number is Equal")