import random
while True:
    input("press enter to continue")
    roll=random.randint(1,6)
    print(roll)
    cont= input("Roll again?(y/n)?")
    if cont=='n':
           break
