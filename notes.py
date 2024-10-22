#Run Test Here


#Space Here
''' Hello World In Python
print('Hello World')
print("Hello World")
print("Hello\nWorld")
'''

''' difference between ' and "
# ' is used for single quotes
# " is used for double quotes

print('Hello, World!')  # prints Hello, World!
print("Hello, World!")  # prints Hello, World!

print('Hello, "World"!')  # prints Hello, "World"!
print('Hello, \'World\'!')  # prints Hello, 'World'!
'''

''' variables and data types
name = 'dayn' # character
age = 25 # integer
weight = 43.5 # float
valid = True # boolean

print(name) # prints dayn
print(age) # prints 25
print(weight) # prints 43.5
print(valid) # prints True
'''

''' basic operators #1 (Arithmetic Operation)
a = 10
b = 3
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus (remainder)
print(a ** b)  # Exponentiation
'''

''' basic operators #2 (Comparison Operation)
a = 15
b = 5
print(a == b)  # Equals         prints False
print(a != b)  # Not equals     prints True
print(a > b)  # Greater than    prints True
print(a < b)  # Less than       prints False
'''

''' basic operators #3 (Logical Operation)
a = 20
b = 10
print(a > b and b > 0)  # Logical AND (&&)  prints True
print(a > b or b < 0)   # Logical OR (||)   prints True
print(not (a > b))      # Logical NOT (!)   prints False
'''

''' control structures #1 (if statements)
num = 10

print(num)

if num > 5:
    print('num is Greater than 5')

if num < 5:
    print('num is Less than 5')
'''

''' control structures #2 (if else statements)
num = 10

print(num)

if num > 5:
    print('num is Greater than 5')
elif num < 5:
    print('num is Less than 5')
'''

''' control srtuctures #3 (for loop) #1 Start|Stop|Step
for num in range(5): # num will be 0
    print(num)          # prints 0 1 2 3 4 5
    
# (5) is condition 
'''

''' control srtuctures #4 (for loop) #2 Declaration Outside of the For Loop
num = 1

for num in range(5): # num will be still 0
    print(num)          # prints 0 1 2 3 4 5
'''

''' control srtuctures #5 (for loop) #3 Start & Condition/End
for num in range(5, 10): # num will start 5
    print(num)          # prints 5 6 7 8 9 10
    
# (5, 10)
# 5 - start
# 10 - end/condition = if 5 reach at 10 it will stop the loop
'''

''' control srtuctures #6 (for loop) #4 Start, End/Condition & Increment
for num in range(5, 10, 2): # num will start at 5
    print(num)              #prints 5 7 9

# (5, 10, 2)
# 5 - start
# 10 - end/condition >> if 5 reach at 10 it will stop the loop
# 2 - it will increment the 5 >> 5 + 2 = 7
'''

''' control srtuctures #7 (while loop)
count = 0

while count < 5: # if count reach 5 it will stop
    print(count)
    count += 1 # increment the variable "count" by 1
'''

''' (def) function #1 Basic Structure
# Basic Structure
# def function_name(parameters):
#    """Docstring: A brief description of the function."""
#    # Function body: Code to execute
#    return value  # Optional: return a value

# function_name = like a variable you will name the functions for your execution
# parameters = like a variable you will pass the values to the function for execution
# fucntion body: = your code/ program you will function
# return value = you will return the value from the function for execution
'''

''' (def) function #2 Addition Integers
def add(a, b)
    return a + b # return a + b = value >> add(8)
    
print(add(3, 5))    # prints 8
'''

''' (def) function #3 Multiply Intergers
def multiply(a, b, c):
    """Return the product of three numbers."""
    return a * b * c

print(multiply(2, 3, 4))  # Output: 24
'''

''' list structure #1 Basic Structure
my_list = [item1, item2, item3, ...]

# my_list >> any name
# item1, item2, item3, ... >> any values you will assign to the list
'''

''' list structure #2 Display all in the list
fruits = ["apple", "banana", "cherry"]

print(fruits)   # Output: ["apple", "banana", "cherry"]
'''

''' list structure #3 Modifying List: Append
# Append: Add an item to the end of the list
# variable.append("name_you_will_add")

fruits = ["apple", "banana", "cherry"]

print(fruits)   # Output: ["apple", "banana", "cherry"]

fruits.append("orange")
print(fruits)   # Output: ['apple', 'banana', 'cherry', 'orange']

fruits.append([1, 2, 3]) # add item value as whole group
print(fruits)   # Output: ['apple', 'banana', 'cherry', 'orange', [1, 2, 3]]
'''

''' list structure #4 Modifying List: Insert
# Insert:  Add an item at a specific position
# variable.insert(NumberOfPostion, "name_you_will_add")

fruits = ["apple", "banana", "cherry"] # apple > 0, banna > 1, cherry > 2

print(fruits)   # Output: ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")
print(fruits)   # Output: ['apple', 'orange', 'banana', 'cherry']
'''

''' list structure #5 Modifying List: Remove
# Remove: Remove an item by value or index
# variable.remove("name_of_the_item")
# del variable[number_of_item_you_want_to_delete]

fruits = ["apple", "banana", "cherry"]

print(fruits)   # Output: ['apple', 'banana', 'cherry']

fruits.remove("banana")     # delete the banana
print(fruits)   # Output: ['apple', 'cherry']

del fruits[0]               # delete the apple
print(fruits)   # Output: ['cherry']
'''

