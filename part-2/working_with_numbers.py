# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
sum = 0
nums = 0
pos_nums = 0
neg_nums = 0


while True:
    num = int(input("Number: "))

    if num == 0:
        break
    
    if num > 0:
        pos_nums += 1
    
    if num < 0:
        neg_nums += 1

    nums += 1
    sum += num

print(f"Numbers typed in {nums}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / nums}")
print(f"Positive numbers {pos_nums}")
print(f"Negative numbers {neg_nums}")