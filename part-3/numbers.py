# Please write a program which asks the user for a number. 
# The program then prints out all integer numbers greater 
# than zero but smaller than the input.

# Write your solution here
num = int(input("Upper limit:"))
x = 1

while x > 0 and x < num:
    print(x)
    x += 1