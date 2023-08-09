# EXERCISES: DAY 3

# Question 1
age = int(39)
print(age)

# Question 2
Height = float(202)
print(Height)

# Question 3
complex_number = 1j
print(complex_number)
print(type(complex_number))

#Question 4
base = int(input('Enter base: '))
height = int(input('Enter height: '))
area = (base*height)/2
print(area)

# Question 5
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter = side_a+side_b+side_c
print(perimeter)

# Question 6
length = int(input('Enter lenght: '))
width = int(input('Enter width: '))
area = length*width
perimeter = 2*(length+width)
print('ÁREA: ',area)
print('PERIMETER: ',perimeter)

# Question 7
import math # use this to get a more accurate quantif for pi
radius = int(input('Enter radius: '))
area_of_circle = math.pi*radius**2
print('area_of_circle: ',area_of_circle)
#ii
circum_of_circle = 2*math.pi*radius
print('circum_of_circle: ',circum_of_circle)

# Question 8 - 11
# need to bone up on year 10 maths

# Question 12
print(len('python') != len('dragon'))

# Question 13
a = 'on'
print(a in'python' and a in'dragon')

# Question 14
a = 'jargon'
print ( a in'I hope this course is not full of jargon')

# Question 15
a = 'on'
print(a not in'python' and a not in'dragon')

# Question 16
wrd = 'python'
wrd = len(wrd)
wrd = float(wrd)
wrd = str(wrd)
print(wrd)
print(type(wrd))

# question 17
num_1 = input ('Enter number to check if is even: ')
num_1 = int(num_1)
print(num_1%2 == 0)

# Question 18
num_a = 2.7
num_a = int(num_a)
num_b = int(7//3)
print('floor division of 7 by 3 is equal to the int converted value of 2.7: ', num_a == num_b)

# Question 19
print("if type of '10' is equal to type of 10: ", type('10')== type(10))

# Question 20
#a = '9.8'
#a = int(a)
print("20. Check if int('9.8') is equal to 10: ",int(float('9.8')) == int(10))

# Question 21
print('21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?')
name = input('What is your name: ')
hours = input('What is your hours: ')
rate = input('What is your rate per hour: ')
print(name,'your weekly earning is',float(hours)*float(rate))