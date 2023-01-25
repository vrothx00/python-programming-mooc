# Write your solution here
num = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
money = float(input("How much money do you spend on groceries in a week? "))
print("\n")
print("Average food expenditure:")
print(f"Daily: {(num * price + money) / 7} euros")
print(f"Weekly: {num * price + money} euros")