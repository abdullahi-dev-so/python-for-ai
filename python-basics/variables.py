# Python Variables

## 1. What is a Variable?
#  A variable is a named location in memory that stores data. In Python, you can create a variable by simply assigning a value to a name using the `=` operator.

## 2. Variable Naming Rules
#  - Variable names must start with a letter or an underscore (_).
#  - The rest of the name can contain letters, numbers, and underscores.
#  - Variable names are case-sensitive (e.g., `myVar` and `myvar` are different variables).

## 3. Assigning Values to Variables
#  You can assign values to variables using the `=` operator. For example:
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_student = True  # Boolean

## 4. Multiple Assignments
#  You can assign values to multiple variables in a single line:
a, b, c = 1, 2, 3
# python has rules for variable names

user_name = "Dave"      # lowercase with underscores (Python style)
userName = "Dave"       # camelCase (works but not Python style)
age2 = 30              # numbers are OK (not at start)
_private = "secret"    # underscore at start is OK

# not allowed
# 2age = 30              # Can't start with number
# my-name = "Dave"       # No hyphens (Python thinks it's subtraction)
# my name = "Dave"       # No spaces
# class = "Python"       # Can't use Python keywords

# python name conventions:
# Good Python style
first_name = "Alice"
user_age = 25
is_logged_in = True
shopping_cart_total = 49.99

# Avoid camelCase (this is for other languages)
firstName = "Alice"  # Works, but not Python style
userAge = 25
isLoggedIn = True

# variable can change 

# Start with one value
score = 0
print(score)  # Shows: 0

# Change it
score = 10
print(score)  # Shows: 10

# Change it again
score = score + 5
print(score)  # Shows: 15

# comman mistakes
#  forget quotes for around text
# using undefined variable names
