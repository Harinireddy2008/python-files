 #online shopping free delivery
ordervalue =1000
if ordervalue>=1000:
    print("Free Delivery")

#login security
balance=900
if balance<1000:
   print("Maintain minimum balance")

#online payment
pin=int(input("enter your pin:"))
if pin==9876:
    print("payment successful")
else:
    print("Invalid PIN")

#Movie Ticket Age check
age=int(input("enter your age:"))
if age<13:
    print("child ticket")
else:
    print("Regular ticket")

#password validation
password=(input("enter your password:"))
if password == "python":
    print("login successful")
else:
    print("Incorrect password")

#Traffic signal
color=input("enter your color")
if color=="red":
    print("stop")
elif color=="yellow":
    print("Get Ready")
elif color=="green":
    print("Go")
else:
    print("Invalid signal")

#mobile data usage
data=int(input("enter your data:"))
if data>5:
    print("very high usage")
elif data>3:
    print("high usage")
elif data>1:
    print("Normal Usage")
else:
    print("Low Usage")

#Employee performance
score=int(input("Enter your score:"))
if score>=90:
    print("outstanding")
elif score>=75:
    print("Excellent")
elif score>=60:
    print("Good")
elif score>=40:
    print("Average")
else:
    print("Needs Improvement")

#college Exam Eligibility
att=80
marks=60
if att>=75:
    print("Eligible")
    if marks>=40:
        print("Eligible and passed")
    else:
        print("Eligible but Failed")
else:
    print("Not Eligible due to Attendance")

#Bank Loan Eligibility
age=int(input("Enter your age"))
salary=60000
if age>21 and age<60:
    if salary>=50000:
        print("Loan Eligible")
    else:
        print("salary Too Low")
else:
    print("Age Criteria Not Satisfied")
    




















    
