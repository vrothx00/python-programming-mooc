# Please write a program which keeps asking the user for a PIN code until they type 
# in the correct one, which is 4321. 
# The program should then print out the number of times the user tried different codes.

# Write your solution here
attempts = 0

while True:
    pin = int(input("PIN:"))
    attempts += 1
    if pin == 4321:
        break
    print("Wrong")

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")