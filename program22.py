class rectangle:
	__area=0
	def __init__(self,length,width):
		self.__length=length
		self.__width=width
	def calc_area(self):
		self.__area=self.__length*self.__width
		print("area=",self.__area)
	def __lt__(self,second):
		if self.__area<second.__area:
			return True
		else:
			return False
l1=int(input("enter the length of 1st rectangle"))
w1=int(input("enter the width of 1st rectangle"))
l2=int(input("enter the length of 2nd rectangle"))
w2=int(input("enter the widthof 2nd rectangle"))
ob1=rectangle(l1,w1)
ob2=rectangle(l2,w2)
ob1.calc_area()
ob2.calc_area()

if ob1<ob2:
	print ("2nd one is large")
else:
	print("1st one is large")