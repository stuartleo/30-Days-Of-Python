# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(float(num_str)))    # 10 
print('num_float', float(num_str))  # 10.6
#SL - had to debug this code as str to int didn't work 
# <ValueError: invalid literal for int() with base 10: '10.6'>
#SL - converting str to int, python doesn't know if is dec or hex
#SL - one soltuion is to convert str to float before converting to int

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)