# Write your solution here
def squared(txt, num):
    row = txt * num ** 2
    i = num
    first = 0
    last =  i
    while num > 0:     
        print(row[first:last])
        first += i
        last += i
        num -= 1


if __name__ == "__main__":
    squared("ab", 3)