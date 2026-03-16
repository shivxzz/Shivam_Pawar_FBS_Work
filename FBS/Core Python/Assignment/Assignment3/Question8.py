import random

correct_userid = "admin"
correct_password = "1234"

userid = input('Enter User ID: ')
password = (input('Enter Password: '))

if (userid == correct_userid and password == correct_password):
    print('Login Successful')

    otp = random.randint(1000, 9999)
    print('OTP:',otp)

    user_otp = int(input('Enter the OTP: '))

    if (user_otp == otp):
        print('verification Successful')
    else:
        print('Verification Failed')

else:
    print('Invalid User ID or Password')