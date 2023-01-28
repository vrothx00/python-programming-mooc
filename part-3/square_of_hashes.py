# Write your solution here
def hash_square(num):
    row = "#" * num
    while num > 0:
        print(row)
        num -= 1
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)