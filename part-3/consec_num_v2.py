# Write your solution here
lim = int(input("Limit: "))
sum = 0
i = 1
sentence = "The consecutive sum: "

while sum < lim :
    sum += i
    sentence += str(i)
    if sum < lim:
        sentence += ' + '
    i += 1

print(sentence + " =", sum)