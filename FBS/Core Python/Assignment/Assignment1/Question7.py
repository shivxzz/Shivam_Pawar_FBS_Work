a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

d = (b ** 2-(4 * a * c))** 0.5

r1 = (- b + d) / 2 * a
r2 = (- b - d) / 2 * a

print(f'Root 1 = {r1}')
print(f'Root 2 = {r2}')