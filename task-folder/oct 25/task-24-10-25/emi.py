# EMI Calculation 
p = int(input("enter the principal amount ")) #principal_amount

r = float(input("enter the interest rate ")) #interest_rate

n = int(input("enter the number of months ")) #total_months

emi = (p*r*(1+r)**n)/((1+r)**n-1)

print("emi is ",round(emi,2))