# Write your solution here
num = int(input("Width:"))
row = ""

while num > 0:
    row += "#"
    num -= 1

print(row)