#1
"""
for number in range(0, 1001, 10):
    print(number)

"""

#2

"""
square_size = int(input("Enter the square size (3-20): "))
if square_size < 3 or square_size >20:
    print("square size must be between 3 and 20.")  
else:
    for i in range(square_size):
        for j in range(square_size):
            if i == 0 or i == square_size - 1 or j == 0 or j == square_size - 1:
                print('*', end= ' ')
            else:
                print(' ', end=' ')
        print()
            
"""

#3 
"""
square_size = int(input("Enter the square size (3-20): "))

if square_size < 3 or square_size > 30:
    print("Square size must be between 3 and 30.")
else:
    for i in range(square_size):
        for j in range(square_size):
            if i == 0 or i == square_size - 1 or j == 0 or j == square_size - 1:
                print('*', end=' ')
            else:
                if j == i or j == square_size - 1:
                    print('#', end=' ')
                else:
                    print (' ', end=' ')
        print()
        
"""


#4
#incription/decription

#convert

def decrypt_letter(char, shift):
    if 'a' <= char <= 'z':
        return chr(((ord(char) - ord ('a') - shift) % 26) + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr(((ord(char) - ord ('A') - shift) % 26) + ord('A'))   
    else:
        return char    
    

#open wordlist
def wordlist(wordlist):
        with open(wordlist, 'r') as file:
            words = wordlist.read().splitlines()
    
#user input

message = input("Enter your encrytped text: " )
wordlist = wordlist('wordlist')

#shift amount

for shift in range(1, 26):
    decrypted = ""  
    for char in message:
        decrypted += decrypt_letter(char, shift)
        
#check list  
    words_in_message = decrypted.split()
    valid_words = [word for word in words_in_message if word in wordlist]
        
    if len(valid_words > len(words_in_message))/ 2:
        print(f"Decrypted message: {decrypted}")    
        print(f"Shift used: {shift} positions(s)")
        break;
    
else:
    print("Couldn't solve")