''' list structure #6 Modifying List: Pop
# Pop: Remove and return the last item
# variable.pop(index_of_item_you_want_to_delete)
# variable.pop()   # delete the last item
# variable.pop(-1) # delete the last item
# variable.pop(0)  # delete the first item
# variable.pop(-2) # delete the second item from the end
# variable.pop(-3) # delete the third item from the end

fruits = ["apple", "banana", "cherry"]

print(fruits)   # Output: ['apple', 'banana', 'cherry']

fruits.pop()        # Delete the last item
print(fruits)

fruits.pop(0)       # Delete the first item
print(fruits)   # Output: ['banana']
'''

''' list structure #7 Modifying list: Clear
# Clear: Remove all items from the list
# variable.clear()

fruits = ["apple", "banana", "cherry"]

fruits.clear()
print(fruits)
'''

''' list structure #7 Modifying list: Extend
# Extend: adds multiple item and unpack all value unlike append adds whole value as one
# Extend: add item at the last

fruits = ["apple", "banana", "cherry"]

print(fruits)                       # Output: ['apple', 'banana', 'cherry']
fruits.extend(["grapes"])   # Add grapes item at the last
print(fruits)                       # Output: ['apple', 'banana', 'cherry', 'grapes']
fruits.extend([8, 'mango']) # Unpack the value and add as single item instead of [..., [8, mango]]
print(fruits)                       # Output: ['apple', 'banana', 'cherry', 'grapes', 8, 'mango']
'''

''' list structure #7 List Methods: Length
# Length: Get the number of items in the list.
# variable1 = len(variable) 

fruits = ["apple", "banana", "cherry"]

length = len(fruits)
print(fruits)
print(length)   # Outputs: 3
'''

''' list structure #8 List Methods: Slicing
# Slicing: Access a sub-list using slicing
# variable1 = variable[numberindex:numberindex]
# variable1 = variable[start_index:stop_index:step]

fruits = ["apple", "kiwi", "cherry", "orange"] # 0, 1, 2, 3

first_two_fruits = fruits[0:2]  # Get the first two items>> 0 1
print(first_two_fruits)     # Output: ['apple', 'kiwi']

k_and_o = fruits[1:4:2]         # 1 > kiwi. 1 + 2 = 3. 3 > cherry
print(k_and_o)              # Output: ['kiwi', 'Orange']
'''

''' list structure #9 List Methods: Sorting #1 .sort
# list.sort() : Sort the list in ascending order permanent

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(numbers)      # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5]

numbers.sort()      # variable.sort() sort the item in ascending order
print(numbers)      # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]

#items will not be return as before
''' 

''' list structure #10 List Methods: Sorting #2 sorted
# items = sorted(list)      # Sort the list in ascending order but doesnt affect the original

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(numbers)              # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5]

fixnum = sorted(numbers)
print(fixnum)               # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]
print(numbers)              # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5]
'''

''' list structure #11 List Methods: Sorting #3 Reverse Ascending
# can be apply on sorted and sort

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(numbers)              # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5]

fixnum  = sorted(numbers, reverse=True) # reverse=True
print(fixnum)               # Output: [9, 6, 5, 5, 4, 3, 2, 1, 1]
print(numbers)              # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5]

numbers.sort(reverse=True)

print(numbers)              # Output: [9, 6, 5, 5, 4, 3, 2, 1, 1]

# can ascending words and letters and can be reverse
'''

''' list structure #12 Mix Data Types
# list can store any data types
mixed_list = ["apple", 42, 3.14, True, ["banana", "pear"], (1, 2)]

print(mixed_list[0])  # Output: apple
print(mixed_list[1])  # Output: 42
print(mixed_list[4])  # Output: ['banana', 'pear']
'''

''' data structures #1 Tuples: Accessing & Update
# Tuples is cannot modify unlike list can be modify
# Tuples defined using () unlike list use square brackets []
# Tuples can also store mix different data types

# Accessing tuple element specific
my_tuple = (1, 2, 3, "apple", "banana")
print(my_tuple)     # Output: (1, 2, 3, 'apple', 'banana')
print(my_tuple[3])  # Output: apple

# Update tuple 
my_tuple = 1, 2, 3  # Update tuple items
print(my_tuple)     # Output: (1, 2, 3)

# Accessing tuple element specific
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3
'''

''' data structures #2 Tuples Operations: Concatenation
# combining tuples
# can combine two or more tuples

t1 = (1, 2, 3)  # tuple 1
t2 = (4, 5, 6)  # tuple 2
comb = t1 + t2  # combining tuple 1 and 2

print(t1)   # Output: (1, 2, 3)
print(t2)   # Output: (4, 5, 6)
print(comb) # Output: (1, 2, 3, 4, 5, 6)
'''

''' data structures #3 

'''

''' data structures #

'''

''' data structures #

'''

''' data structures #

'''

''' data structures #

'''

''' data structures #

'''

''' data structures #

'''

''' data structures #

'''

''' data structures #

'''






''' (def) function #4
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())         # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!
'''











