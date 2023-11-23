lst=[]
n=int(input("Enter the limit:"))
for i in range(n):
	value=int(input("Enter the value"))
	if value>100:
		lst.append("over")
	else:
		lst.append(value)
print(lst)
