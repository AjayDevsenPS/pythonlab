def trueorfalse(s1,s2,n):
	if(s1[0:n]==s2[0:n]):
		print("True")
	else:
		print("False")
s1=input(("Enter the first string "))
s2=input(("Enter the first string "))
n=int(input("Enter the length to which you want to compare the two strings "))
trueorfalse(s1,s2,n)
