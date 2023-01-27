# Write your solution here

while True:
    num = int(input("Please type in a number:"))
    i_num = num
    if num <= 0:
        break
    fac = 1
    while num > 0:
        fac *= num
        num -= 1
    print(f"The factorial of the number {i_num} is {fac}")
print("Thanks and bye!")