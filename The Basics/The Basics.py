#1) Create two variables – one with your name and one with your age
#2) Create a function which prints your data as one string
#3) Create a function which prints ANY data (two arguments) as one string
#4) Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)

name=input("Waht's your name?")
age=int(input("How old are you?"))

def display():
    print(name,"is", age, "years old and already lived",decades(age), "decade(s) in the world.")
    return

def decades(age):
    decades=age//10
    return decades

display()
