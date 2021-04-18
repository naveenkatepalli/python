#tuples
t1=('saileja',5,'grrf',54)
print(t1)
#accessing
print(t1[0])
print(t1[3])
t2=t1+('basavaiah','naveen','katepalli','saileja')
print(t2)
#slicing
print(t1[0:1])
print(t1[1:4])
print(t2[0:5:2])
print(t2[::3])
#find length of tuple
print(len(t2))
#sorting the tuple
t3=('hgnfhd','rujryt','urjytfyt','jtdtyf','utu6rt','utrytjh')
print(sorted(t3))
#nested tuple
t4=('naveen',('basavaiah','saileja','katepalli'),'pavan','parvatalu','sai')
print(t4[1][2])
print(t4[3])
#lists
l1=['naveen','basavaiah','saileja','katepalli','chakkapalli','parul university']
#accessing
print(l1[5])
#slicing
print(l1[0:3])
#adding elements
print(l1+[5,6,9])
l2=['fsgs','ddsweef','rwafds',58,7]
print(l1+l2)
#changing lists
#extend
l1.extend([5,6,9])
print(l1)
#append
l1.append(l2)
print(l1)
#removing 
l1.remove(l2)
print(l1)
l1.remove(9)
print(l1)
#replacing
l1[5]='Piet'
print(l1)
#deleting the elements of list
del(l1[6])
print(l1)
#converting the string into list
z='naveen katepalli basavaiah sailaja'
xx=z.split( )
print(xx)
zz='1,2,3,4,5,6,7,8,9'
yy=zz.split(",")
print(yy)
#clonning of a list
bb=l1[:]
print(bb)
#finding the index of an element of a list
aa=l1.index('katepalli')
print(aa)
#sets
#convertion of list into set
l4=[1,2,3,4,5,6,7.8,9,'naveen']
s1=set(l4)
print(s1)
#convertion of tuple into set
l3=('d','f','h','r','w')
s3=set(l3)
print(s3)
#set operation
a={'naveen','basavaiah','saileja'}
print(a)
a.add('katepalli')
print(a)
#removing the elements
a.remove('katepalli')
print(a)
#verification of elements
ff='naveen' in a
print(ff)
#intersection of sets
vv=s1 & a
print(vv)
#union of two sets
print(s1.union(a))
#checking if set2 is subset of set1
print(s1.issubset(a))
n={'naveen','saileja'}
print(n.issubset(a))
#subtraction of sets
print(a.difference(n))
#chicking if set1 is superset of set2
print(a.issuperset(n))
#sum of elements of a set
nn={1,2,3,4,5,6,7,8,9}
print(sum(nn))
#dictionaries
thisdict={
    'brand':'nike',
    'type':'shoes',
    'color':['black','blue','red'],
    'size':9, 
    'lether':False
}
print(thisdict)
print(thisdict['lether'])#access
print(len(thisdict))#length of a dictionary

#conditions and branching
#comparission
print('naveen'=='naveen')
print(5==6)
#branching
#if statement 