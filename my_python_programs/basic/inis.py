# for i in 'hello':
#     print(i)

# do it in command prompt
# list1=[1,2,3,4,5]
# list2=[6,7,8,9]
# for item in list1:
#     if item in list2:
#         print("overlapping")
# else:
#     print("not overlapping")

x = 24
y = 20
list = [10, 20, 30, 40, 50];
if (y not in list):
   print ("x is  present in given list")
else:
    print ("x is NOT present in given list")



#‘is’ operator – Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
x = 5
if (type(x) is int):
    print ("true")
else:
    print ("false")

x = 5.2
if (type(x) is not int):
    print ("true")
else:
    print ("false")

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)
# Output: True
print(x2 is y2)
# Output: False
print(x3 is y3)
print(id(x3))
print(id(y3))
print(id(x1))
print(id(y1))






