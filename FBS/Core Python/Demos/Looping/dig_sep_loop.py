num = int(input('Enter Number: '))
temp = num

while(temp > 0):
    d = temp % 10
    print(d)
    temp = temp // 10