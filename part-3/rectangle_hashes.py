# Write your solution here
num = int(input("Width:"))
rows = int(input("Height:"))
row = "#" * num

while rows > 0:
    print(row)
    rows -= 1