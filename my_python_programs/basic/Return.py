def func_return():
    a=10
    return  a
def no_return():
    a=10;
print(func_return())
print(no_return())

#Functions can have optional parameters, also called default parameters. Default parameters are parameters, which don't have to be given, if the function is called. In this case, the default values are used. We will demonstrate the operating principle of default parameters with an example. The following little script, which isn't very useful, greets a person. If no name is given, it will greet everybody:
# def Hello(name="everybody"):
#     """ Greets a person """
#     print("Hello " + name + "!")
#
# Hello("Peter")
# Hello()

#The first statement in the body of a function is usually a string, which can be accessed with function_name.__doc__
#This statement is called Docstring.
#Example:
# def Hello(name="everybody"):
#     """ Greets a person """
#     print("Hello " + name + "!")
#
# print("The docstring of the function Hello: " + Hello.__doc__)

#Using keyword parameters is an alternative way to make function calls. The definition of the function doesn't change.
def sumsub(a, b, c=0, d=0):
    return a - b + c - d

print(sumsub(12,4))
print(sumsub(42,15,d=10))

#In our previous examples, we used a return statement in the function sumsub but not in Hello. So, we can see that it is not mandatory to have a return statement. But what will be returned, if we don't explicitly give a return statement. Let's see:
def no_return(x,y):
    c = x + y
    return c;
res = no_return(4,5)
print(res)

def empty_return(x,y):
    c = x + y
    return

res = empty_return(4,5)
print(res)


