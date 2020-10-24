# def generator():
#     for i in range(6):
#         yield  i*i
# g=generator()
# for i in g:
#     print(i)
#     o/p:0,1,4,9,16,25
# def simple():
#     yield 1
#     yield 2
#     yield 3
# for values in simple():
#         print(values)
# o/p:1,2,3

#When to use yield instead of return in Python?
#The yield statement suspends function’s execution and sends a value back to caller, but retains enough state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather them computing them at once and sending them back like a list.
#A generator function that yields 1 for first time,
# 2 second time and 3 third time
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
# # Driver code to check above generator function
# for value in simpleGeneratorFun():
#     print(value)

#Return sends a specified value back to its caller whereas Yield can produce a sequence of values. We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

#Yield are used in Python generators. A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function.
# A
# Python
# program
# to
# generate
# squares
# from
#
# 1


# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
# def nextSquare():
#     i = 1;
#
#     # An Infinite loop to generate squares
#     while True:
#         yield i * i
#         i += 1  # Next execution resumes
#         # from this point
#
#
# # Driver code to test above generator
# # function
# for num in nextSquare():
#     if num > 100:
#         break
#     print(num)

# Iterables
# When you create a list, you can read its items one by one, and it’s called iteration:
# mylist = [1, 2, 3]
# for i in mylist:
#    print(i)
#Mylist is an iterable. When you use a list comprehension, you create a list, and so an iterable

#Generators
#Generators are iterators, but you can only iterate over them once. It’s because they do not store all the values in memory, they generate the values on the fly
# mygenerator = (x*x for x in range(3))
# for i in mygenerator:
#     print(i)
#It is just the same except you used () instead of []. BUT, you can not perform for i in mygenerator a second time since generators can only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.

#Yield
#Yield is a keyword that is used like return, except the function will return a generator.

# def generator():
#     for i in range(6):
#         yield  i*i
# g=generator()
# for i in g:
#     print(i)

