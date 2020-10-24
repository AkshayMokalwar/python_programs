var=10
def fun1():
    print(var)
def fun2():
    global var
    var=6
def fun3():
    var=15


fun1()
fun2()
fun1()


# o/p:
# 10
# 6
# 6

# When we create a variable inside a function, it’s local by default.
# When we define a variable outside of a function, it’s global by default. You don’t have to use global keyword.
# We use global keyword to read and write a global variable inside a function.
# Use of global keyword outside a function has no effect

#Accessing global Variable From Inside a Function
# c = 1 # global variable
# def add():
#     print(c)
# add()

# Modifying Global Variable From Inside the Function
# c = 1 # global variable
# def add():
#     c = c + 2  # increment c by 2
#     print(c)
#
#
# add()
#
# UnboundLocalError: local variable 'c' referenced before assignment
# This is because we can only access the global variable but cannot modify it from inside the function.
#
# The solution for this is to use the global keyword.

#Changing Global Variable From Inside a Function using global
c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)


