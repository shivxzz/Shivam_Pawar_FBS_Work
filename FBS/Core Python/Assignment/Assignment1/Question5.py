principel = int(input('Enter the principel: '))
rate = int(input('Enter thr rate: '))
time = int(input('Enter the time: '))

amount = principel *(1 + rate / 100) ** time
compound_interest = amount - principel

print(f"Compound Interest: {compound_interest}")
