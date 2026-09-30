#Harshad Number
sum=0
n=int(input("Enter your num:"))
c=n
while c>0:
    r=c%10
    sum=sum+r
    c=c//10
if n%sum==0:
    print(n,"is Harshad Number")
else:
    print(n,"is not Harshad Number")

#Fibonacci series
n=int(input("Enter your n:"))
a=0
b=1
print(a,b,end=" ")
for i in range(n-2):
     c=a+b
     a=b
     b=c
     print(c,end=" ")

#or

n=int(input("Enter your n:"))
a=0
b=1
print(a,b,end=" ")
for i in range(2,n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

#gcd/hcf
n1=int(input("Enter your n1:"))
n2=int(input("Enter your n2:"))
gcd=1
for i in range(1,min(n1,n2)+1):
     if n1%i==0 and n2%i==0:
          gcd=i
print("GCD is:", gcd)

#Deficient number

n=int(input("Enter your n:"))
sum=0
for i in range(1,n):
     if n%i==0:
          sum=sum+i
if sum<n:
     print(sum,"is a Deficient number")
else:
     print(sum,"Not a Deficient number")

     




