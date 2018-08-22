#1) Create a list of names and use a for loop to output the length of each name (len() ).
#2) Add an if  check inside the loop to only output names longer than 5 characters.
#3) Add another if  check to see whether a name includes a “n”  or “N”  character.
#4) Use a while  loop to empty the list of names (via pop() )

name=["Nalita", "Olivia", "Amy", "Savannah", "Emily", "Alexander", "Matthew", "Sebastian", "Levi", "Leo"]

print("The length for each name: ")
for i in name:
    print(i,"length is ", len(i))

print("\nHere are the name which length longer than 5: ")
for i in name:
    if len(i)>5:
        print(i)

print("\nHere are the name which length longer than 5 and has N or n in it: ")
for i in name:
    if len(i)>5 and ("n" in i.lower()):
        print(i)

print("\nempty the list:")
while len(name)>=1:
    name.pop()
print(name)