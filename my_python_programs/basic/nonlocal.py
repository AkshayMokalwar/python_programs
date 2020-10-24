#global and local variable with different name

# x="global"
# #global variable can be accessed from anywhere
# def funct1():
#     global x
#     y="local"
#     x=x*2
#     print(x)
#     print(y)
#
# print("Global x= ",x)
# funct1()
# print("Global x= ",x)




# -----------------------------------------------------------------------------------Global and Local variable with same name----------------------------------------------------------------------------------
a=5
def funct2():
    a=10 #local variables are accessed from the block where it is defined only
    print("local a:",a)

print("global a:",a)
funct2()
print("global a:",a)


#creating and using a non local variable
# def outer():
#     x="local" #x will be updated after define x is non local
#     def inner():
#         nonlocal x #Nonlocal vriable are used in nested function
#         x="nonlocal"
#         print("inner",x)
#
#     inner()
#     print("outer:",x)
# outer()
#
# # o/p:inner: nonlocal
# #     outer: nonlocal
#
# def outer():
#     x="local"
#     def inner():
#         # nonlocal x #Nonlocal vriable are used in nested function
#         x="nonlocal"
#         print("inner",x)
#
#     inner()
#     print("outer:",x)
# outer()

# o/p: inner nonlocal
# outer: local

# Global Variables
# In Python, a variable declared outside of the function or in global scope is known as global variable. This means, global variable can be accessed inside or outside of the function.
# x = "global"
#
# def foo():
#     print("x inside :", x)
#
# foo()
# print("x outside:", x)

# Local Variables
# A variable declared inside the function's body or in the local scope is known as local variable
# def foo():
#     y = "local"
#
# foo()
# print(y)
# NameError: name 'y' is not defined
#The output shows an error, because we are trying to access a local variable y in a global scope whereas the local variable only works inside foo() or local scope

# def foo():
#     y = "local"
#     print(y)
#
# foo()

#Using Global and Local variables in same code
# x = "global"
#
#
# def foo():
#     global x
#     y = "local"
#     x = x * 2
#     print(x)
#     print(y)
#
#
# foo()

#Global variable and Local variable with same name
# x = 5
#
# def foo():
#     x = 10
#     print("local x:", x)
#
# foo()
# print("global x:", x)
#In above code, we used same name x for both global variable and local variable. We get different result when we print same variable because the variable is declared in both scopes, i.e. the local scope inside foo() and global scope outside foo().

#When we print the variable inside the foo() it outputs local x: 10, this is called local scope of variable.

#Similarly, when we print the variable outside the foo(), it outputs global x: 5, this is called global scope of variable.

# Nonlocal Variables
# Nonlocal variable are used in nested function whose local scope is not defined. This means, the variable can be neither in the local nor the global scope.
#
# Let's see an example on how a global variable is created in Python.
#
# We use nonlocal keyword to create nonlocal variable.
# def outer():
#     x = "local"
#
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
#
#     inner()
#     print("outer:", x)


# outer()


#In the above code there is a nested function inner(). We use nonlocal keyword to create nonlocal variable. The inner() function is defined in the scope of another function outer().

#Note : If we change value of nonlocal variable, the changes appears in the local variable

# def myfunc1():
#   x = "John"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2()
#   return x
#
# print(myfunc1())

# def myfunc1():
#   x = "John"
#   def myfunc2():
#     x = "hello"
#   myfunc2()
#   return x
#
# print(myfunc1())


