"""
The nation of Examplania has the following income tax brackets:

income cap      marginal tax rate
  ¤10,000           0.00 (0%)
  ¤30,000           0.10 (10%)
 ¤100,000           0.25 (25%)
    --              0.40 (40%)
If you're not familiar with how tax brackets work, see the section below for an explanation.

Given a whole-number income amount up to ¤100,000,000, find the amount of tax owed in Examplania. Round down to a whole number of ¤.

Examples
tax(0) => 0
tax(10000) => 0
tax(10009) => 0
tax(10010) => 1
tax(12000) => 200
tax(56789) => 8697
tax(1234567) => 473326




"""

def tax(income):
    if income <= 10000:
        tax = 0
    if income > 10000 and income <= 30000:
        tax = int(((income - 10000) * 0.10))
    if income > 30000 and income <= 100000 :
        tax = int(((income - 30000) * 0.25 ) + 2000)
    if income > 100000 :
        tax = int(((income - 100000) * 0.40 ) + 19500)

    return tax 
