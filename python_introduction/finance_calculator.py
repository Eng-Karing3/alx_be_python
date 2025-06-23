
monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - total_monthly_expenses
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_annual_savings = annual_savings + interest

print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_annual_savings)}.")
