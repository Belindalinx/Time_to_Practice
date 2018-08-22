#Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.

person = [{"name": "Alice", "age": "25", "hobbies": ["music", "art", "coloring"]},
          {"name": "Bob", "age": "27", "hobbies": ["science", "gaming", "sleep"]},
          {"name": "Corgi", "age": "3", "hobbies": ["ball", "run", "eat"]}
          ]

#Use a list comprehension to convert this list of persons into a list of names (of the persons).
"""
name = []
for i in person:
    for k, v in i.items():
        if k == "name":
            name.append(v)
"""

name=[i["name"] for i in person]
print(name)

#Use a list comprehension to check whether all persons are older than 20.
"""
age = []
for i in person:
    for k, v in i.items():
        if k == "age":
            age.append(int(v))

if all(age) > 20:
    print("All persons are older than 20.")
else:
    print("All persons are not older than 20.")
"""

age=all([int(i["age"]) >20 for i in person])
print(age)


#Copy the person list such that you can safely edit the name of the first person (without changing the original list).
c_person = [i.copy() for i in person]
c_person[0]["name"] = "Gina"
print(person)
print(c_person)

#Unpack the persons of the original list into different variables and output these variables.

a, b, c, = person
print(a)
print(b)
print(c)


