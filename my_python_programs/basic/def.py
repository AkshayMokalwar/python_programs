#The def keyword is used to create, (or define) a function.
#In Python, function is a group of related statements that perform a specific task.

def add(n,m):
    return n+m
print(add(10,20))
#o/p 30

# def fun():
#     print("Function is called")
# fun()
# o/p:Function is called

def typeOfNum(num): # Function header
    # Function body
    if num % 2 == 0:
        def message():
            print("You entered an even number.")
    else:
        def message():
            print("You entered an odd number.")
    message()
# # End of function
#
typeOfNum(2)  # call the function
typeOfNum(3)  # call the function again

# Function definition is here
# def printme(str):
#    "This prints a passed string into this function"
#    # return
#    print(str)
#    return
#
# # Now you can call printme function
# printme("I'm first call to user defined function!")
# printme("Again second call to the same function")


#def changeme( mylist ):
   #"This changes a passed list into this function"
   #mylist.append([1,2,3,4]);
   #print ("Values inside the function: ", mylist)


# Now you can call changeme function
#mylist = [10,20,30];
#changeme( mylist );
#print("Values outside the function: ", mylist)

# Function definition is here
#def changeme(mylist):
   #"This changes a passed list into this function"
   #mylist = [1,2,3,4]; # This would assign new reference in mylist
   #print("Values inside the function: ", mylist)


# Now you can call changeme function
#mylist = [10,20,30];
#changeme( mylist );
#print("Values outside the function: ", mylist)

# Function definition is here
# def printme(str):
#    "This prints a passed string into this function"
#    print(str)
   # return;
   # return str

# Now you can call printme function
# printme(str = "My string")
# print(str)
# Function definition is here

def printinfo(name, age ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )

# Nested Function
def function1(): # outer function
    print ("Hello from outer function")
    def function2(): # inner function
        print ("Hello from inner function")
    function2()

function1()

# def function1(): # outer function
#     print ("Hello from outer function")
#     def function2(): # inner function
#         print ("Hello from inner function")
#     function2()
# function1()


def function1(): # outer function
    x = 2 # A variable defined within the outer function
    def function2(a): # inner function
       # Let's define a new variable within the inner function
       # rather than changing the value of x of the outer function
        x = 6
        print (a+x)
    print (x) # to display the value of x of the outer function
    function2(3)

function1()


def outer_function(x):
    # Hidden from the outer code
    def inner_increment(x):
        return x + 2
    y = inner_increment(x)
    print(x, y)

# inner_increment(5)
outer_function(5)

# def f1(): #outer function
#     print ("Hello")
#     def f2(): #inner function
#         print ("world")
#     f2()
#
# f1()

#def f1(): #outer function
    #x = 1 # variable defined in the outer function
    #def f2(a): #inner function
       #will create a new variable in the inner function
       #instead of changing the value of x of outer function
        #x = 4
        #print (a+x)
    #print (x) # prints the value of x of outer function
    #f2(2)

#f1()

# a = 1
# def f1():
#    a = 5
#    print(a) #will print 5
# print (a) #will print 1
# f1()

def f1(): #outer function
    a = 1
    def f2(): #inner function
        print(a) #will print 1
    f2()
f1()



# def f1(a):
#     def f2(b):
#         return a+b
#     return f2
# a = f1(1)
# b = f1(100)
#
# print (a(2))
# print (b(2))

# for comment we have to use shortcut key ctrl+/.




