numbers=[-3,5,-8,10,-2,15]
positive_numbers=[num for num in numbers if num>0]
print("The list is",numbers)
print("The positive numbers in the list are",positive_numbers)
n=5
squares=[x**2 for x in numbers]
print("The squares of the numbers in list are",squares)
word="hello"
vowels=[char for char in word if char in 'aeiouAEIOU']
print("The character is ",word)
print("The vowels in the character are",vowels)
ordinal_values=[ord(char) for char in word]
print("The ordinal values are",ordinal_values)
