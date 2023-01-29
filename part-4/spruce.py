# Write your solution here
def sen():
    print("a spruce!")

def max_len(num):
    i = 1
    while num > 1:
        i += 2
        num -= 1
    half = i // 2
    return  half

def line(num, half):
    i = 1
    while num > 0:
        print(" " * half + "*" * i + " " * half)
        num -= 1
        half -= 1
        i += 2

def l_line(num, half):
    print(" " * half + "*" * 1 + " " * half)

def spruce(num):
    sen()
    h = max_len(num)
    line(num, h)
    l_line(num, h)



# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)