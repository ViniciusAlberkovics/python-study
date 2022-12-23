from math import *
from random import randint
import datetime
import json
import re
import requests

# Import My Custom Module
import character_class_module
import defaults_character_class
from my_module import print_hello  # import specific part

# https://www.w3schools.com/python/python_classes.asp

# Learn Simple Variables
character_name = "John"
character_birth_dt = "1998-11-16"
character_weigth = 56.7
character_is_male = True
print("My name is: " + character_name)
print("My birth date is: " + character_birth_dt)
print("My weigth is: " + str(character_weigth))
print("Is male? A:" + str(character_is_male))


# Learn String Manipulation
phrase = "my phrase"
print(len(phrase))  # phrase size


# Learn Number Manipulation
positive = 12
negative = -2
decimal_number = 2.3
print(str((positive - negative) * decimal_number))
print("Mod:" + str(11 % 2))
print("Absolute value:" + str(abs(negative)))
print(str(max(1, 3, 7)) + " is max value")
print(str(min(1, 3, 7)) + " is min value")


print("round:" + str(round(3.7)))
print("floor:" + str(floor(3.2)))
print("ceil:" + str(ceil(3.2)))
print("sqrt:" + str(sqrt(4)))


# Learn Get User Input
inputed_name = input("Enter your name: ")
print("User Name is: " + inputed_name)


# Learn Lists
colors = ["red", "blue", "purple", "green"]
print(colors)
print("Filtred list: " + str(colors[1:2]))

colors.append("white")
print("Append:" + str(colors))

colors.insert(1, "black")
print("Insert:" + str(colors))

colors.remove("black")
print("remove:" + str(colors))

print("Check if BLUE exists in colors: " + str(colors.index("blue")))

colors.append("red")
print("count RED:" + str(colors.count("red")))


# Learn Tuples
coordinates = (1, 7)  # immutable
print("Tuple:" + str(coordinates[0]))


# Learn Functions


def say_hello(name: str):
    print("Hello!")
    return "Hello " + name + "!"


def say_hello_without_explict_type(name):
    return "Hello " + name + "!"


print(say_hello("John Doe"))
print(say_hello_without_explict_type("Cloe Doe"))


# Learn Return Statements


def cube(num):
    return num*num*num


print(cube(3))


# Learn If Statements
int_value = randint(0, 1000)
print("int value:" + str(int_value))
mod_rest = int_value % 10
print("int value mod_rest:" + str(mod_rest))
if mod_rest == 0:
    print("Mod 10 and rest 0 is true")
else:
    print("Mod 10 and rest 0 is false")


if mod_rest > 1 and mod_rest < 100:
    print("Mod Rest is greater than 1 and less then 100")
elif mod_rest > 100 or mod_rest < 200:
    print("Mod Rest is greater than 100 or less then 200")
elif not(mod_rest == 999):
    print("Mod Rest only value 999 is rejected")
else:
    print("end if")


# Learn Dictionary
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print("Dictionary: " + str(month_conversions["Jan"]))
print("Dictionary: " + str(month_conversions.get("any value")))

complex_dictionary = {
    "John": {
        "birth_day": 13,
        "surname": "john_doe"
    },
    "Cloe": {
        "birth_day": 11,
        "surname": "cloe_doe"
    },
}
print("Complex Dictionary: " +
      str(complex_dictionary["John"]["birth_day"]))
print("Complex Dictionary: " +
      str(complex_dictionary.get("Cloe").get("surname")))


# Learn Loop
i = 0
while i < 5:
    print(i)
    i += 1

for color in colors:
    print(color)


# Learn Try Except (try/catch)
try:
    result = 10/0
    print(int("asda"))
except ZeroDivisionError as err:  # specific error
    print(err)
except ValueError as err:
    print("\"asda\" is not a integer" + str(err))

try:
    result = 10/0
except Exception as err:  # any error
    print(err)

try:
    raise Exception("My Error Message")  # throw error
except Exception as err:  # any error
    print(err)

try:
    print("try")
except Exception as err:  # any error
    print(err)
else:
    print("Nothing went wrong")

try:
    print("try")
except Exception as err:  # any error
    print(err)
else:
    print("Nothing went wrong")
finally:
    print("finally")


