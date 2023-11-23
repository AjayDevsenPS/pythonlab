li=input("Enter the values:").split(',')
oli=[]
for i in li:
	if int(i)%2!=0:
		oli.append(int(i))
print("original list:",li)
print("New list without even numbers:",oli)




