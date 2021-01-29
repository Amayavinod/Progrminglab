no=input("enter list of Numbers")
list1=[]
list1=[int (i) for i in no.split()]
print("Actual List=",list1)
pos_no=[i for i in list1 if i>=0]
print("posative numbers=",pos_no)