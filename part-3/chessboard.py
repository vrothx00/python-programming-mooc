# Write your solution here
def chessboard(num):
    i = 0
    y = 0
    f_row = ""
    fs_row = ""
    while i < num:
        if i % 2 == 0:
            f_row += "1"
            fs_row += "0"
        else:
            f_row += "0"
            fs_row += "1"
        i += 1
    
  
    
    while y < num:
        if y % 2 == 0:
            print(f_row)
        else:
            print(fs_row)
        y += 1

# Testing the function
if __name__ == "__main__":
    chessboard(3)