
# syntax and examples
# lambda p1, p2:expression


# ex1
adder=lambda x,y:x+y
# print(adder(1,4))


# not working****************8
# string='some kind of a useless lambda'
# print(lambda string:print(string))
 
# x="some kind of a   aaaaaaaaaaaaaaa"
# print(lambda x:print(x))(x)

# **********************8

# x="some kind of a useless lambda"
# (lambda x : print(x))(x)


# Regular Function
def guru(funct, *args):
    funct(*args)

def printer_one