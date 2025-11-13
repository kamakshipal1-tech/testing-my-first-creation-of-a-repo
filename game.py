a=13
guesscount=0
guesslimit=5
while guesscount < guesslimit:
    guess=int(input())
    guesscount=guesscount+1
    if guess==a:
       print("You won")
       break
    elif guess<a:
        print("Too low")
    else:
         print("Too high")
else:
     print("Invalid no")
