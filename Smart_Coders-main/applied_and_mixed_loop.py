#1.Print the multiplication table of a given number
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

#2.Find the sum of even and odd numbers separately from 1 to N
n = int(input("Enter N: "))
even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Sum of evens:", even_sum)
print("Sum of odds:", odd_sum)

#3.Check if a number is an Armstrong number (generalized for any digits)
n = int(input("Enter a number: "))
digits = str(n)
power = len(digits)
total = sum(int(d) ** power for d in digits)
print(f"{n} is {'an Armstrong' if total == n else 'not an Armstrong'} number")

#4.Find the largest and smallest digit in a number
n = int(input("Enter a number: "))
digits = str(abs(n))
largest = max(digits)
smallest = min(digits)
print("Largest digit:", largest)
print("Smallest digit:", smallest)

#5.Print all factors / divisors of a number
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()

#6.Check if a number is a perfect number (sum of divisors == number)
n = int(input("Enter a number: "))
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
print(f"{n} is {'a perfect' if total == n else 'not a perfect'} number")

#7.Convert decimal to binary
n = int(input("Enter a decimal number: "))
if n == 0:
    binary = "0"
else:
    binary = ""
    temp = n
    while temp > 0:
        binary = str(temp % 2) + binary
        temp //= 2
print("Binary:", binary)

#8.Convert binary to decimal
binary = input("Enter a binary number: ")
decimal = 0
for digit in binary:
    decimal = decimal * 2 + int(digit)
print("Decimal:", decimal)

#9.Read numbers until user enters -1, print the count and average
count = 0
total = 0
while True:
    n = float(input("Enter a number (-1 to stop): "))
    if n == -1:
        break
    count += 1
    total += n

if count > 0:
    print("Count:", count)
    print(f"Average: {total / count:.2f}")
else:
    print("No numbers entered")

#10.Find the sum of a series: x - x^3/3! + x^5/5! - x^7/7! ... (sin series)
x = float(input("Enter x (in radians): "))
n_terms = int(input("Enter number of terms: "))

result = 0
sign = 1
for i in range(n_terms):
    power = 2 * i + 1
    factorial = 1
    for j in range(1, power + 1):
        factorial *= j
    term = (x ** power) / factorial
    result += sign * term
    sign *= -1

print(f"sin({x}) approx = {result:.6f}")

#11.Palindrome Check: Check whether a string is a palindrome using recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

s = input("Enter a string: ")
print(f"'{s}' is {'a palindrome' if is_palindrome(s) else 'not a palindrome'}")

#12.Count Vowels: Count the number of vowels in a string using recursion
def count_vowels(s):
    if len(s) == 0:
        return 0
    first = 1 if s[0].lower() in 'aeiou' else 0
    return first + count_vowels(s[1:])

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))

#13.def count_vowels(s):
    if len(s) == 0:
        return 0
    first = 1 if s[0].lower() in 'aeiou' else 0
    return first + count_vowels(s[1:])

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))

#14.Increasing + Decreasing: Using a single recursive function, print increasing then decreasing
    if i > n:
        return
    print(i, end=" ")
    print_inc_dec(i + 1, n)
    print(i, end=" ")

n = int(input("Enter N: "))
print_inc_dec(1, n)
print()
def print_inc_dec(i, n):
    if i > n:
        return
    print(i, end=" ")
    print_inc_dec(i + 1, n)
    print(i, end=" ")

n = int(input("Enter N: "))
print_inc_dec(1, n)
print()
