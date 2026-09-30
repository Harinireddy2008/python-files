age=18
if age>=18:
   print("you can register")

age=17
if age>=18:
    print("you can register")

balance=10000
withdraw=5000
if balance>=withdraw:
    print("withdraw done")

balance=10000
withdraw=11000
if balance>=withdraw:
    print("withdraw done")


temp=42
if temp>40:
    print("High Temperature Alert")


attendance=75
if attendance>=75:
    print("eligible to write exams")

age=20
if age>=18:
    print("you can register")
else:
    print("you can't register")

age=16
if age>=18:
    print("you can register")
else:
    print("you can't register")


balance=10000
withdraw=9000
if balance>=withdraw:
    print("withdraw done")
else:
    print("insufficient balance")

balance=10000
withdraw=11000
if balance>=withdraw:
    print("withdraw done")
else:
    print("insufficient balance")

n=30
if n%2==0:
    print(n,"is even number")
else:
    print(n,"is odd number")

n=int(input("enter the number"))
if n%2==0:
    print(n,"is even number")
else:
    print(n,"is odd number")

marks=40
if marks>=40:
    print("student is pass")
else:
    print("student is Fail")

marks=30
if marks>=40:
    print("student is pass")
else:
    print("student is Fail")

marks=75
if marks>=90:
    print("A grade")
elif marks>=80:
    print("B grade")
elif marks>=50:
    print("C grade")
elif marks>=40:
    print("D grade")
else:
    print("Fail")

marks=int(input("enter your marks"))
if marks>=90:
    print("A grade")
elif marks>=80:
    print("B grade")
elif marks>=50:
    print("C grade")
elif marks>=40:
    print("D grade")
else:
    print("Fail")

n=int(input("enter n:"))
if n==1:
    print("check balance")
elif n==2:
    print("withdraw")
elif n==3:
    print("deposit")
else:
    print("exit")

units=int(input("enter units:"))
if units>500:
    print("very high usage")
elif units>300:
    print("high usage")
elif units>100:
    print("medium usage")
else:
    print("low usage")

rating=int(input("enter rating:"))
if rating==5:
    print("Excellent")
elif rating==4:
    print("very good")
elif rating==3:
    print("Good")
elif rating==2:
    print("average")
else:
    print("poor")

n=5
if n>0:
    print("n is positive")
    if n%2==0:
        print("even")
    else:
        print("odd")
else:
    print("n is negative")

n=-1
if n>0:
    print("n is positive")
    if n%2==0:
        print("even")
    else:
        print("odd")
else:
    print("n is negative")

    
pin=1234
balance=10000
withdraw=9000
if pin==1234:
   if balance>=withdraw:
       print("withdraw successful")
   else:
       print("insufficient balance")
else:
    print("invalid pin")

member=input("Enter your member")
purchase=6000
if member=="yes":
   print("prime member")
   if purchase>=5000:
      print("20%discount")
   else:
      print("10%discount")
else:
   print("not prime member")
   if purchase>=5000:
      print("10%discount")
   else:
      print("No discount")


member=input("Enter your member")
purchase=6000
if member=="yes":
   print("prime member")
   if purchase>=5000:
      print("20%discount",purchase*0.8)
   else:
      print("10%discount",purchase*0.9)
else:
   print("not prime member")
   if purchase>=5000:
      print("10%discount",purchase*0.9)
   else:
      print("No discount")

marks=int(input("Enter your marks"))
if marks>=40:
   if marks>=75:
       print("distinction")
   else:
      print("pass")
else:
   print("Fail")
   
age=int(input("Enter your age"))
if age>=18:
   if age>=60:
      print("senior citizen")
   else:
      print("Adult")
else:
   print("no ticket")

n=int(input("Enter your num"))
if n>0:
   print("n is positive")
   if n%2==0:
      print("even")
   else:
      print("odd")
elif n<0:
     print("n is negative")
else:
    print(" n is zero")

ch='a'
if ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u'or ch=='A'or ch=='E'or ch=='I'or ch=='O'or ch=='U':
   print("True")
else:
   print("False")
#or
ch='a'
if ch in "aeiouAEIOU":
   print(True)
else:
   print(False)

degree=input("enter your degree")
experience=3
if degree=="yes":
    if experience>=2:
       print("Eligible for Interview")
    else:
       print("Fresher Interview")
else:
   print("Not Eligible")
   
marks=80
income=10000
if marks>=80:
   if income<300000:
      print("100%")
   elif income>300000 and income<600000:
        print("50%")
   else:
      print("25%")
else:
    print("not eligible")







