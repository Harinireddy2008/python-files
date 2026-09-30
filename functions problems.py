#GCD/HCF from 1 to 21 forward

def GCD(n1,n2):
    gcd=1
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            gcd=i
    return gcd
x=GCD(20,40)
print(x)

#or from 21 to 1 backward

def GCD(n1,n2):
    gcd=1
    for i in range(min(n1,n2),0,-1):
        if n1%i==0 and n2%i==0:
            gcd=i
            break
    return gcd
x=GCD(20,40)
print(x)

#LCM


