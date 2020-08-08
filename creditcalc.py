import math
from math import ceil
from typing import Union

print("Enter the credit principal:")
credit_principal = int(input())
print("What do you want to calculate?")
print("type 'm' - for count of months,")
print("type 'p' - for monthly payment:")
count = input()
if count == 'm':
    print("Enter monthly payment:")
    payment = int(input())
    result = credit_principal / payment
    result = math.ceil(result)
    print(result)
else:
    print("Enter count of months:")
    months = int(input())
    payment1 = credit_principal / months
    payment1 = math.ceil(payment1)
    lastPayment = credit_principal - (months - 1) * payment1
    if lastPayment != 0:
        print("Your monthly payment = ", payment1, " with last monthly payment = ", lastPayment,".")
    else: print("Your monthly payment = ", payment1)
