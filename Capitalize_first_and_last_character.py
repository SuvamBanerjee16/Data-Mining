#Data Mining Assignment
#Question 5

string = input("Enter the string ")
string = string.title()

list = string.split()
output =''

for i in list:
    output += i[:-1]+i[-1].upper()+" "

print(output)
