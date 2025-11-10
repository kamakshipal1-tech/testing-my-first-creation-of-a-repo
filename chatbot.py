responses={'hi':"Hello", "how are you?":"Good","bye":"Bye!"}
while True:
    choice = input("Enter your choice: ")
    if choice in responses:
        print(responses[choice])
        break
    else:
     print("invalid choice")
