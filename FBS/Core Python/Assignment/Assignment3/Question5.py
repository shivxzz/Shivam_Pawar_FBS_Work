side_1 = int(input('Enter the first side: '))
side_2 = int(input('Enter the second side: '))
side_3 = int(input('Enter the third side: '))

if (side_1 == side_2 == side_3): 
    print('Triangle is Equilateral.')
elif (side_1 == side_2) or (side_2 == side_3) or (side_1 == side_3):
    print('Triangle is Isosceles.')
else:
    print('Triangle is Scalene')