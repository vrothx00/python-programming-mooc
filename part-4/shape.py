# Copy here code of line function from previous exercise and use it in your solution
def line(num, txt):
    if txt == "":
        print("*" * num)
    else:
        print(txt[0] * num)

def shape(seize, char, base, b_char):
    i = 1
    y = seize
    while i <= seize:
        line(i, char)
        i += 1

    
    while base > 0:
        line(y, b_char)
        base -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")