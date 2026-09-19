# # this is comment python
# # this is another comment

# name = "abdalla"  # this name variable comment
# age = 24
# user_name = "huseen"

# score = 10
# print(score)
# score += 5
# print(score)
# 5+6
# 5/5
# total = 10-5
# power = 10 ** 2
# 5+5
# squared = 5 ** 2
# name = "abdullahi"

# first_name = "abdullahi"
# last_name = "ibraahim"
# full_name = first_name + " "+last_name
# long_dash = "-" * 12
# len(full_name)
# message = "hello"
# print(len(message))

# is_login_in = True
# is_student = False
# age=12
# can_vote = age>=True

# operator example and logic
import math
import os
from math import pi
import random
import datetime
age = 25
has_license = True

car_drive = age >= 16 and has_license
print(f"somthing: {car_drive}")

# this is or  example
day = "saturday"
is_weekend = day == "saturday" or day == "sunday"
print(is_weekend)

# string manipulation

first_name = "abdullahi"
last_name = "huseen"
full_name = first_name + " " + last_name

name = "Abdalla"
print(f"hi there my name is {name}")

# print(f"hello, {name}")

age = 12
intro = f"i'm {first_name} and i'm {age} years old"

# repetition
star = "-"
star = star*20

# string method
text = "python is programing"
print(text.upper())
print(text.upper())

# clearning string
messy = "  hello world  "
print(messy)
price = "$19.99"
print(price.strip("$"))

# Finding and replacing

message = "I love Python programming with Python"
print("Python" in message)
print(message.startswith("I"))

# control flow  if statement
temperature = 25
if temperature > 30:
    print("its hot")
else:
    print("its nice weather!")

# if-elif-else chains
score = 85

if score >= 90:
    print("A-excelent")
elif score >= 60:
    print("B-Good job")
elif score >= 80:
    print("c-keep up !")
else:
    print("f-improvement")

# nasted if statement
has_ticket = False
age = 18

if has_ticket:
    if age >= 12:
        print("Enjoy the movie")
else:
    print("buy the ticket")

# loops = repeat code without writing multiple times

for i in range(0, 10, 2):
    print(i)
#  while loop

count = 0

while count < 5:
    print(f"count is {count}")
    count += 1

#  list array

my_list = ["apple", "banana", "orange"]

# print(f"list is : {my_list[0]}")
# my_list[0]='lemon'
# print(my_list)
my_list.append("mango")
print(my_list)
my_list.remove("orange")
print(my_list)


# List methods

number = [1, 2, 3, 4, 5, 6, 7, 7]
print(f"numer is {number}")
print(len(number))
print(number.count(2))
number.sort()
print(number)
number.reverse()
print(number)

# dictionary method
person = {
    "name": "abdullahi",
    "age": 25,
    "city": "somali"
}
person["name"] = "hise"
person["age"] = 26
print(person.values())
print(person.keys())
print(person.items())
if "name" in person:
    print("name found")

person.update({"name": "abdalla", "age": 24, "city": "uk"})
print(person)
print(person.get("name"))
print(person["age"])
person["email"] = "abdalla@example.com"
print(person)
person["city"] = "london"
print(person)

# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")
colors[1]
# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = (42)  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20

point = (3, 5)
print(point[0])

x, y = point
print(f"x: {x}, y:{y}")
# swap variable values
x, y = y, x
print(f"x: {x}, y:{y}")

# set
empty_set = set()

fruits = {"apple", "banana", "orange"}
print(fruits)
fruits.add("mango")
print(fruits)
# from list to set remove duplicates
numbers = [1, 2, 3, 2, 1, 4]
unique_numbers = set(numbers)


# functions with python

def greet():
    print("Hello, world!")
    print("Welcome to Python!")


# Call the function
greet()


# fucntion with logic

def check_weather():
    temperature = 25
    if temperature > 30:
        print("its hot")
    else:
        print("its nice weather!")


# use fuction
check_weather()


def say_goodbye():
    print("Goodbye!")
    print("See you later!")


# Call it multiple times
say_goodbye()
say_goodbye()
say_goodbye()

# fucntion with parameter


def greet_abdalla(name, age, city):
    print(f"Hello, {name}!")
    print(f"i am {age} years old.")
    print(f"i'm in {city}.")


# Call the function with different arguments
greet_abdalla("Abdalla", 24, "London")


def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    total = price + tax - discount
    print(f"Total price: {total}")


calculate_total(100, 0.08, 10)  # Example usage

today = datetime.date.today()
print(today)

number = random.randint(1, 10)
print(f"Random number: {number}")

current_dir = os.getcwd()

# petern :1 import whole mudule

math.sqrt(16)
# pettern :2 import specific item  from module
print(f"Value of pi: {pi}")

import random
numers = random.randint(10, 12)
choice = random.choice(["apple", "banana", "orange"])





# first api call example
import requests
def  get_weather(latitude,longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
    data = response.json()
    return data["current"]["temperature"]

paris_temp=get_weather(48.8566, 2.3522)
london_temp=get_weather(51.5074, -0.1278)
tokyo_temp=get_weather(35.6895, 139.6917)

print(f"Current temperature in Paris: {paris_temp}°C")
print(f"Current temperature in London: {london_temp}°C")  
print(f"Current temperature in Tokyo: {tokyo_temp}°C")  
