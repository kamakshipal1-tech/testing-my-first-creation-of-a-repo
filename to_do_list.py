

tasks=["7","8","9","10","11","12"]
while True:
    print("\n to do list")
    print("1: Add task")
    print("2: Delete task")
    print("3: View tasks")
    print("4: Exit")
    choice = input()
    if choice == "1":
        task = input("Enter task name: ")
        tasks.append(task)
        print("Task added")
    elif choice == "2":
        if not tasks:
            print("no tasks are there to delete")
        else:
            num=int(input("Enter task number: "))
            if 0<=num<len(tasks):
                removed=tasks.pop(num-1)
                print("Task removed")
            else:
                print("invalid task no")
    elif choice == "3":
        if not tasks:
            print("Empty list")
        else:
            for i,task in enumerate(tasks):
                print(i,tasks)
    elif choice == "4":
        print("Exiting")
        break
else:
    print("Invalid operation")

