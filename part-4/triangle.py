# Copy here code of line function from previous exercise
def line(num, txt):
    if txt == "":
        print("*" * num)
    else:
        print(txt[0] * num)

def triangle(size):
    # You should call function line here with proper parameters
    i = 0
    while i <= size:
        line(i, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
