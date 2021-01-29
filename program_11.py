txt=input("enter the line of text").split(" ")
lst=[]
for i in txt:
	if i not in lst:
		lst.append(i)
for i in lst:
	print("no of occurence",i,"=",txt.count(i))