hours = int(input('Enter Hours: '))
minutes = int(input('Enter Minutes: '))
seconds = int(input('Enter Seconds: '))

total_seconds = seconds + (minutes * 60) + (hours * 3600)

print('Total Seconds =', total_seconds)
