from graphics import circle,rectangle
from graphics.dgraphics import cuboid,sphere
r=int(input("enter the radius"))
circle.circle_area(r)
circle.circle_perimeter(r)


l=int(input("enter the length"))
b=int(input("enter the breadth"))
rectangle.rectangle_area(l,b)
rectangle.rectangle_perimeter(l,b)

l=int(input("enter the length"))
b=int(input("enter the breadth"))
h=int(input("enter the height"))
cuboid.cuboid_area(l,b,h)
cuboid.cuboid_perimeter(l,b,h)



r1=int(input("enter radius"))
sphere.sphere_area(r)
sphere.sphere_perimeter(r)