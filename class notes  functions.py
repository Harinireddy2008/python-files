#Functions

'''def greet():
    print("hello")
greet()
greet()
greet()
greet()
greet()

def help():
    print("execute program in laptop")
help()
help()

def printOneToTen():
    for i in range(0,11):
        print(i)
printOneToTen()
printOneToTen()
printOneToTen()
    
def sum():
    a=5
    b=3
    print(a+b)
sum()
sum()
sum()

def Mul():
    a=5
    b=3
    print(a*b)
Mul()
Mul()
Mul()

def sub():
    a=5
    b=3
    print(a-b)
sub()
sub()
sub()

def div():
    a=5
    b=3
    print(a/b)
div()
div()
div()

def sum(a,b):
    print(a+b)
sum(2,3)
sum(4,5)
sum(1,1)

def greet(name):
    print("Hello",name)
greet("Ravi")
greet("sita")
greet("kiran")

def Mul(a,b,c):
    print(a*b*c)
Mul(2,3,4)
Mul(6,7,8)
Mul(5,9,1)

def sub(a,b):
    print(a-b)
sub(5,3)
sub(8,4)
sub(9,7)

def div(a,b):
    print(a/b)
div(5,3)
div(6,2)
div(5,10)

def square(a):
    print("Area for square",a*a)
square(4)

def Rectangle(a,b):
    print("Area for rectangle",a*b)
Rectangle(3,4)

#Returns

def sum(a,b):
    result=a+b
    return result

add=sum(1,2)
print(add)

def sum(a,b):
    result=a+b
    return result
task1=sum(1,2)
print(task1*5)
task2=sum(3,5)
print(task2)
task3=sum(4,9)
print(task3*2)

def sum(a,b):
    return a+b
result=sum(10,20)*5
print(result)

def sum(a,b):
    result=a+b
    return result
x=sum(1,2)
print(x*5)
y=sum(3,4)
print(y)
z=sum(4,5)
print(z*8)

def maximum(a,b):
    if a>b:
        return a
    else:
        return b
x=maximum(10,20)
print(x)

def can_vote(age):
    if age>=18:
        return True
    else:
        return False
x=can_vote(20)
print(x)

def sum_n(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
x=sum_n(5)
print(x)

def reverse_number(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev
x=reverse_number(7789)
print(x)


def palindrome(n):
    rev=0
    temp=n
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if temp==rev:
        return True
    else:
        return False
    
x=palindrome(121)
print(x)


def total(price,quantity):
    result=price*quantity
    return result
x=total(100,5)*0.9
print(x)

def total_marks(m1,m2,m3):
    return m1+m2+m3
x=total_marks(80,75,90)/300*100
print(x)

#or

def total_marks(m1,m2,m3):
    return m1+m2+m3
x=total_marks(80,75,90)
perc=x/300*100
print(perc)

def sum(a,b,c):
    print(a)
    print(b)
    print(c)
sum(b=5,a=3,c=2)

def mult(a,b,c,d):
    print(a*b*c*d)
mult(1,2,3,4)#positional method
mult(c=5,d=3,a=4,b=7)#keyword method

#default method

def sum(a,b,c=5):
    print(a)
    print(b)
    print(c)
sum(1,2)

def greet(name,msg="Hai"):
    print(msg,name)
greet("ravi")
greet("raju","hello")

def Mul(a,b,c):
    print(a*b*c)
Mul(b=9,c=4,a=3)

def Mul(a,b=5,c=4):
    print(a*b*c)
Mul(3,9)

def div(a,b):
    print(a/b)
div(b=10,a=9)

def div(a=8,b=4):
    print(a/b)
div(9,10)

def square(a=5):
    print("Area of square:",a*a)
square(2)

def square(a):
    print("Area of square:",a*a)
square(a=2)

def sub(a,b,c):
    print(a-b-c)
sub(b=3,c=4,a=10)

def sub(a,b=3,c=4):
    print(a-b-c)
sub(10)

def sub(a,b,c=4):
    print(a-b-c)
sub(10,3)

def sub(a=5,b=6,c=9):
    print(a-b-c)
sub(10,3,4)

def sub(a=5,b,c=9):
    print(a-b-c)
sub(10,3,4)

#variable-length  positional Arguments

def help(b,*a):
    print(a,b)
    print(type(a))
help(1,2)
help(4,5,6,7)



def help(*a,b):
    print(a,b)
    print(type(a))
help(1,2,b=3)
help(4,5,6,b=7)


def help(c,*a,b):
    print(a,b,c)
    print(type(a))
help(1,2,3,b=8)
help(4,5,6,7,b=15)


def help(*c,b):
    print(c,b)
help(7,8,9,b=22)

#variable-length keyword Arguments

def help(**a):
    print(a)
    print(type(a))
help(b=7,c=8,d=12,f=16,z=111)

def student(**details):
    print(details)
    print(type(details))
    print(details['name'])
    
student(name="Ravi",age=25,city="Hyderabad")



def student(*a,**details):
    print(a,details)
    print(type(details))
    print(details['name'])
    
student(1,2,name="Ravi",age=25,city="Hyderabad")


#unpacking

num=[1,2,3]
a,b,c=num
print(a,b,c)

num=[1,2,3,4,5,6]
a,*b=num
print(a,b)
*c,d=num
print(c,d)
x,*y,z=num
print(x,y,z)
m,n,*p=num
print(m,n,p)

numbers=[10,20,30,40,50]
a,*b=numbers
print(a,b)


numbers=(10,20,30,40,50)
a,*b=numbers
print(a,b)
*c,d=numbers
print(c,d)
x,*y,z=numbers
print(x,y,z)

#Multiple return value

def help(a,b):
    s=a+b
    p=a*b
    sub=a-b
    return s,p,sub
x,y,y2=help(2,3)
print(x,y,y2)
z=help(7,8)
print(z)

#scope of variables
#local variable
def help():
    a=10
    print(a)
help()

#global variable
a=10
def help():
    print(a)
help()
print(a)


a=10
def help():
    a=20
    print(a)
help()
print(a)


a=10
def help():
    global a
    a=40
    print(a)
help()
print(a)

#==========Lambda|anonymous function============
#Ex:Add two numbers
add2=lambda a,b:a+b
y=add2(7,8)
print(y)

#square
square=lambda a:a*a
print(square(5))

#max of two numbers
maxi=lambda a,b:max(a,b)
print(max(2,3))

#min of 3 num
mini=lambda a,b,c:min(a,b,c)
print(min(3,4,5))

#uppercase
convert=lambda a:a.upper()
print(convert("abc"))

#check given number is even or odd if even true else flase
check=lambda a:a%2==0
print(check(7))

#===================Map===============

#convert every value in upper case
n1=["abc","ravi","raju","ramu"]
result=list(map(lambda a:a.upper(),n1))
print(result)

#add 10 to every number
a=[12,4,5,8,15]
result=list(map(lambda a:a+10,a))
print(result)

#creat a list containing their cubes
num=[1,2,3,4,5]
result=list(map(lambda a:a**3,num))
print(result)

#celsius Formula=c*9/5+32
celsius=[0,10,20,30,40]
result=list(map(lambda c:(c*9/5+32),celsius))
print(result)'''

#================Filter==========

#even or odd
num=[3,4,5,6,7,8]
result=list(filter(lambda a:a%2==0,num))
print(result)

#vote eligible
num=[18,19,20,25,17]
result=list(filter(lambda a:a>=18,num))
print(result)

#extract odd numbers
a=[13,4,5,6,7,8,9]
result=list(filter(lambda a:a%2==1,a))
print(result)

#extract greater than 50
a=[55,24,52,67,11,44]
result=list(filter(lambda a:a>=50,a))
print(result)

#extract all positive numbers
a=[-2,4,5,6,-11,3,8,9,1]
result=list(filter(lambda a:a>0,a))
print(result)

#number divisible by 5
a=[15,2,20,3,17,25,30,45]
result=list(filter(lambda a:a%5==0,a))
print(result)

#Extract names whose length is greater than 5

name=["Ram","Alexander","josh","harini"]
result=list(filter(lambda a:len(a)>5,name))
print(result)













