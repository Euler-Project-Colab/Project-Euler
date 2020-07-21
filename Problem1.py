
"""
Program to print out sum of all multiples of three or five below 1000
"""
divisibleby3 = []
divisibleby5 = []
number = 0
for i in range(1000) :
    if number % 3 == 0 and number % 5 !=0:
        divisibleby3.append(number)
    elif number % 5 == 0 and number % 3 !=0:
        divisibleby5.append(number)
    elif number %5 == 0 and number % 3 == 0:
        divisibleby3.append(number)
    number += 1

finallist = divisibleby3  + divisibleby5
sumofdivisible = 0
for item in finallist:
    sumofdivisible += item

print(sumofdivisible)
