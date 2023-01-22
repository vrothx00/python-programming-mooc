# Please write a program which asks the user for three letters. 
# The program should then print out whichever of the three letters would be 
# in the middle if the letters were in alphabetical order.

# Write your solution here
letter1 = input("1st letter:")
letter2 = input("2nd letter:")
letter3 = input("3rd letter:")
middle = letter2

if (letter1 < letter2 < letter3) or (letter3 < letter2 < letter1):
    middle = letter2

if (letter2 < letter1 < letter3) or (letter3 < letter1 < letter2):
    middle = letter1

if (letter2 < letter3 < letter1) or (letter1 < letter3 < letter2):
    middle = letter3

print(f"The letter in the middle is {middle}")