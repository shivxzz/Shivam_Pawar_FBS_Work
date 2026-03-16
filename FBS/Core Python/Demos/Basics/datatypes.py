####1.Numeric
#1. int
#int x : variable declaration- not available in python
 

x = 10                   ##: variable initialization
print(type(x))


####2. float
x = 3.14
print(type(x))


####3. complex
x = 10 + 5j              #10 is real number and 5j is imaginary
print(type(x))


####2. Text
#1. str
x = 'First "Bit" Solution'
print(type(x))

x = "First 'Bit Solution"
print(type(x))

x = '''
This is the first line
This is the second line
'''
print(type(x))

x = """
This is the first line  
This is the second line
"""


'''
This is the first line         ## multiline comments not exits in python
This is the second line        ## basicically it is a str which is not define!
'''
print(type(x))


####3. sequential
#1. list
x = [10, 20, 30, 40]
print(type(x))

#2. tuple
x = (10, 20, 30, 40)
print(type(x))

#3. range
x = range(1,10)
print(type(x))


####4. Set type
#1. Set
x = {10, 20, 30, 40}
print(type(x))

#2. Frozenset
x = frozenset({10, 20, 30, 40})


####5. Mapping
#1.dict
x = {1:'Python', 2:'Java', 3:'Testing'}
print(type(x))


####6. bool (Boolean)
x = True
print(type(x))


####7. Nontype
x = None
print(type(x))
