numbers=[]
limit=int(input("Enter number of elements:"))
for i in range(0,limit):
	ele=int(input())
	numbers.append(ele)
positive_numbers=[num for num in numbers if num>0]
print("The list is",numbers)
print("The positive numbers in the list are",positive_numbers)
squares=[x**2 for x in numbers]
print("The squares of the numbers in list are",squares)
word=input("Enter the word ")
vowels=[char for char in word if char in 'aeiouAEIOU']
print("The character is ",word)
print("The vowels in the character are",vowels)
print("The ordinal values of each characters are:")
for char in word:
	print(ord(char))
