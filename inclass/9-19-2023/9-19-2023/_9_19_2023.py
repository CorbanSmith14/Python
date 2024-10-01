"""
num = 124567.345
print (f'{num:<20,.2f}')
print (f'{num:^20,.2f}')
print (f'{num:>20,.2f}')
"""

#loops
num = 1

while (num <= 100000) :
    print(f'{num:,}')
    num = num + 1
    

   
keep_going = 1 <= 5  
while (keep_going == "y"):
    score1 = float(input("Enter the first score: "))
    score2 = float(input("Enter the second score: "))
    score3 = float(input("Enetr the third score: "))
    avg = (score1 + score2 + score3)/3
    print(f"your average score is: {avg}")
    keep_going += 1