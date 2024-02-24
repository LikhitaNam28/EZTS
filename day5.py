#int(),print() are the methods of sys module,these are by default
#isdigit Vs isdecimal-isdigit checks individual digits,isdecimal checks overall number
import string

#odd index and even index in a string
#approach1
"""s=input()
print(s[1:len(s):2],end="")
print(s[0:len(s):2])"""

#approach2
"""s=input()
os=""
es=""
for i in range(len(s)):
    if i%2==1:
        os=os+s[i]
    else:
        es=es+s[i]
print(os+es)"""

#counting a character
"""s=input()
c=input()
count=0
for i in s:
    if c==i:
        count+=1
print(count)"""

#even count of a character
"""s=input()
c=input()
ec=0
for i in range(len(s)):
    if i%2==0:
        if s[i]==c:
            ec+=1
print(ec)"""

#only vowels or not
"""s=input()
s.lower()
v="aeiou"
for i in s:
    if i not in v:
        print("No")
        break
else:
    print("Yes")"""

#digits or not
#approach-1
"""s=input()
D="0123456789"
for i in s:
    if i not in D:
        print('No')
        break
else:
    print('yes')"""

#approach-2
"""s=input()
if s.isdigit():
    print("yes")
else:
    print("No")"""


#approach3
#based on alphabet
"""s=input()
D="0123456789"
c=0
for i in s:
    if i not in D:
        c+=1
if c==0:
    print("yes")
else:
    print("No")"""

#vowel count and consonant count
"""s=input()
vc=0
cc=0
s.lower()
v='aeiou'
s.lower()
for i in s:
    if i.isdigit():
        s=s.replace(i,"")
for i in s:
    if i in v:
        vc+=1
    else:
        cc+=1
print(vc,cc) """      

#approach2
"""s=input()
vc=0
cc=0
v="aeiouAEIOU"
for i in s:
    if i.isalpha():
        if i in v:
            vc=vc+1
        else:
            cc=cc+1
print(vc,cc)"""

#need to check this
"""s=input()
for i in range(len(s)):
    count=0
    for j in range(i,len(s)):
        if s[i]==s[j]:
            count+=1
    else:
        print(s[i]+str(count),end="")
        break"""

#word count,vowel count,consonant count
"""s=input()
s=s.strip()
words=list(s.split())
vc=0
cc=0
V="aeiouAEIOU"
C="bcdfghjklmnpqrstvwxyz"
for i in s:
    if i in V:
        vc+=1
    elif i in C:
        cc+=1
print(len(words),vc,cc)"""

#removing elements of first word in second word
#approach-1
"""s=input()
l=s.split()
for i in l[0]:
    for j in i:
        l[1]=l[1].replace(j,"")
print(l[1])"""

#approach-2
"""a,b=input().split()
r=""
for i in b:
    if i not in a:
        r=r+i
print(r)"""

#output based program
#approach-1
"""s,n=input().split()
n=int(n)
letter=list(string.ascii_lowercase)
for i in s:
    if i in letter:
        k=letter.index(i)
        s=s.replace(i,letter[(k+n)%26])
print(s)"""

#approach-2

"""t=int(input())
r=''
for i in range(t):
    a,b=input().split()
    b=int(b)
    for j in a:
        k=ord(j)+n
        if k>122:
            k=96+(k-122)
            r=r+chr(k)
        else:
            r=r+chr(k)

    print(r)"""

#oops example1

"""class classa:
    def factorial(self,a):
        fact=1
        for i in range(1,a+1):
          fact=fact*i
        print(fact)
ob=classa()
ob.factorial(5)"""

#oops example2
"""class a:
    def __init__(self):
        print("hello")
ob=a()"""

#oops fact
"""class classa:
    def __init__(self,n):
        self.n=n
    def factorial(self):
        fact=1
        for i in range(1,self.n+1):
          fact=fact*i
        print(fact)
ob=classa(6)
ob.factorial()"""
        

class classa:
    def __init__(self,n):
        self.n=n
    def factorial(self,n=None):
        if n==None:
            n=self.n
        if n==1:
           print(n)
        else:
           return n*self.factorial(n-1)
    def hel
ob=classa(6)
ob.factorial()



























