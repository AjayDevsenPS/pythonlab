


li=input("Enter a list of words seperated by spaces :").split()
lo=0
for word in li:
        if len(word)>lo:
                lo=len(word)
print("The length of the longest word is:",lo)
