monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your monthly expenses:"))

#Calculating monthly savings
monthly_savings = monthly_expenses - monthly_income

#Projecting annual savings
interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)