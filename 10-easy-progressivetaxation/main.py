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
from bracket import *
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


# Optional - Getting values from a dict 

def tax_optional(income):
    cap1 = list(brackets.keys())[0]
    cap2 = list(brackets.keys())[1]
    cap3 = list(brackets.keys())[2]
    tax_cap1 = cap1 * brackets[cap1]
    tax_cap2 = (cap2 - cap1) * brackets[cap2]
    tax_cap3 = ((cap3 - cap2) * brackets[cap3]) + tax_cap2
    if income <= cap1:
        tax = brackets[cap1]
    if income > cap1 and income <= cap2:
        tax = int(((income - cap1) * brackets[cap1])+ tax_cap1)
    if income > cap2 and income <= cap3 :
        tax = int(((income - cap2) * brackets[cap3] ) + tax_cap2)
    if income > cap3 :
        tax = int(((income - cap3) *  brackets['over']) + tax_cap3)

    return tax 
