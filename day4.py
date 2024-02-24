#keys are immutable and values are mutable in dictionaries
#update in dictionary acts like extend in lists
#to convert set to dictionary, we use from keys
#sorted function takes only keys in dictionaries
#converting list to set maintains order i.e.,set() function
#set vs hashset
#dictionary vs hashset

#pangram
"""import string
flag=0
str=input()
str.lower()
str.strip()
L=list(str)
AL=list(string.ascii_lowercase)
for i in AL:
    if i in L:
        flag=1
    else:
        break
if flag==1:
    print("pangram")
else:
    print("No")"""

#pangram using sets

"""str=input()
str.lower()
S=set(str)
if len(S)==27:
    print("pangram")
else:
    print("No")"""

#pangram using dictionaries

"""Strn=input().replace(" ","")
D={}
for i in Strn:
    D[i]=1
if len(D)==26:
    print("pangram")
else:
    print("No")"""

#first repeating letter

"""strn=input()
S=set(strn)
D={}
for i in S:
    D[i]=0
for i in strn:
    D[i]+=1
for i in D:
    if D[i]==2:
        print(i)
        break
else:
    print(".")"""


#phoneBook
"""n=int(input())
D={}
for i in range(n):
    key,value=map(str,input().split(" "))
    D[key]=value
while(1):
    req=input()
    try:
        print(fD[req])
    except:
        print("Not found")"""
                
#max count of letter in lexicographical order    
"""n=int(input())
List=[]
D={}
maxi=[]
for i in range(n):
    a=input()
    List.append(a)
for i in List:
    D[i]=List.count(i)
m=max(D.values())
for i in D:
    if D[i]==m:
        maxi.append(i)
print(max(maxi),m) """

#Graph

"""N=int(input())
D={}
for i in range(N):
    K,V=input().split()
    if K in D:
       D[K].append(V)
    else:
       D[K]=[V]
req=input()
if req in D:
   print(D[req])
else:
    print("None")"""

# weighted graph


"""N=int(input())
Dic={}
lists=[]

for i in range(N):
    S,D,d=input().split()
    if S in Dic:
        Dic[S].append([D,int(d)])
    else:
        Dic[S]=[[D,int(d)]]
req=input()
if req in Dic:
    for i in range(len(Dic[req])):
        min=Dic[req][0][1]
        if Dic[req][i][1]<min:
            min=Dic[req][i][1]
            global pos
            pos=Dic[req][i][0]
    print(pos)
else:
    print("None")"""
        
    
    

    
  





























