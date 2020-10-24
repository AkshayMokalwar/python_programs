i=10
if i%2==0:
    print("Even")
else:
    print("Odd")

for i in [1,2,3]:
    if(i==1):
        print("One")
    elif(i==2):
        print("Two")
    else:
        print("three")
# o/p:one Two three

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")
#
num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

num = 3
# Try these two variations as well.
num = -5
num = 0
if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")

num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

var = 100
if var == 200:
   print("1 - Got a true expression value")
   print (var)
elif var == 150:
   print("2 - Got a true expression value")
   print (var)
elif var == 100:
   print("3 - Got a true expression value")
   print (var)
else:
   print ("4 - Got a false expression value")
   print (var)

print ("Good bye!")

i = 20
if (i == 10):
    print ("i is 10")
elif (i == 15):
    print ("i is 15")
elif (i == 20):
    print ("i is 20")
else:
    print ("i is not present")

num = 1122
if 9 < num < 99:
    print("Two digit number")
elif 99 < num < 999:
    print("Three digit number")
elif 999 < num < 9999:
    print("Four digit number")
else:
    print("number is <= 9 or >= 9999")



