#Take the input of the subjects

Python = int(input('Enter python marks: '))
Java = int(input('Enter Java marks: '))
C = int(input('Enter C marks: '))
html = int(input('Enter HTML marks: '))
css = int(input('Enter CSS marks: '))

#Calculate the add of the subjects

gain_marks = Python + Java + C + html + css

#Calculate the percentage of the subjects

percentage = (gain_marks / 500) * 100

# Display output

print("This is the percentage of your subjects:",percentage)