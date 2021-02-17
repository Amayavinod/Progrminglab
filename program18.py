print("area of rectangle")
f1=lambda l,b:l*b
l=int(input("enter length"))
b=int(input("enter bredth"))
print("area of rectangle=",f1(l,b))
print("area of square")
f1=lambda l,:l*l
l=int(input("enter a side"))
print("area of rectangle=",f1(l))
print("area of triangle")
f1=lambda b,h:.5*b*h
h=int(input("enter height"))
b=int(input("enter bredth"))
print("area of rectangle=",f1(b,h))