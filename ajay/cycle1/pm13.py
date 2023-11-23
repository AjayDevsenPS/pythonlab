l1=[]
l2=[]
l3=[]
n1=int(input("Enter the length of list1:"))
for i in range(0,n1):
        x=int(input("Enter the element"))
        l1.append(x)
n2=int(input("Enter the length of list2:"))
for i in range(0,n2):
        y=int(input("Enter the element"))
        l2.append(y)
if len(l1)==len(l2):
 print("list1 and list2 have same length")
else:
 print("list1 and list2 have same length")
if sum(l1)==sum(l2):
 print("sum of list1 and list2 are same ")
else:
 print("sum of list1 and list2 are different")
for i in range(0,n1):
 for j in range(0,n2):
  if l1[i]==l2[j]:
   a=l1[i]
   l3.append(a)
if l3!=[]:
  print("Commom element are ",l3);
else:
 print("No common elements")
