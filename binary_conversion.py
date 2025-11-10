n=int(input("Enter the number"))
binary= bin(n)[2:]
ones_grp= binary.split("0")
max_one= max(len(group) for group in ones_grp)
print(max_one)