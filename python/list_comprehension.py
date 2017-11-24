numbers_0_to_9 = [x for x in range(10)]
print("Numbers 0 to 9", numbers_0_to_9)
# Numbers 0 to 9 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = [x * x for x in range(10)]
print("Squares       ", squares)
# Squares        [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

odds = [x for x in range(10) if x % 2 == 1]
print("Odds          ", odds)
# Odds           [1, 3, 5, 7, 9]


# Advanced List Comprehensions
from collections import namedtuple
Person = namedtuple("Person", ["name", "age", "gender"])

people = [
    Person("Andy", 30, "m"),
    Person("Ping", 1, "m"),
    Person("Tina", 32, "f"),
    Person("Abby", 14, "f"),
    Person("Adah", 13, "f"),
    Person("Sebastian", 42, "m"),
    Person("Carol" , 68, "f"),
]

andy = people[0]

print("name:  ", andy.name)
print("age:   ", andy.age)
print("gender:", andy.gender)


male_names = [person.name for person in people if person.gender=="m"]
print("Male names:", male_names)
# Male names: ['Andy', 'Ping', 'Sebastian']

teen_names = [p.name for p in people if 13 <= p.age <= 18 ]
print("Teen names:", teen_names)
# Teen names: ['Abby', 'Adah']
