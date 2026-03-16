angle_1 = int(input('Enter the first angle: '))
angle_2 = int(input('Enter the second angle: '))
angle_3 = int(input('Enter the third angle: '))

if angle_1 + angle_2 + angle_3 == 180 and angle_1 > 0 and angle_2 > 0 and angle_3 > 0:
    print('Triangle is valid')
else:
    print('Triangle is not valid')