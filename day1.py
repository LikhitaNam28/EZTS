#largest among 2
"""a=int(input("Enter first number"))
b=int(input("Enter 2 number"))
if a>b:
    print(a)
else:
    print(b)"""


#second largest number among 3
"""a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c:
        a=0
elif b>c:
    b=0
else:
    c=0
#or we can find the largest among 3 as one value is 0 we can get the second largest easily
if a==0:
    if b>c:
        print(b)
    else:
        print(c)
elif b==0:
    if a>c:
        print(a)
    else:
        print(c)
elif c==0:
    if a>b:
        print(a)
    else:
        print(b)"""

#smallest among two

"""a=int(input("Enter first number"))
b=int(input("Enter second number"))
if a>b:
    print(b)
else:
    print(a)"""
    


#second largest among 3
'''a=int(input())
b=int(input())
c=int(input())
l=[a,b,c]
l.sort()
print(l[-2])'''

#print("a\n"*5)

#printing 1000 times
'''for i in range(1000):
    print("Hello World")'''
#small/large/equal
"""a,b=map(int,input().split(" "))
if a<b:
    print("a < b")
elif a>b:
    print("a > b")
else:
    print("a == b")"""

#Triangle validator
"""a,b,c=map(int,input().split(" "))
if a+b>c and b+c>a and a+c>b:
    print("Yes")
else:
    print("No")"""
#Divide apples
"""n,k=map(int,input().split(" "))
#print(k%n)
while(k>=n):
    k=k-n
print(k)"""

#Reverse number
"""num=int(input())
rev=0
flag=0
if num<=0:
    num=num*-1
    flag=1
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
if flag==1:
    print(-rev)
else:
    print(rev)"""

#Watermelon dividing
'''weight=int(input())
if weight==2:
    print("NO")
elif weight%2==0:
    print("YES")
else:
    print("NO")'''

#Fever
"""t=int(input())
for i in range(t):
    temp=int(input())
    if temp>98:
        print("Fever")
    else:
        print("No fever")"""

#discount
"""t=int(input())
for i in range(t):
    dis=int(input())
    print(100-dis)"""

#discount on TV

"""A=int(input())
B=int(input())
C=int(input())
D=int(input())
dis1=A*(C/100)
dis2=B*(D/100)
if (dis1>dis2):
    print("TV A")
else:
    print("TV B")"""


#discount in rupees

"""t=int(input())
for i in range(t):
    A,B,C,D=map(int,input().split(" "))
    if (A-C>B-D):
        print("second")
    elif (A-C < B-D):
        print("first")
    else:
        print("Any")"""

#candy distribution

"""N=int(input())
K=int(input())
a=N-K
pac=a%4
if pac==0:
    print(a//4)
else:
    print(a//4+1)"""

#Pizza

"""n=int(input())
slcs=int(input())
total=n*slcs
a=total%4
if a==0:
    print(total//4)
else:
    print(total//4+1)"""


#pizza while loop
n=int(input())
slcs=int(input())
total=n*slcs
count=0
while(total>0):
    total=total-4;
    count=count+1
print(count)



        


































    
