#Assignment 6
#Corban Smith



#question 1
#prime numbers
"""
def is_prime(n):
    if n <= 1:
        return False  # prime

    if n <= 3:
        return True  # prime

    if n % 2 == 0 or n % 3 == 0:
        return False  # prime

    if n == 5:
        return True
    if n == 7: 
        return True

def main():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

main()
"""

#question 2
#date format
"""
#months
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Input
date_str = input("Enter a date (mm/dd/yyyy): ")

# Split month, day, and year
parts = date_str.split('/')
if len(parts) != 3:
    print("Invalid date format. Please use mm/dd/yyyy.")
else:
    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])
    
    # Check range
    if 1 <= month <= 12 and 1 <= day <= 31 and 0 <= year <= 9999:
        # Format date
        month_name = months[month - 1]
        formatted_date = f"{month_name} {day}, {year}"
        
        # Display
        print("Formatted date: " + formatted_date)
    else:
        print("Invalid date.")
"""

#question 3
#copy string
"""
#capitilization function
def capitalize_first_char_of_sentences(input_string):
    # Split string
    sentences = input_string.split('. ')
    
    # list 
    modified_sentences = []

    for sentence in sentences:
        # Capitalize the first character of each sentence and add it to the list.
        modified_sentence = sentence[0].upper() + sentence[1:]
        modified_sentences.append(modified_sentence)

    # Join modified strings into single string.
    modified_string = '. '.join(modified_sentences)

    return modified_string

# user input
user_input = input("Enter a string: ")

# Call function 
result = capitalize_first_char_of_sentences(user_input)

# Display.
print("Modified String:")
print(result)
"""

#question 4
#rock paper scissors
"""
import random

def get_computer_choice():
    # copmuter choice
    computer_choice_num = random.randint(1, 3)
    if computer_choice_num == 1:
        return "rock"
    elif computer_choice_num == 2:
        return "paper"
    else:
        return "scissors"

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors) or 'quit to exit: ")
        
        if player_choice == "quit":
            break

        valid_choices = ["rock", "paper", "scissors"]
        if player_choice in valid_choices:
            computer_choice = get_computer_choice()
            print(f"Computer chose {computer_choice}")
            
            result = determine_winner(player_choice, computer_choice)
            print(result)
        else:
            print("Invalid choice. Please choose from rock, paper, or scissors.")

main()

"""

#question 5
#
"""
# remove unwanted characters
def clean_data(text):
    cleaned_text = []
    for line in text:
        cleaned_text.append(line)
    return cleaned_text

# location in cleaned text
def find_word_location(cleaned_text, word):
    page_number, line_number = 1, 1
    for line in cleaned_text:
        words = line.split()
        if word in words:
            word_number = words.index(word) + 1
            return f"{page_number}.{line_number}.{word_number}"
        line_number += 1
        if line_number > 10:
            line_number = 1
            page_number += 1
    return None  # Word not found

# decrypt location + retrieve word
def decrypt_location(cleaned_text, location):
    parts = location.split(".")
    if len(parts) != 3:
        return "???"
    
    page_number, line_number, word_number = int(parts[0]), int(parts[1]), int(parts[2])
    
    if page_number < 1 or page_number > len(cleaned_text) // 10 + 1:
        return "???"
    
    page_index = page_number - 1
    
    if line_number < 1 or line_number > 10:
        return "???"
    
    line_index = line_number - 1
    
    lines = cleaned_text[page_index * 10:(page_index + 1) * 10]
    if line_index >= len(lines):
        return "???"
    
    words = lines[line_index].split()
    
    if word_number < 1 or word_number > len(words):
        return "???"
    
    return words[word_number - 1]

def main():
    # Read
    with open("book1.txt", "r") as file:
        text = file.read().splitlines()
        cleaned_text = clean_data(text)

    #main
    while True:
        print("Choose an option:")
        print("(a) Encrypt a message")
        print("(b) Decrypt a message")
        print("(c) Exit")
        choice = input("Enter your choice: ")

        if choice == "a":
            message = input("Enter a message: ")
            words = message.split()
            result = []
            for word in words:
                location = find_word_location(cleaned_text, word)
                result.append(location if location else "?.?.?")
            print(" ".join(result))

        elif choice == "b":
            locations = input("Enter locations: ").split()
            result = []
            for location in locations:
                word = decrypt_location(cleaned_text, location)
                result.append(word)
            print(" ".join(result))

        elif choice == "c":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose (a), (b), or (c).")

main()


"""
