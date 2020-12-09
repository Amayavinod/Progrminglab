y=int(input("enter the year : "))
if y%400 == 0 or (y%4 == 0and y%100 != 0):
	print(y,"is a leap year")
else:
	print(y,"is not a leap year") 