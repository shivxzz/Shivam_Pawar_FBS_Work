
####### Separating the given number #######
 
num = 427
print("Number:",num)


d1 = num % 10
num = num //10

d2 = num % 10
num = num //10

d3 = num % 10
num = num //10


print(f'd1:{d1}, d2:{d2}, d3:{d3}')




'''

####### Add the digits of the given number #######

num = 427
print("Given Number:",num)


d1 = num % 10
num = num //10

d2 = num % 10
num = num //10

d3 = num % 10
num = num //10

sum = d1 + d2 + d3

print("This is addition of numbers digits:",sum)

'''

'''

####### Reverse the given number ####### 

num = 427
print("Given Number:",num)


d1 = num % 10
num = num //10

d2 = num % 10
num = num //10

d3 = num % 10
num = num //10

sum = (d1* 100)+(d2*10)+(d3)
print("Reverse given number:",sum)

'''