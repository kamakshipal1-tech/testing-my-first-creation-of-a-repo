a=int(input())
b=int(input())
op=input()
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
      print(a*b)
elif op=='/':
      if(b!=0):
          print(a/b)
      else:
          print("Invalid division")
else:
    print("Invalid operation")
