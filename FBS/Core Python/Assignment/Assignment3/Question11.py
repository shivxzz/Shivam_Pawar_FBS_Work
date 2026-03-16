person1 = int(input('Enter age of person 1: '))
ticket1 = int(input('Enter ticket amount: '))

if person1 < 12:
    final_ticket1 = ticket1 - (ticket1 * 0.30)
elif person1 > 59:
    final_ticket1 = ticket1 - (ticket1 * 0.50)    
else:
    final_ticket1 = ticket1


person2 = int(input('Enter age of person 2: '))
ticket2 = int(input('Enter ticket ammount: '))

if person2 < 12:
    final_ticket2 = ticket2 - (ticket2 * 0.30)
elif person1 > 59:
    final_ticket2 = ticket2 - (ticket2 * 0.50)    
else:
    final_ticket2 = ticket2


person3 = int(input('Enter age of person 3: '))
ticket3 = int(input('Enter ticket ammount: '))

if person3 < 12:
    final_ticket3 = ticket3 - (ticket3 * 0.30)
elif person1 > 59:
    final_ticket3 = ticket3 - (ticket3 * 0.50)    
else:
    final_ticket3 = ticket3


person4 = int(input('Enter age of person 4: '))
ticket4 = int(input('Enter ticket ammount: '))

if person4 < 12:
    final_ticket4 = ticket4 - (ticket4 * 0.30)
elif person1 > 59:
    final_ticket4 = ticket4 - (ticket4 * 0.50)    
else:
    final_ticket4 = ticket4


person5 = int(input('Enter age of person 5: '))
ticket5 = int(input('Enter ticket ammount: '))

if person5 < 12:
    final_ticket5 = ticket5 - (ticket5 * 0.30)
elif person5 > 59:
    final_ticket5 = ticket5 - (ticket5 * 0.50)    
else:
    final_ticket5 = ticket5


total_ticket = final_ticket1 + final_ticket2 + final_ticket3 + final_ticket4 + final_ticket5
print('Total ticket amount =',total_ticket)