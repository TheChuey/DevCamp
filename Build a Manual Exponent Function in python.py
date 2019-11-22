import math

from functools import reduce
"""
manual_exponent(2,3)
#>8
manual_exponent(10,2)
#>100
"""

def manual_exponent(r, y):
    for x in range(y):
        a = r * r
        answear = a * x
    print (answear)   
   

print (manual_exponent(2,3))
print (manual_exponent(10,2))


#  return math.pow(x,y) 
#  return  return x**y




