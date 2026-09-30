'''day=2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Invalid day")


day="Monday"
match day:
    case"Monday":
        print(1)
    case"Tuesday":
        print(2)
    case"wednesday":
        print(3)
    case"Thursday":
        print(4)
    case"Friday":
        print(5)
    case _:
        print("Invalid day")

option=2
match option:
    case 1:
        print("check Balance")
    case 2:
        print("withdraw Money")
    case 3:
        print("Deposit Money")
    case 4:
        print("Exit")
    case _:
        print("Invalid option")

option=3
match option:
    case 1:
        print("you selected pizza-200")
    case 2:
        print("you selected Burger-100")
    case 3:
        print("you selected Biryani-250")
    case 4:
        print("you selected Dose-50")
    case _:
        print("Invalid option")

n1=[1,3.14,"hello",True]
print(n1)
n2=[2,"abcd",2.98,False,3,5]
print(n2)
a=3
b=4.14
n3=[a,b]
print(n3)
c,d,e=3,4,5
print(c)
n1=[1,3.14,"hello",True]
print(n1[-1])
n2=['😊','😂','🤣','😒','🙌','👍👌','😁']
print(n2[2])

print(list(range(1,10)))
print(list(range(10)))
print(list(range(1,10,2)))
print(list(range(4,20,3)))
print(list(range(5,20,2)))
print(list(range(5,0,-1)))
print(list(range(10,0,-2)))

for i in range(5):
    print("Hello")
for i in range(1,6):
    print("Hello")
for i in range(5):
    print(i)
for i in range(1,1001):
    print(i)
for i in range(0,51,2):
    print(i)
for i in range(1,50,2):
    print(i)
for i in range(10,0,-1):
    print(i)
for i in range(10,-1):
    print(i)
for i in range(10,-11,-1):
    print(i)

for i in range(1,21):
    print(7,'*',i,'=',7*i)

sum=0
for i in range(1,11):
    sum=sum+i
print("sum is:",sum)

for i in range(1,11):
    sum=0
    sum=sum+i
print("sum is:",sum)

sum=0
for i in range(0,51,2):
    sum=sum+i
print("sum is:",sum)

sum=0
for i in range(1,50,2):
    sum=sum+i
print("sum is:",sum)


for i in range(0,51,1):
    if i%2==0:
        print(i)

sum=0
for i in range(0,51,1):
    if i%2==0:
        sum=sum+i
print("sum is:",sum)
    
sum=0
for i in range(0,51,1):
    if i%2==1:
        sum=sum+i
print("sum is:",sum)

count=0
for i in range(1,51):
    if i%2==0:
        count=count+1
print(count)
    
count=0
for i in range(1,51):
    if i%3==0:
        count=count+1
print(count)

fact=1
for i in range(1,6):
    fact=fact*i
print("fact is:",fact)

fact=1
for i in range(5,0,-1):
    fact=fact*i
print("fact is:",fact)

fact=1
n=int(input("enter n"))
for i in range(1,n+1):
    fact=fact*i
print(fact)

count=1
while count<=5:
    print(count)
    count=count+1

count=10
while count>=1:
    print(count)
    count=count-1

count=0
while count<=50:
    if count%2==0:
        print(count)
    count+=1
count=0
while count<=50:
    if count%2==1:
        print(count)
    count+=1'''

n=7789

while n>0:
    rem=n%10
    print(rem,end=",")
    n=n//10

n=7789
count=0
while n>0:
    n=n//10
    count=count+1
print(count)

n=7789
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem#or lastdigit
    n=n//10
print(rev)

n=121
rev=0
temp=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if temp==rev:
    print("palindrome")
else:
    print("not a palindrome")

n=7789
rev=0
temp=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if temp==rev:
    print("palindrome")
else:
    print("not a palindrome")

n=int(input("enter your n:"))
for i in range(1,n+1):
      if n%i==0:
         print(i)


n=24
i=1
while i<(n+1):
    if n%i==0:
        print(i)
    i+=1

n=28
sum=0
for i in range(1,n):
      if n%i==0:
         sum=sum+i
print(sum)
if sum==n:
      print("perfect number")
else:
      print("not a perfect number")


n=28
count=0
for i in range(1,n+1):
      if n%i==0:
         count=count+1
print(count)


n=int(input("enter n"))
count=0
for i in range(1,n+1):
      if n%i==0:
         count=count+1 
if count<=2:
      print("prime number")
else:
      print("not a prime number")
     

n=7
count=0
for i in range(1,n+1):
      if n%i==0:
         count=count+1
if count<=2:
      print("prime number")
else:
      print("not a prime number")

for i in range(1,4):
      for j in range(1,4):
            print(i,j)


for i in range(1,4):
      for j in range(1,4):
            print(i,j)

for i in range(1,5):
      for j in range(1,5):
            print(i,j)

for i in range(0,1000):
      for j in range(0,1000):
            print(i,j)

for i in range(0,12):
      for j in range(1,15):
            print(i,j)

#vertical
n=int(input("enter n:"))
for i in range(0,n):
      print("*")
 #hor
n=5
for i in range(0,n):
      print("*",end="")

#square pattern
n=5
for i in range(0,n):
      for j in range(0,n):
            print("*",end="")
      print()
    
 #or     
n=5
for i in range(0,n):
      for j in range(0,n):
            print("*",end="")
      print(end="\n")
      
#stars like 1234
n=5    
for i in range(0,n):
      for j in range(0,i+1):
            print("*",end="")
      print(end="\n")
      
#rev the stars
      
n=5
for i in range(0,n):
      for j in range(0,n-i):
            print("*",end="")
      print(end="\n")


#or

n=5
for i in range(n,0,-1):
      for j in range(0,i):
            print("*",end="")
      print(end="\n")

#space
n=5
for i in range(0,n):
      for j in range(0,n-i-1):
          print(" ",end="")
      for j in range(0,i+1):
           print("* ",end="")
      print()

#rev space
n=5
for i in range(n-1,-1,-1):
      for j in range(0,n-i-1):
          print(" ",end="")
      for j in range(0,i+1):
           print("* ",end="")
      print()
      
# square number pattern

n=5
for i in range(1,n+1):
      for j in range(1,n+1):
            print(j,end=" ")
      print()
      
#number pattern
n=5
for i in range(1,n+1):
      for j in range(1,i+1):
         print(j,end="")
      print()
#rev pattern
n=5
for i in range(n,0,-1):
      for j in range(1,i+1):
          print(j,end="")
      print()
#numbers like 123456789
n=5
a=0
for i in range(1,n+1):
      for j in range(1,i+1):
           print(a+1,end="")
           a=a+1
      print()

    
    
    

    
    
    

        
