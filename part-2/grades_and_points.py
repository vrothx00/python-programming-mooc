# The table below outlines the grade boundaries on a certain university course. 
# Please write a program which asks for the amount of points received 
# and then prints out the grade attained according to the table.

# Write your solution here
points = int(input("How many points [0-100]:"))

if points > 100 or points < 0:
    print("Grade: impossible!")
elif points >= 90 and points <= 100:
    print("Grade: 5")
elif points >= 80 and points < 90:
    print("Grade: 4")
elif points >= 70 and points < 80:
    print("Grade: 3")
elif points >= 60 and points < 70:
    print("Grade: 2")
elif points >= 50 and points < 60:
    print("Grade: 1")
elif points >= 0 and points < 50:
    print("Grade: fail")