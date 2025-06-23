
monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - total_monthly_expenses
print(f"Your monthly savings are ${monthly_savings:.2f}")

projected_annual_savings = monthly_savings * 12 * 1.05
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}")

