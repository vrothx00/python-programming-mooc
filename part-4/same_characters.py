# Write your solution here
def same_chars(txt, num1, num2):
    if num1 >= len(txt) or num2 >= len(txt):
        return False
    if txt[num1] == txt[num2]:
        return True
    return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 13))