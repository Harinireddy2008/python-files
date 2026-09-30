'''n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end="")
    print()
n=5
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()

n=4
for i in range(0,n):
    for j in range(0,n-i-1):
        print("  ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()


n=4
for i in range(n-1,-1,-1):
    for j in range(0,n-i-1):
        print("  ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()

    
    
n=9
for i in range(3,n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()

n=9
for i in range(n-1,2,-1):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()

n=10
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()
    
n=10
for i in range(n-1,-1,-1):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()'''
n=10
for i in range(n-1,-1,-1):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,n-i):
        print("* ",end="")
    print()
