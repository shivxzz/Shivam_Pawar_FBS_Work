python = int(input('Enter your python marks: '))
java = int(input('Enter your JAVA marks: '))
c = int(input('Enter your C marks: '))
html = int(input('Enter HTML marks: '))
css = int(input('Enter CSS marks: '))

gain_marks = python + java + c + html + css

percentage = (gain_marks / 500) * 100

print("This is the percentage of your subjects:",percentage)