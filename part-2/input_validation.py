from math import sqrt
# Write your solution here
freq = 0

while True:
    num = int(input("Please type in a number:"))

    if num > 0:
        print(sqrt(num))
    
    if num == 0:
        print("Exiting...")
        break
    
    if num <= 0:
        print("Invalid number")