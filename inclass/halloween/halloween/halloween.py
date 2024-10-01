"""
import requests

result = requests.get("https://climate.nasa.gov/vital-signs/carbon-dioxide/")

html = result.txt

co2 = html.split('''</span>
</div>
<div class='value'>''', 1)[1].strip().split('\n')[0]

print(f"C02 = {co2.strip()} PPM.")
"""


#dictionary
"""
stds = {
    123: "john",
    456: "mark",
    789: "Mia"
    
    }
#add student

stds[900] = "Shawn"

#delete student

del stds[456]


print(stds[900])

"""

#iterrate over dictionary

#1
for k in stds: 
    print(k, stds[k]) 
    
#2
for k in stds.keys():
    print(k, stds[k])    

#3
stds.items()    
for i in li:
    print(i[0],i[1])  
#4

for k,v in stds.items():
    print(k,v)    
