# pattern_drawing.py

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Start row counter
row = 0

# While loop for rows
while row < size:
    # For loop for columns
    for col in range(size):
        print("*", end="")
    print()  # Move to next line
    row += 1
