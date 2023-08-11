# Example 1: If-Else Statement
# Check if a number is positive, negative, or zero

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Example 2: For Loop
# Print numbers from 1 to 5

for i in range(1, 6):
    print(i)

# Example 3: While Loop
# Print numbers from 1 to 5 using a while loop

i = 1
while i <= 5:
    print(i)
    i += 1

# Example 4: Function
# Calculate the square of a number

def square(num):
    return num ** 2

result = square(5)
print("Square:", result)

# Example 5: List
# Create a list of fruits and iterate over it

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

# Example 6: Dictionary
# Create a dictionary of student names and their ages

students = {
    "John": 20,
    "Jane": 22,
    "Tom": 19
}

for name, age in students.items():
    print(name, "is", age, "years old.")

# Example 7: File Handling
# Read and write data to a file

# Write data to a file
with open("data.txt", "w") as file:
    file.write("Hello, World!")

# Read data from a file
with open("data.txt", "r") as file:
    data = file.read()
    print("Data from file:", data)
