#Recursion

'''def help():
    print("hello")
    help()
help()

#print hello  5 times using  recursion

def help(n):
    if n==0:
        return
    print("hello")
    help(n-1)
help(5)

def help(n):
    if n==0:
        return
    print("harini")
    help(n-1)
help(7)

def help(i,n):
    if i>n:
        return
    print(i)
    help(i+1,n)
help(1,5)

#reverse 5 to 1 homework 

def help(i,n):
    if i<n:
        return
    print(i)
    help(i-1,n)
help(5,1)

#sum of numbers homework

def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
x=sum(5)
print(x)


#factors

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
ans=fact(5)
print(ans)

#fibonacci

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(6))


#=============module =========

import math
print(math.sqrt(25))
print(math.pow(2,3))
print(math.ceil(5.6))
print(math.floor(5.6))
print(math.factorial(5))
print(math.fabs(-10))
print(math.gcd(12,24))
print(math.sin(0))
print(math.tan(45))
print(math.pi)
print(math.e)


#random module

import random
print(random.random())
print(random.randint(0,10))
print(random.choice([10,20,30,40,50]))
abc=[10,20,30,40,50]
random.shuffle(abc)
print(abc)
print(random.sample([10,20,30,40,50],2))

#importing  specific items

from math import sqrt,ceil,pi
print(sqrt(25))
print(ceil(5.6))
print(pi)'''









































