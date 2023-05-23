# Earned amounts for each item
earned_amounts = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80
}

# Print earned amounts
print("Earned amount:")
for item, amount in earned_amounts.items():
    print(f"{item}: ${amount}")

# Total earnings
total_earnings = sum(earned_amounts.values())
print("\nIncome:", total_earnings)

# Staff expenses
staff_expenses = int(input("Staff expenses: "))

# Other expenses
other_expenses = int(input("Other expenses: "))

# Calculate net income
net_income = total_earnings - staff_expenses - other_expenses

# Print net income
print("Net income: $" + str(net_income))
