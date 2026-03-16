x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
print(f'Befour Swapping x = {x}, y = {y}')

y = x + y
x = y - x
y = y - x
print(f'After Swapping x = {x}, y = {y}') 