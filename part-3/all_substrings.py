# Write your solution here
# Write your solution here
wrd = input("Please type in a word:")
char = input("Please type in a character:")

idx = 0
while idx < len(wrd):
    if char == wrd[idx] and (len(wrd[idx:]) > 2):
        print(wrd[idx:idx+3])
    idx += 1