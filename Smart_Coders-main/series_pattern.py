#1.fibonacci series

n = int(input("enter value of n : "))
a,b=0,1

for i in range (n):
    print(a,end=" ")
    a,b =b,a+b
print()

#2.compute sum num
a = int(input("enter a : "))
for i in range (1,a+1):
    sum = sum + 1/i
    print(sum)
