# Please write a program which asks the user for a floating point number 
# and then prints out the integer part and the decimal part separately.
#  Use the Python int function.

number = float(input("Please type in a number: "))
intpart = int(number)
decpart = number - intpart
print(f"Integer part: {intpart}")
print(f"Decimal part: {decpart}")