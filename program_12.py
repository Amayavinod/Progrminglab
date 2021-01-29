d = {}
n = int(input("Enter the number of items in the dictionary:"))
for i in range(n):
    d[i] = input("Enter value")
asc = sorted(d.values())
print("In ascending order:", asc)
asc.reverse()
print("In descending order:", asc)