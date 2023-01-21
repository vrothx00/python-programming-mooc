# Please write a program which asks the user for a word and then prints out the number of characters, 
# if there was more than one typed in.

word = input("Please type in a word: ")
l_word = len(word)
if (l_word > 1):
	print(f"There are {l_word} letters in the word hey")
print("Thank you!")