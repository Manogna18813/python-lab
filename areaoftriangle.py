import math
a=float(input("Enter the side a of the triangle: "))
b=float(input("Enter the side b of the triangle: "))
c=float(input("Enter the side c of the triangle: "))
s=((a+b+c)/2)
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle is: ",area
