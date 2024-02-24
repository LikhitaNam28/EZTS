#positive indexing-left to right
#negative indexing-right to left
"""Traversing a list can be done in 3 ways
1.indexing
2.slicing
3.using loops"""

"""a=input().split()
3 4
a
['3', '4'] """

#insert method takes more time compared to other methods in lists

#after clear also some memory will be allocated for that,this is the difference between del and clear

#sort is a method and sorted is a function

#for using method we have to use dot(.),but no need in function

#only we can access elements using slicing,no deletion
#edge cases


#Duplicate elements
"""N=int(input())
L=list(map(int,input().split(" ")))[:n]
for i in L:
    count=0
    for j in L:
        if j==i:
            count+=1
            if count>=2:
                print(i)
                break
    break"""


"""a=[1,2,2,3,4]
for i in range(len(a)):
    if a[i]==a[i+1]:
        print(a[i])
        break"""

"""N=int(input())
L=list(map(int,input().split(" ")))[:N]
for i in L:
    if L.count(i)<2:
         print(i,end=" ")"""


#codechef team selecting based on divisors

"""T=int(input())
for i in range(T):
    N=int(input())
    L=[]
    for i in range(1,N+1):
        if N%i==0:
            L.append(i)
    if len(L)%2==0:
        
        T1=[i for i in L if i%2==0]
        T2=[i for i in L if i%2!=0]
        if len(T1)==len(T2):
            print(1)
        else:
            print(0)
    else:
        print(0)"""
#above code using recursion
"""N=int(input())
def test(N):
    if (N>0):
        dividing_team()
        test(N-1)
    else:
        return"""

#chef freshness in groceries

"""T=int(input())
for i in range(T):
    N,X=map(int,input().split(" "))
    A=list(map(int,input().split(" ")))
    B=list(map(int,input().split(" ")))
    cost=0
    for i in range(N):
        if A[i]>=X:
            cost=cost+B[i]
    print(cost)    """

#prime number or not

"""N=int(input())
factors=[]
for i in range(1,N+1):
    if N%i==0:
        factors.append(i)
if len(factors)==2:
    print("Prime")
else:
    print("Not prime")"""



"""N=int(input())
count=0
for i in range(1,N+1):
    if N%i==0:
        count=count+1
if count==2:
    print("prime")
else:
    print("Not prime")"""
    
#Alice Bob running            
"""N=int(input())
AH=0
BH=0
count=0
A=list(map(int,input().split(" ")))
B=list(map(int,input().split(" ")))
for i in range(N):
    if B[i]>2*A[i]:
        BH+=1
    elif A[i]>2*B[i]:
        AH+=1
    else:
        count+=1
print(count)"""


#even perfect Number
"""n=int(input())
perf=[]
for i in range(1,n+1):
    factors=[]
    for j in range(1,i):
        if i%j==0:
            factors.append(j)
    if sum(factors)==i:
        perf.append(i)
for i in perf:
    if i%2==0:
        print(i)"""
        










    























    
