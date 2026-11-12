
# ==========================================
# DAY 4 - PYTHON PRACTICE
# Topics: Nested Loops, Patterns, Strings,
# Prime Numbers, Lists and Number Logic
# ==========================================


# 1. Sum of Even Numbers (1 to 50)

total = 0

for i in range(1, 51):
    if i % 2 == 0:
        total += i

print("Sum of even numbers:", total)


# 2. Negative Indexing in Lists

numbers = [1, 2, 3, 4, 5]

print("Last element:", numbers[-1])
print("Third last element:", numbers[-3])


# 3. Reverse a String

text = "Python"

reverse = text[::-1]

print("Original string:", text)
print("Reversed string:", reverse)


# 4. Nested Loops - Rectangle Pattern

for i in range(1, 4):
    for j in range(1, 3):
        print("*", end=" ")
    print()


# 5. Right Triangle Pattern

for i in range(1, 6):
    print("* " * i)


# 6. Inverted Triangle Pattern

for i in range(5, 0, -1):
    print("* " * i)


# 7. Prime Number Checker

n = 17
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(n, "is a Prime Number")
else:
    print(n, "is not a Prime Number")


# 8. Print Prime Numbers from 1 to 50

print("Prime numbers from 1 to 50:")

for num in range(2, 51):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

print()


# 9. Multiplication Table

n = 5

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# 10. Count Vowels in a String

text = "programming"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Total vowels:", count)


# 11. Find Sum of Digits

n = 12345
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print("Sum of digits:", total)


# 12. Check Palindrome

word = "madam"

if word == word[::-1]:
    print(word, "is a Palindrome")
else:
    print(word, "is not a Palindrome")


print("\nDay 4 Python Practice Completed!")
