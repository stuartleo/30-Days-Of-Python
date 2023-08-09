# EXCERCISE: LEVEL 1

# Question 1
#Day 2: 30 Days of python programming

# Question 2 - 13
first_name = 'Stuart'
last_name = 'Leo'
full_name = first_name,last_name
country = 'Australia'
city = 'Melbourne'
age = 39
year = 2023
is_married = False
is_true = True
is_light_on = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']

# EXCERCISE: LEVEL 2

# Question 1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(skills))

# Question 2 - 3
print(len(first_name))
print(len(first_name)-len(last_name)) #might be useful to specify int or float

# Question 4
num_one = 5
num_two = 4
total = num_one+num_two
print(total)
diff = num_one-num_two
print(diff)
product = num_one*num_two
print(product)
division = num_one/num_two
print(division)
remainder = num_one%num_two
print(remainder)
exp = num_one**num_two
print(exp)
floor_division = num_one//num_two
print(floor_division)

# Question 5
import math
radius = 30
#i
area_of_circle = math.pi*radius**2
print(area_of_circle)
#ii
circum_of_circle = 2*math.pi*radius
print(circum_of_circle)
#iii
# see i

# Question 6
first_name = input('What is your first name: ')
last_name = input('What is your last name: ')
country = input('What country are you from: ')
age = input('How old are you? ')

print(first_name)
print(last_name)
print(country)
print(age)

print(help('keywords'))