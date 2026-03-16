side_1 = int(input('Enter the first side: '))
side_2 = int(input('Enter the second side: '))
side_3 = int(input('Enter the third side: '))

if (side_1 + side_2 > side_3) and (side_1 + side_3 > side_2) and (side_2 + side_3 > side_1):
    print('Triangle is valid')
else:
    print('Triangle is not valid')