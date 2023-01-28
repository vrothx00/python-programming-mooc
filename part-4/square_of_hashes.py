# Copy here code of line function from previous exercise
def line(num, txt):
    if txt == "":
        print("*" * num)
    else:
        print(txt[0] * num)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    i = size
    while size > 0:
        line(i, "#")
        size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
