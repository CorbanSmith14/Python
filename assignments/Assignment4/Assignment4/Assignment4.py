
#q1
"""
c = 0 
while ( c <= 1000 ):
    print(c)
    c += 10
    """
    
#q2
"""
factorial = 1
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    for c in range(1, n + 1):
        factorial *= c

    print(f"The factorial of {n} is {factorial}")
    """
    


#q3
"""
c = 1
while (c>=1):
    n=1
    while(n<=c):
        print('*', end = ' ')
    print ()
n = int(input("Enter a number: "))
c-=1
"""



#q4

num = int(input("Enter a number to check if it is prime: "))

if num <= 1:
    print("Not prime!")
else:
    is_prime = True
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime!")
    else:
        print("Not prime!")


