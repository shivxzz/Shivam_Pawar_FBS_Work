user_id = input('Enter User ID: ')
password = int(input('Enter Password: '))

if (user_id == 'admin' and password == 1234):
    print('Login Successful')
else:
    print('Invalid User ID or Password')
