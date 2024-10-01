"""
file_ptr = open("tds_info.txt", "a")


file_ptr.write("123 Alex 2.8\n")
file_ptr.write("122 Kevin 3.2\n")

file_ptr.close()
"""
"""
file_out = open("number.txt", "w")

for i in range(1,11):
    file_out.write(f"{i} \n")

file_out.close()
"""

file_in = open("number.txt" , "r")



"""
sum = 0
for line in file_in:
    sum += int(line.strip())
    
print(sum)
"""
"""
number = file_in.readlines()
sum = 0
for num in number:
    j = int(num.strip())
    sum += j

print(sum)

"""  
"""
number = int(file_in.readline().strip())
while (number != ""):
    print(number)
    number = int(file_in.readline().strip())
"""
file_in.close()