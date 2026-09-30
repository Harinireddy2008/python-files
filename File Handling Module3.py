#File Handling
#======read======
file=open("students.txt","r")
data=file.read()
print(data)
file.close()

#=======readline=========
file=open("students.txt","r")
data=file.readline()
print(data)
data2=file.readline()
print(data2)


file=open("students.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#=====write=====

file=open("students.txt","w")
file.write("Raju\nRavi\n")
file.write("Ramu")
file.close()
print("writing is done man")

#=======append=====

file=open("students.txt","a")
file.write("\nJyothsna\n")
file.write("Ramesh")
file.close()
print("appended done")

#=======writeline=====

file=open("students.txt","w")
students=["panduu\n","ammuu\n","pranuu\n"]
file.writelines(students)
file.close()
print("Done man")

#=======x mode=========

'''file=open("csmb2.txt",'x')
file.write("hello bro")
print("file is created")'''

#=====file properties=====

file=open("students.txt","r")
print(file.name)
print(file.mode)
print(file.closed)
file.close()
print(file.closed)

#=====task=====
file=open("marks.txt","w")
file.write("harini 97\nvarshini 92\nladdu 89\nvennela 93")
file.close()
print("writing is done man")

file=open("marks.txt","r")
data=file.read()
print(data)

#======r+=======

file=open("students.txt","r+")
data=file.read()
print(data)
file.write("\nharini")
file.close()

#=======w+====
file=open("students.txt","w+")
file.seek(0)
data=file.readable()
print(data)
file.write("\nharini")
file.close()

#=====a+======
  
file=open("students.txt","a+")
file.seek(0)
data=file.read()
print(data)
file.write("\nharini")
file.close()



#=======tell========

file=open("paragraph.txt","r")
data=file.read(15)
print(data)
x=file.tell()
print(x)
data2=file.read()
print(data2)
file.close
 
#=======seek====
file=open("paragraph.txt","r")
print(file.read(5))
file.seek(0)
print(file.read(5))
file.close()

#=======truncate====

file=open("paragraph.txt","r+")
file.truncate(5)
file.close()
                











