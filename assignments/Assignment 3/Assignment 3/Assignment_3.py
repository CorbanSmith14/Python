
#1 A

# user input
num = int(input("Enter a number within the range of 1 through 10: "))

# Compare range
if num >= 1 and num <= 10:
    # Convert to Roman numeral
    if num == 1:
        roman_numeral = "I"
    elif num == 2:
        roman_numeral = "II"
    elif num == 3:
        roman_numeral = "III"
    elif num == 4:
        roman_numeral = "IV"
    elif num == 5:
        roman_numeral = "V"
    elif num == 6:
        roman_numeral = "VI"
    elif num == 7:
        roman_numeral = "VII"
    elif num == 8:
        roman_numeral = "VIII"
    elif num == 9:
        roman_numeral = "IX"
    else:
        roman_numeral = "X"

    # Display the Roman numeral
    print(f"The Roman numeral for {num} is {roman_numeral}")
else:
    # Display an error message
    print("Error: Number must be within the range of 1 through 10.")
    
#2 B
""" I prefer the if-elif-else statement as it presents a much 
cleaner code that is easier to read"""

#2
# User input
pocket_number = int(input("Enter a pocket number (0-36): "))

# number range
if 0 <= pocket_number <= 36:
    # Determine color
    if pocket_number == 0:
        color = "green"
    elif 1 <= pocket_number <= 10:
        color = "red" if pocket_number % 2 == 1 else "black"
    elif 11 <= pocket_number <= 18:
        color = "black" if pocket_number % 2 == 0 else "red"
    elif 19 <= pocket_number <= 28:
        color = "red" if pocket_number % 2 == 1 else "black"
    elif 29 <= pocket_number <= 36:
        color = "black" if pocket_number % 2 == 0 else "red"

    # Display pocket color
    print(f"The pocket {pocket_number} is {color}.")
else:
    # Error message
    print("Error: Pocket number must be between 0 and 36.")
    
#3
# User input
name = input("Enter your name: ")
age = input("Enter your age: ")

# Display name and age
message = f"Hello, {name}! You are {age} years old."
print(message)


#4

# Exchange rates
usd_to_eur = 0.85
usd_to_gbp = 0.74
usd_to_jpy = 111.2

# User input
usd_amount = float(input("Enter the amount in USD: "))

# Convert to other currencies
eur_amount = usd_amount * usd_to_eur
gbp_amount = usd_amount * usd_to_gbp
jpy_amount = usd_amount * usd_to_jpy

# Display amounts
print(f"{usd_amount:.2f} USD is equivalent to:")
print(f"{eur_amount:.2f} EUR")
print(f"{gbp_amount:.2f} GBP")
if jpy_amount > 999:
    print(f"{jpy_amount:,.2f} JPY")
else:
    print(f"{jpy_amount:.2f} JPY")

    
#5

# Initialize student
students = []

# For loop and range 
for i in range(3):
    name = input("Enter student name: ")
    gpa = float(input("Enter GPA: "))
    students.append((name, gpa))

# Sort the students list in descending order by GPA
students.sort(key=lambda x: x[1], reverse=True)

# Print GPA and Table
print("Student GPA Report:")
print(f"{'Name':<15}{'GPA':<5}")
print("-" * 22)

for name, gpa in students:
    print(f"{name:<15}{gpa:.2f}")



#6

# Initialize name
names = []

# User input
for i in range(4):
    name = input(f"Enter the {i + 1} name: ")
    names += [name]  # Use the '+' operator to concatenate the lists

# Sort names + alphabetical order (ignoring case sensitive)
names.sort(key=lambda x: (x[0].lower(), x))

# Display names
print("The names in alphabetical order are:", ", ".join(names))


