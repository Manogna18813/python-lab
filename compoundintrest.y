p=float(input("Enter principle amount: "))
r=float(input("Enter rate of interest: "))
t=float(input("Enter time in years: "))
CI=p*(1+r/100)**t-p
print("compound interest: ",CI)
