"""
file_in = open ("numbers.txt", 'w')

file_in.write("10\n32\n43\n")


file_in.close()
"""

file_in = open("numbers.txt", 'r')

number1 = int(file_in.readline().strip())
number2 = int(file_in.readline().strip())
number3 = int(file_in.readline().strip())

if number1 > number2:
    number1,number2 = number2,number1 
    
if number2 > number3:
    number2,number3 = number3,number2 
    
if number1 > number2:
    number1,number2 = number2,number1 

print(number1)
print(number2)
print(number3)

file_in.close()

file_in = open("nubers.txt", "w")

file_in.write("number1\nnumber2\number2\n")

file_in.close()

