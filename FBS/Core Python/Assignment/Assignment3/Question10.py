gender = (input('Enter gender (M/F): '))
age = int(input('Enter age: '))

if(gender in ['F', 'f', 'female', 'Female', 'FEMALE'] ):
    if(age >= 18):
        print('Eligible for marriage. ')
    else:
        print('Not ligible for marriae. ')
else:
    if(age >= 21):
        print('Eligible for marriage. ')
    else:
        print('Not ligible for marriae. ')