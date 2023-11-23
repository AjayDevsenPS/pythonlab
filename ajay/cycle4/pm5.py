def vsum(*args):
	"""variable length argument sum"""
	sum=0
	for num in args:
		sum+=num
	print(sum)
a=()
a=input("Enter the numbers you want to add ")
vsum(a)
