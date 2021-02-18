class rect:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def area(self):
        ar=self.length*self.width
        print("AREA OF RECTANGLE =",ar)
        return ar
    def perimeter(self):
        peri=2*(self.length+self.width)
        print("PERIMETER OF RECTANGLE =",peri)
def choice():
       print("MENU\n1.AREA\n2.PERIMETER\n3.COMPARE AREA\n4.EXIT")
       ch=int(input("Enter your choice :"))
       if ch==1:
           l=int(input("Enter length ="))
           w=int(input("Enter width ="))
           r=rect(l,w)
           r.area()
           choice()
       elif ch==2:
           l=int(input("Enter length ="))
           w=int(input("Enter width ="))
           r=rect(l,w)
           r.perimeter()
           choice()
       elif ch==3:
 
        l1=int(input("Enter Length 1:"))

        b1=int(input("Enter Breadth 1:"))

        s=rect(l1,b1)

        l2=int(input("Enter Length 2:"))

        b2=int(input("Enter Breadth 2:"))

        t=rect(l2,b2)

        if s.area()>t.area():

            print("Area 1 is Greater")

        else:

            print("Area 2 is Greater")

        choice()
  
        
       elif ch==4:
           print("Exiting..!")
           return 0
       else:
           print("Invalid Choice")
           choice()
choice()