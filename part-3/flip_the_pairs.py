# Write your solution here
num = int(input("Please type in a number:"))
erste = 1
zweite = 2
 
while num > zweite or num == zweite:
    print(zweite)
    print(erste)
    zweite += 2
    erste += 2
    
if erste >= num and num % 2 != 0:
    print(erste)
