#functions 

"""
def message():
    print("Hello world")
    
    
for i in range(0,5):
    message()

"""

#Main function
"""
def main():
    print("Your name is ")    
    name()
    print("your major is ")
    major()
    
#Define name and major
def name():
    print("Corban")  
        
def major():
    major = (input("What is your major"))   
    
main()
   """
   
"""  

def main():
    print("Cup converter")
    value = int(input("how many cups do you need: "))
    convert(value)
    
def convert(fluid):
    result = fluid * 28.0
    print(result)
    
main()
"""
"""
total = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    elif number < 0:
        continue
    total += number
print(f"Sum: {total}")
"""

"""
import random
num1 = random.randint(1,6)
num2 = random.randint(1,6)


while(num1!=num2):
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
 
    print(num1,' ', num2)
    """
    

"""
def sum():
    import random
    num1= random.randint(1,100) 
    print(num1)
    if (num1 % 2 == 0):
        print ("Even")
    else:
        print("Odd")    
        

sum()
    """
    

"""
def small():
    import random
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    print(num1)
    print(num2)
    if (num1 < num2):
        print(num1, "is smaller") 
    else :
        print(num2, "is smaller")
        
small()
"""

