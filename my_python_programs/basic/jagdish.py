# def improper_return_fuction(a):
#     if(a%2)==0:
#         return True
# x=improper_return_fuction(3)
# print(x)


# for i in range(1,11):
#      if i==5:
#          continue
#      print(i)
# def fuction_sum():
#     a=10
#     b=20
#     c=10+20
#     print(c)
#     return c
# fuction_sum()
# def display():
#      print("hbb")
# display()
# def if_example(a):
#      if a==1:
#           print('one')
#      elif a==2:
#           print('two')
#      else:
#           print('something else')
# if_example(2)
# if_example(4)
# if_example(1)
# names=['A''B''C']
# for i in names:
#      print('HELLO'+i)
# for i in range(0,11):
#      print(i)


# a=10
# def read():
#     print(a)
# def write():
#      global a
#      a=5
# def display():
#      a=15
# read()
# write()
# read()
# display()
# read()
# a=[1,2,3,4,5]
# print(5 in a)
# print(10 in a)
# for i in 'jagdish':
#       print(i)
# print(True is True)
# print(False is False)
# print(None is None)
# print{}=={}
# print{} is {}
# print[] is []
# print()==()
# print""==""
# print''==''
# print'' is ''
# def outer_fuction():
#      a=5
#      def inner_fuction():
#
#           a=10
#           print("inner fuction:", a)
#      inner_fuction()
#      print("outer_fuction:",a)
# outer_fuction()
# def jD_fuction():
#      pass
#   print('hello world')
# jD_fuction()
# def fuction_return():
#      a=10
#      return a
# def no_return():
#      a=10
# print(fuction_return)
# print(no_return)
# i=5
# while(i):
#  print(i)
#  i=i
# def genrator():
#       for i in range(6):
#            yield i*i
# g=genrator()
# for i in g:
#      print(i)

    # OPERATOR
# a=10
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a%b)
# print(a/b)
#
# a=10
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a%b)
# print(a/b)
# print(10//2)
# print(10.0//2)
# print(10//3)
# print(10.0//3)
# print(10**2)
# print(2**4)
# print('Sannu+jagdish')
# print('Sannu'+str(10))
# print('jagdish'+'14')
# print(10.0//0)
# print('jagdish'+'True')
# a=10
# b=20
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(10<20)
# print(10<=20)
# print(10>20)
# print(10>=20)
# a='jagdish'
# b='pardhi'
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(True>False)
# print(True<False)
# print(True>=False)
# print(True<=False)
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)
#
# print(not True)
# print(not False)
# print('jagdish'&'pardhi')
# print(10 or 20)
# print(True & False)
# print(False & True)
# print(10 <<20)
# print(10 >>20)
# print(10 ^20)
# x=10
# print(++x)
# print(+++x)
# print(--x)
# print(-+x)
# s=10
# r=20
# c=30 if s>r else 40
# print(c)
#

# a=10
# b=10
# print(a is b)
# a=10
# b=20
# print(a is b)
# l1=[10,20,30,40]
# l2=[10,20,30,40]
# print(l1)
# print(l2)
# print(l1==l2)
# print(10*2+4/4%1)
# print(1%1)
# s='hello learning python in very easy'
# print('h' in s)
# print('d'in s)
# print('d' not in s)
# print('python' in s)
# a=30
# b=20
# c=10
# d=5
# print((a+b)!=c/d)
# print((a+b)!=(c/d))
# print(a+(b+c)/d)
# print(a+(b+c)/d)
# x=888
# y=999
# def add(x,y)
#     print('performing add operation')
#     print('The sum=',x*y)
# def product(x,y):
#     print('performing multiplication operator')
#     print('The product=',x*y)

    # import dmath
    # dmath.add(10,20)
    # dmath.product(10,20)
# def is_even(n):
#     return n%2==0
# num=[1,2,3,4,5]
# evens=list(filter(is_even,num))
# print(evens)
#
# def add(n):
#     return n+n
# num=[1,2,3,4,5]
# add=list(map(add,num))
# print(add)
# def sub(n):
#     return n+n
# num=[1,2,3,4,5]
# mul=list(map(lambda x:x*x+1,num))
# print(mul)
# from functools import reduce
# def sub (x1,x2):
#     return x1+x2
# print(reduce(sub,[2,3,4,5]))
#
# from functools import reduce
# def sum (x1,x2):
#     return x1+x2
# x1=[1,2,3,4,5]
# x2=[5,4,3,2,1]
# print(reduce(sum(x1+x2)))
# ex1
# class student:
#     branch="cse"
#     rno=123
#     name="abc"
#     def read(self):
#      print("reading")
#
# s1=student()
# print("rno=",s1.rno)
# print("name=",s1.name)
# print("branch=",s1.branch)
# s1.read()
# ex2
# class student:
#     branch="cse"
#     rno=123
#     name="abc"
#     def read(self):
#         rollno=345
#         print("rollno=",rollno)
#         print("reading")
#
# abc=student()
# print("rno=",student.rno)
# print("name=",student.name)
# print("branch=",student.branch)
# abc.read()
#
# # ex3
# class student:
#     branch="cse"
#     rno=123
#     name="abc"
#     def read(self):
#         rollno=345
#         print("rollno=",rollno)
#         print("instant variable=",self.rno)
#         print("read")
# ex3
# abc=student()
# print("rno=",student.rno)
# print("name=",student.name)
# print("branch=",student.branch)
# abc.read()


# a=input("enter username")
# b=input("enter password")
# print("login")
# if a=="jagdish" and b=="12345":
#          print("login successful")
# else:
#          print("login failed")

# a=int(input("enter number"))
# b=a**3
# print(b)


