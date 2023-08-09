# EXERCISE: LEVEL 2

# Question 1 
# how do I print python version within python script?
import sys #import module
print(sys.version)

# Question 2
print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

# Question 3
print('stuart')
print('leo')
print('Australia')
print('I am enjoying 30 days of python')

# Question 4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['stuart','python','Australia']))
print(type('Stuart'))
print(type('Leo'))
print(type('Australia'))

# EXERCISE: LEVEL 3

# Question 1
#print(1)
print(type(1)) # Number (int)
#print('stuart')
print(type('stuart')) # String (str)
print(type(True))
print(type(['stuart','python','Australia'])) # List []
print(type(('stuart','python','Australia'))) # Tuple ()
print(type({'stuart','python','Australia'})) # Set {}
print(type({'name':'stuart','lang':'python','çountry':'Australia'})) # Dictionary {x:y}

# Question 2
print((((10-2)**2)+((8-3)**2))**.5)
print(float((((10-2)**2)+((8-3)**2))**.5)) # same as above, but specifies floating output
print(int((((10-2)**2)+((8-3)**2))**.5)) # specifies integer output