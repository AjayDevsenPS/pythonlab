def simpleinterest( yn,p,n):
	if yn=="y":
		r=.12
	else:
		r=.10
	s=p*n*r
	print("The simple interest is:",s)
yn=input('Is the person a senior or not,if yes enter "y",else enter "n":')
p=int(input("Enter the principle amount "))
n=int(input("Enter the  no of years "))
simpleinterest(yn,p,n)


