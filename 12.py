# Question 12: Calculate income tax for the given income by adhering to the below rules
# Taxable Income	Rate (%)
# First $10,000	    0
# Next $10,000	    10
# The remaining	    20


def tax_calc(income):
    if income <= 10000:
        total_tax = 0
    elif income <= 20000:
        total_tax = (income - 10000)*.1
    else:
        # first 10000
        total_tax = 0

        # second 10000
        total_tax = (10000)*.1

        # rest
        total_tax = total_tax + (income-20000)*.2
    return total_tax


income = int(input("Please provide an income: "))
print("Your taxable amount is: " + str(tax_calc(income)))




