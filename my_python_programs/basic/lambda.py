# def square(a):
#     return a*a
#     # print(a)
# result=square(5)
# print(result)
# o/p:25

# f=lambda a:a*a
# print(f(5))
# result=f(5)
# print(result)

# o/p:25

# f=lambda a,b:a+b
# result=f(5,6)
# print(result)
# o/p:11
#we can pass number of argument but it should be one expression

#A lambda function that adds 10 to the number passed in as an argument, and print the result:

# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

# def myfunc(n):
#   return lambda a : a * n
#
# mydoubler = myfunc(2)
#
# print(mydoubler(11))

# def myfunc(n):
#   return lambda a : a * n
#
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# #
# print(mydoubler(11))
# print(mytripler(11))

# showing difference between def() and lambda().
# def cube(y):
#     return y * y * y;
#
#
# g = lambda x: x * x * x
# print(g(7))
#
# print(cube(5))

# Without using Lambda : Here, both of them returns the cube of a given number. But, while using def, we needed to define a function with a name cube and needed to pass a value to it. After execution, we also needed to return the result from where the function was called using the return keyword.
# Using Lambda : Lambda definition does not include a “return” statement, it always contains an expression which is returned. We can also put a lambda definition anywhere a function is expected, and we don’t have to assign it to a variable at all. This is the simplicity of lambda functions.
# Lambda functions can be used along with built-in functions like filter(), map() and reduce().

# Use of lambda() with filter()
#
# The filter() function in Python takes in a function and a list as arguments. This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True. Here is a small program that returns the odd numbers from an input list:

# Python code to illustrate
# filter() with lambda()
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(filter(lambda x: (x%2 != 0) , li))
# print(final_list)

#Use of lambda() with map()

#The map() function in Python takes in a function and a list as argument. The function is called with a lambda function and a list and a new list is returned which contains all the lambda modified items returned by that function for each item. Example:
# Python code to illustrate
# map() with lambda()
# to get double of a list.
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(map(lambda x: x*2 , li))
# print(final_list)

#Use of lambda() with reduce()

#The reduce() function in Python takes in a function and a list as argument. The function is called with a lambda function and a list and a new reduced result is returned. This performs a repetitive operation over the pairs of the list. This is a part of functools module.
# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print (sum)


