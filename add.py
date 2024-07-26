import math
#print(1+1)
x=int(input("Enter 1st number"))
y=int(input("Enter 2nd number"))
sum=x+y
print("sum=",sum)
#Area of Triangle
a=float(input("Enter 1st side of triangle"))
b=float(input("Enter 2nd side of triangle"))
c=float(input("Enter 2rd side of triangle"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)**0.5)
print("Area",area)
#Sqaure root
x=int(input("Enter a number"))
root=x**0.5
