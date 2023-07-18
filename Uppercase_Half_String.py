#Data Mining Assignment
#Question 4

test_str = 'helloworldfriend' 

# To get user defined inputs use : input("Enter a String")

mid = len(test_str) // 2
output = ''
for i in  range (len(test_str)):
    if i >= mid:
        output = output + test_str[i].upper()
    else:
        output = output + test_str[i]

print(output)

