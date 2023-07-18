#Data Mining Assignment
#Question 1


String=input("Enter a String ")
l=len(String)
rev=''.join(reversed(String))

#check for palindrome
if String==rev:
    print("The entered string is palindrome")
else:
    print("The entered string is not palindrome")

#check for Symmetric
if l%2 == 0:              #if no. of letters is even
    mid= l//2
    first=String[:mid]
    last=String[mid:]
else:                     # if no. of letters is odd
    mid=(l-1)//2
    print(mid)
    first=String[:mid]
    last=String[mid+1:]
if first==last:
    print("The entered string is symmetrical")
else:
    print("The entered string is asymmetrical")
