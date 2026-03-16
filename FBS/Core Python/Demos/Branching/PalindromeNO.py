num = int(input('Enter 3 digit number: '))
temp = num
print('This is the orignal number: ',num)

d1 = temp % 10
temp = temp //10

print(d1,temp)

d2 = temp % 10
temp = temp //10

print(d1,temp)

d3 = temp % 10
temp = temp //10

print(d1,temp)

rev_no = (d1* 100)+(d2*10)+(d3)

print('This is the reverce number: ',rev_no)

if (num == rev_no):
    print('The given number is the palindrome number')
else:
    print('The given number is not the palindrome number')