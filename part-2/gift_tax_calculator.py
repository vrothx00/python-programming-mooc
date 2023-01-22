# Some say paying taxes makes Finns happy, so let's see if the secret of happiness lies in one of 
# the taxes set out in Finnish tax code.

# According to the Finnish Tax Administration, a gift is a transfer of property to another 
# person against no compensation or payment. If the total value of the gifts you receive 
# from the same donor in the course of 3 years is €5,000 or more, you must pay gift tax.

# Write your solution here
value = int(input("Value of gift: "))
tax = 100.0

if value < 5000:
    print("No tax!")
elif value == 5000:
    print(f"Amount of tax: {tax} euros")
elif value > 5000 and value < 25000:
    tax = (100 + (value - 5000) * 0.08)
    print(f"Amount of tax: {tax} euros")
elif value > 25000 and value < 55000:
    tax = (1700 + (value - 25000) * 0.10)
    print(f"Amount of tax: {tax} euros")
elif value > 55000 and value < 200000:
    tax = (4700 + (value - 55000) * 0.12)
    print(f"Amount of tax: {tax} euros")
elif value > 200000 and value < 1000000:
    tax = (22100 + (value - 200000) * 0.15)
    print(f"Amount of tax: {tax} euros")
elif value > 1000000:
    tax = (142100 + (value - 1000000) * 0.17)
    print(f"Amount of tax: {tax} euros")