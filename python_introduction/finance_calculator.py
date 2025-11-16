monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your monthly expenses:"))

#Calculating monthly savings
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are", monthly_savings)
#Projecting annual savings
interest_rate = 0.05
projected_savings = monthly_savings * 12 + monthly_savings * 12 * 0.05
print("Projected savings after one year, with interest, is:", projected_savings)