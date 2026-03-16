num = int(input('Enter the number: '))

if(num < 0):
    print('The number is less :')
elif(num >= 0 and num <= 100):
    print('The number is between 0 to 100.')
elif(num >= 101 and num <= 200):
    print('The number is between 101 to 200')
elif(num >= 201 and num <= 300):
    print('The number is between 201 to 300')
else:
    print('NUMBER INVALIDE')

