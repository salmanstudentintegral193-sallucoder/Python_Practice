
# ==========================================
# DAY 3 - PYTHON PRACTICE
# Topics: Variables, Data Types, Loops,
# Conditions, Lists, Strings and Functions
# ==========================================


# 1. Basic Arithmetic
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# 2. Floor Division
print("Floor Division:", 10 // 3)


# 3. Data Types
name = "Python"
age = 20
marks = 95.5

print(type(name))
print(type(age))
print(type(marks))


# 4. String Repetition
x = "Python"
print(x * 3)


# 5. If-Else Condition
x = 15

if x > 10:
    print("Hello")
else:
    print("Bye")


# 6. For Loop
for i in range(1, 5):
    print(i)


# 7. List Indexing
numbers = [10, 20, 30, 40]
print("List element:", numbers[2])


# 8. List Append and Length
fruits = ["apple", "banana", "mango"]
fruits.append("orange")

print(fruits)
print("Total fruits:", len(fruits))


# 9. Even or Odd
n = 7

if n % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# 10. While Loop
i = 1

while i <= 10:
    print(i)
    i += 1


# 11. Square Function
def square(n):
    return n ** 2

print("Square:", square(5))


# 12. Addition Function
def add(a, b):
    return a + b

print("Sum:", add(2, 5))


# 13. Find Maximum Number
numbers = [12, 45, 7, 89, 23]

print("Maximum number:", max(numbers))


# 14. String Slicing
x = "Python"
print("Sliced string:", x[0:3])


# 15. Positive, Negative or Zero
n = -5

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


# 16. Even Numbers Using Range
for i in range(2, 10, 2):
    print(i)


# 17. List and Tuple
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# List is mutable
my_list[0] = 10

# Tuple is immutable
print(my_list)
print(my_tuple)


print("\nDay 3 Python Practice Completed!")
