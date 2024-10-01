"""#input
cost = float(input("How much was your food? "))
#variables
tip = 0.15 * cost
tax = .007 * cost
total = cost + tip + tax
#print
print ("Food cost: ", round(cost,2))
print ("Tip amount: ", round(tip,2) )
print ("Sales tax: ", round(tax,2) )
print ("Total cost: ", round(total,2))
"""


"""#constant
COOKIES_PER_RECIPE = 48
SUGAR_PER_RECIPE = 1.5
BUTTER_PER_RECIPE = 1
FLOUR_PER_RECIPE = 2.75

#input
cookies_needed = int(input("How many cookies do you want to make? "))

#cookie calculation
ingredient_scale = (cookies_needed / COOKIES_PER_RECIPE)

#ingredient calculation
sugar_needed = SUGAR_PER_RECIPE * ingredient_scale
butter_needed = BUTTER_PER_RECIPE * ingredient_scale
flour_needed = FLOUR_PER_RECIPE * ingredient_scale

# Display ingredients
print("To make ", cookies_needed," cookies, you'll need:")
print("Sugar: ",round(sugar_needed,2), "cups")
print("Butter: ", round(butter_needed,2)," cups")
print("Flour: ", round(flour_needed,2)," cups")
"""
"""
#user input for rectangle 1
length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))

#user input for rectangle 2
length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))

# Calculate the area of rectangles
area1 = length1 * width1
area2 = length2 * width2

# Compare the areas
if area1 > area2:
    print("The first rectangle has a greater area.")
if area2 > area1:
    print("The second rectangle has a greater area.")
if area1 == area2:
    print("The two rectangles have the same area.")
    """
    
"""
#user input
user_input = int(input("Enter a number in the range of 1 through 7: "))

#compare num to day
if user_input == 1:
    day = "Monday"
if user_input == 2:
    day = "Tuesday"
if user_input == 3:
    day = "Wednesday"
if user_input == 4:
    day = "Thursday"
if user_input == 5:
    day = "Friday"
if user_input == 6:
    day = "Saturday"
if user_input == 7:
    day = "Sunday"

# Display day or error message
if user_input >= 1 and user_input <= 7:
    print("The corresponding day of the week is:", day)
else:
    print("Error: Please enter a number in the range of 1 through 7.")
    """
    
"""  
if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
"""

"""
#Question 6: A
#User input

points = int(input("Enter an integer number: "))

# Check point value and display response
if points < 9 or points > 51:
    print("Invalid points.")
if points > 9 or points <51:
    print("Valid points.")
    
#Question 6: B
#User input
points = int(input("Enter an integer number: "))

# Check point value and display response
if points < 9 or points > 51:
    print("Invalid points.")
else:
    print("Valid points.")
"""

#Question 7: A
#user input
num = int(input("Enter a number between 1 and 10: "))

# Compare range
if 1 <= num <= 10:
    # Convert to roman numerals
    if num == 1:
        roman_numeral = "I"
    if num == 2:
        roman_numeral = "II"
    if num == 3:
        roman_numeral = "III"
    if num == 4:
        roman_numeral = "IV"
    if num == 5:
        roman_numeral = "V"
    if num == 6:
        roman_numeral = "VI"
    if num == 7:
        roman_numeral = "VII"
    if num == 8:
        roman_numeral = "VIII"
    if num == 9:
        roman_numeral = "IX"
    if num == 10:
        roman_numeral = "X"
    
    # Display the Roman numeral
    print(f"The Roman numeral for {num} is {roman_numeral}")
else:
    # Display an error message if the input is outside the range
    print("Error: Please enter a number between 1 and 10.")
    
#Question 7: B
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



