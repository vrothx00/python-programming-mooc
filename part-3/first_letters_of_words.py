sentence = input("Please type in a sentence:")

i = 0
print(sentence[i])
while i < len(sentence):
    if sentence[i] == " ":
        print(sentence[i+1:i+2])
    i += 1