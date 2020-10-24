for i in range(10):
    if(i%2!=0):
       pass
    # pass the statement if condition is true
    else:
        print(i)

for num in range(6):
    if(num==3):
        pass
    else:
        print(num)

#What is pass statement in Python?
#In Python programming, pass is a null statement. The difference between a comment and pass statement in Python is that, while the interpreter ignores a comment entirely, pass is not ignored.

#However, nothing happens when pass is executed. It results into no operation (NOP).

#Syntax of pass
#pass
#Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. They cannot have an empty body. The interpreter would complain. So, we use the pass statement to construct a body that does nothing.
# pass is just a placeholder for
# functionality to be added later.
# sequence = {'p', 'a', 's', 's'}
# for val in sequence:
#     pass

# for letter in 'Python':
#    if letter == 'h':
#       pass
#       print ('This is pass block')
#    print ('Current Letter :', letter)
#
# print("Good bye!")

