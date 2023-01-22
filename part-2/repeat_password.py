# Please write a program which asks the user for a password. 
# The program should then ask the user to type in the password again. 
# If the user types in something else than the first password, 
# the program should keep on asking until the user types the first password again correctly.

# Write your solution here
passw = input("Password:")

while True:
    r_pass = input("Repeat password:")

    if passw != r_pass:
        print("They do not match!")
    else:
        print("User account created!")
        break