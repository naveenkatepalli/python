n=bool(1)
print(n)
a=654+432
b=5432*567
c=544/23
d=544//23
print(a)
print(b)
print(c,d)
#string operations
name='katepalli naveen'
print(name[0:11])
print(name[::2])
print(name[0:13:3])
#funtion to find the length of string
print(len(name))
first_name=name+" katepalli"
print(first_name)
#repitition function
f=3*" naveen"
s=5*name
print(f,s)
#to give tab space between words
print("naveen\tkatepalli")
#print a backward slash
print("naveen\\katepalli")
print(r"naveen\katepalli")
#string methods
#upper
A="naveen katepalli"
B=A.upper()
print(B)
#replace
C=A.replace("naveen","basavaiah")
print(C)
#find
D=A.find("pa")
print(D)
#slicing of string
x='basavaiah'
print(x[0:4])
print(x[2:5])
print(x[0:10])
print(x[-5:-1])