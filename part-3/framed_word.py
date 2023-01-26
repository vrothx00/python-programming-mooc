# Write your solution here

wrd = input("Word: ")
print("*" * 30)
start_space = (28 - len(wrd)) // 2
end_space = start_space

if len(wrd) % 2 != 0:
	end_space += 1
print("*" + " " * start_space + wrd + " " * end_space + "*")
print("*" * 30)