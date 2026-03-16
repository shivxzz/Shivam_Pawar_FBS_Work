cost_price = int(input('Enter cost price of the book: '))
discount_percentage = int(input('Enter the discount percentage: '))

discount = (cost_price * discount_percentage) / 100
selling_price = cost_price - discount

print('Selling price of the book:',selling_price)
