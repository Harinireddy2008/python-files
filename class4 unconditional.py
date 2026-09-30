#break
'''for i in range(0,10):
    break
    print(i)

for i in range(0,10):
    if i==5:
        break
    print(i)

#continue
    
for i in range(0,10):
    if i==5:
        continue
    print(i)

for i in range(0,10):
    if i%2==0:
        continue
    print(i)

#pass
for i in  range(0,10):
    pass

#list

#ordered
a=(1,2,3)
print(a)

a=[1,2,3,4,5,6,7,8,9,10]
print(a[0:5])
print(a[2:8])
print(a[-1:-5:-1])
print(a[-1:-5])
print(a[::-1])
print(a[::])
print(a[5:9])
print(a[-2:-7:-1])
print(a[0:9])
print(a[-4:-8:-1])
print(a[3:7])
print(a[-3:-9:-1])
print(a[0:4])
print(a[2:7])

a=[1,2,3,4,5,6,7,8,9,10]
b=[12,13,14]
a.append(11)
print(a)
a.insert(2,22)
print(a)
a.pop(5)
print(a)
a.pop()
print(a.count(2))
a.sort()
print(a)
print(len(a))
a.reverse()
print(a)

# Nested lists

a=[
   ["ravi",25,85],
   ["raju",26,89]
]
print(a[1][0])
a.append(["kumar",24,88])
b=[2,3,4]
c=[5,6,7]
print(b+c)
print(b*2)
print(2 in b)

#tuples

a=(1,2,3,4)
print(a)
print(type(a))

a=(1,2,3,1,1)
print(a.count(1))
print(a.index(1))

a=[1,2,3,4,0,12,5,6]
a.sort()
print(a)


a=[1,2,3,4,0,12,5,6]
#a.sort()
sorted(a)
print(a)

a=(1,2,3,4,0,12,5,6)
#a.sort()
b=sorted(a)
print(a)
print(b)
print(a.count(1))
print(a.index(5))


#sets

a={1,2,3,4,5,6,1,1,2,3,12}
print(a)


#Method of sets
a={1,2,3,4,5,6,1,1,2,3,12}
a.add(17)
a.update([16,22])
a.update([89,98])
a.discard(77)
a.remove(77)
a.pop()
a.clear()
         

a={1,2,3,4}
b={3,4,5,6}
print(a.union(b))
print(a|b)
print(a.intersection(b))
print(a&b)
print(a.difference(b))
print(a-b)
print(a.symmetric_difference(b))
print(a^b)
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))


a=10
b=20
c=a
a=b
b=c
print(a)
print(b)

#this process only works in python
#or 

a=10
b=20
a,b=b,a
print(a)
print(b)

#or
a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b)

#or
a=5
b=2
a=a*b
b=a//b
a=a//b
print(a)
print(b)

#frozenset

a={1,2,3,4,5}
b=frozenset(a)
print(a)
print(b)
c=frozenset({4,5,6,7,8})
print(b.union(c))
print(b.intersection(c))
print(b.issubset(c))

#Dictionary

student={
    "name":"ravi",
    "age":25,
    "marks":25,
    "city":"hyderabad",
    "ispassed":True,
    2:"Raju",
    True:4,
    3.14:"pi",
    "percentage":65.6,
    "subjectmarks":[45,44,65,76]
}
print(student)

 #adding the element
student={
    "name":"Ravi",
    "age":20
}
student["city"]="Hyderabad"
print(student)

#get

student={
    "name":"ravi",
    "age":25,
    "marks":25,
}
#print(student["city"])
print(student.get("city"))'''

student={
    "name":"Ravi",
    "age":25,
    "marks":25,
    "city":"Hyderbad",
    "ispassed":True
}
print(student.get("name"))
student.update({
    "percentage":65,
    "grade":"D"
})
print(student.pop("ispassed"))
print(student)
print(student.popitem())
print(student)
print(student.keys())
print(student.values())
print(student.items())

dulicatestudent=student.copy()
print(dulicatestudent)

