# Write your solution here
wrd = input("Please type in a word:")
letter = input("Please type in a character:")

position = wrd.find(letter)
end = position + 3
if len(wrd) > end:
    print(wrd[position:end])