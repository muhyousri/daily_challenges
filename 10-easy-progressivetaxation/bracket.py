"""
Input your brakets here 

example : 
income cap      marginal tax rate
  ¤10,000           0.00 (0%)
  ¤30,000           0.10 (10%)
 ¤100,000           0.25 (25%)
    --              0.40 (40%)

is equivilant to 

brackets = {10000:0,30000:0.10,100000:0.25,over:0.40}
"""




brackets = {10000:0,30000:0.10,100000:0.25,'over':0.40}