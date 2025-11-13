cube= lambda x: x**3
seq=[0,1]

def fibonacci(n):
    for i in range(2,n+1):
        seq.append(seq[-1]+seq[-2])

        return seq[:n]
n=int(input("Enter the number"))
print(list(map(cube, fibonacci(n))))

