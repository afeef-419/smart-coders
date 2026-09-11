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


#3.alternting series
b = int(input("enter b : "))
t = 0
for i in range (1,b+1):
    if i % 2 == 0:
            t -= 1
    else :
         t-=1
print(t)


#4.power finding
x = float(input("Enter base x: "))
n = int(input("Enter exponent n: "))
result = 1
for _ in range(abs(n)):
    result *= x
if n < 0:
    result = 1 / result
print(f"{x}^{n} = {result}")

#5.factorial
n = int(input("Enter N: "))
total = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    total += factorial
print("Sum of factorials:", total)