#1.fibonacci series

n = int(input("enter value of n : "))
a,b=0,1

for i in range (n):
    print(a,end=" ")
    a,b =b,a+b
print()
