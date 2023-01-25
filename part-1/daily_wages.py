# Write your solution here
wage = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")
d_wages = wage * hours
if day == 'Sunday':
    d_wages *= 2

print(f"Daily wages: {d_wages} euros")