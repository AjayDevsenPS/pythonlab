str=input("Enter a string:")
lst=list(str)
first=lst[0]
for i in range(1,len(lst)):
        if lst[i]==first:
                lst[i]="$"
str=""
str=str.join(lst)
print(str)


