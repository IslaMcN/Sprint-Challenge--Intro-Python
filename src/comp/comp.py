# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
for x in humans:
    if x.name[0] == 'D':
        a1 = f'{x.name}'
        a.append(a1)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
for x in humans:
    if x.name[-1] == 'e':
        b1 = f'{x.name}'
        b.append(b1)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []

for x in humans:
    if x.name[0] == 'D':
        c5 = f'{x.name}'
        c.append(c5)
    if x.name[0] == 'C':
        c1 = f'{x.name}'
        c.append(c1)
    if x.name[0] == 'F':
        c2 = f'{x.name}'
        c.append(c2)
    if x.name[0] == 'E':
        c3 = f'{x.name}'
        c.append(c3)
    if x.name[0] == 'G':
        c4 = f'{x.name}'
        c.append(c4)
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
for x in humans:
    if x.age >= 10:
        d1 = x.age + 10
       
        d.append(d1)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for x in humans:
    e1 = f'{x.name}-{x.age}'
    e.append(e1)
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for x in humans:
    if x.age <= 32:
        if x.age > 27:
            f1 = (f'{x.name}, {x.age}')
            f.append(f1)

print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
for x in humans:
    g1 = f'{x.name.upper()}, {x.age}'
    g.append(g1)
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
for x in humans:
    h1 = math.sqrt(x.age)
    h.append(h1)
print(h)
