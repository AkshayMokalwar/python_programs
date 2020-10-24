a=4
assert a<5
assert a>5
#we can also give messages
assert a>5,"The value of a is less than 5"

x = "hi"
# if condition returns True, then nothing happens:
assert x == "hi"
# if condition returns False, AssertionError is raised:
assert x == "hello"

x = "hello"
# if condition returns False, AssertionError is raised:
assert x == "hi", "x should be 'hello'"



batch = [40, 26, 39, 30, 25, 21]

# initializing cut temperature
# cut = 26
# using assert to check for temperature greater than cut
for i in batch:
    assert i >= 26, "Batch is Rejected"
    print(str(i) + " is O.K")


