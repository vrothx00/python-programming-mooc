while True:
	name = input("Editor:")
	if name.lower() == "emacs" or name.lower() == "vim" or name.lower() == "atom":
		print("not good")
	elif name.lower() == "word" or name.lower() == "notepad":
		print("awful")
	elif name.lower() == "visual studio code":
		print("an excellent choice")
		break