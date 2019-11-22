from decimal import Decimal

product_cost = 88.80
commission_rate = 0.08
qty = 450

print(int(product_cost))
print(float(qty))
print(Decimal(product_cost))
print(complex(commission_rate))

# first example we take the product cost and convert it to an integer
# use float and pass in the quantity
# next we converted the product cost to a decimal by using Decimal and by pulling in the decimal library
# for the comission rate we are getting the scientific notation for 0.08 by using complex
