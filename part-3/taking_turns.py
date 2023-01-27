last = int(input("Please type in a number:"))
first = 0

half = last // 2

while True:
    first += 1
    print(first)
    if first == last:
        break
    print(last)
    last -= 1
    if last == half:
        break