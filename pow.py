b=int(input("Enter the base: "))
e= int(input("Enter the exponent: "))
result=1
for i in range(e):
    result*=b
print("power of the number is: ",result)