# Learn Lambda

# my_num = lambda arg1: float(arg1)
# my_sum = lambda arg1, arg2: float(arg1) + float(arg2)


def my_num(arg1): return float(arg1)
def my_sum(arg1, arg2): return float(arg1) + float(arg2)


def my_func(n):
    return lambda a: a * n


print("Lambda:" + str(my_num(2)))
print("Lambda:" + str(my_sum(2, 3)))
print("Lambda:" + str(my_func(2)(3)))


# Learn Class/Objects


class SampleEmptyClass:
    my_property = "sample_empty_class"


sample_empty_class = SampleEmptyClass()
print(sample_empty_class.my_property)


class SampleWithConstructor:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


sample_with_ctor = SampleWithConstructor("Jose", 12)
print(sample_with_ctor.name + " - " + str(sample_with_ctor.age))


class SampleWithMethod:
    def __init__(self, x) -> None:
        self.x = x

    def sum_y_in_x(self, y) -> int:
        return self.x + y


sample_with_method = SampleWithMethod(10)
print(str(sample_with_method.sum_y_in_x(1)))


class SampleClassNotBeEmpty:
    pass  # use pass in empties class or __init__


sample_class_not_be_empty = SampleClassNotBeEmpty()


# Learn Inheritance


class Person:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def print_full_name(self) -> None:
        print(self.firstname + " " + self.lastname)


person = Person("Ichigo", "Kurosaki")
person.print_full_name()


class Student(Person):
    pass


student = Student("Rukia", "Kuchiki")
student.print_full_name()


class Teacher(Person):
    def __init__(self, firstname, lastname, matter) -> None:
        super().__init__(firstname, lastname)
        self.matter = matter

    def print_profile(self) -> None:
        print(self.firstname + " " + self.lastname + " - " + self.matter)


teacher = Teacher("Ishida", "Uryu", "Archer")
teacher.print_profile()


class Archer(Person):
    def __init__(self, strength) -> None:
        Person.__init__(self, "Emiya", "Shiro")
        self.strength = strength

    def print_archer(self):
        print("Name: " + self.firstname + " " +
              self.lastname + " - Strength: " + str(self.strength))


archer = Archer(12)
archer.print_full_name()
archer.print_archer()


# Learn Iterator
my_classes = ["Archer", "Lancer", "Witch", "Swordsman", "Warrior"]
my_it = iter(my_classes)
print(next(my_it))
print(next(my_it))


class SampleIterator:
    def __iter__(self):
        self.strength = 1  # initial value iterator
        return self

    def __next__(self):
        strength = self.strength  # get current value
        self.strength += 1  # fill next value
        return strength  # return value after sum


sample_iterator = SampleIterator()
it_sample_iterator = iter(sample_iterator)
print(next(it_sample_iterator))
print(next(it_sample_iterator))
print(next(it_sample_iterator))


class SampleStopIterator:
    def __iter__(self):
        self.strength = 1  # initial value iterator
        return self

    def __next__(self):
        if self.strength <= 10:
            strength = self.strength  # get current value
            self.strength += 1  # fill next value
            return strength  # return value after sum
        else:
            raise StopIteration  # Signal to end iterator


for sample_next in iter(SampleStopIterator()):
    print(str(sample_next))


# Learn Module
archer = character_class_module.CharacterClass(
    "Archer", "https://hero.fandom.com/wiki/Archer_%28Fate/stay_night%29")
archer.describe()

for characters in defaults_character_class.default_character_class:
    characters.describe()

print(dir(defaults_character_class))
print_hello()

# Learn Dates
now = datetime.datetime.now()
print(now)
print(now.strftime("%A"))

any_time = datetime.datetime(2022, 7, 22)
print(any_time)

# Learn JSON
json_loaded = json.loads('{"property":123}')
print(json_loaded["property"])

var_to_json = {
    "name": "ASD",
    "age": 123
}

print(json.dumps(var_to_json))

# Learn RegEx
phrase_1 = "batatinha quando nasce se esparrama pelo chão"
result_regex = re.search("quando nasce", phrase_1)
print(result_regex)
print(re.split("\s", phrase_1))

# Learn Http Request
response = requests.get("https://www.w3schools.com/python/demopage.htm")
print(response.status_code)
