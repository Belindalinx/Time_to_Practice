#Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.

def normal(a):
    print(a(2))
    return

#Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.

normal(lambda a: a*2)

#Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.

def norm(b, *args):
    for arg in args:
        print(b(arg))

norm(lambda b: b * 2, 4, 6)

#Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.

def no(c, *args):
    for arg in args:
        print("{:^20.1f}".format(c(arg)))

no(lambda c: c * 2, 4, 6)
