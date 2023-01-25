# Write your solution here
num = int(input("How many students on the course? "))
group = int(input("Desired group size? "))
groups = num % group
if groups == 0:
    print(f"Number of groups formed: {num // group}")
else:
    print(f"Number of groups formed: {(num // group) + 1}")