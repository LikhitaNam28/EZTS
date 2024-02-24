#sum takes only one argument

#python follows pass by reference

#factorial of a number
"""fact=1
n=int(input())
for i in range(n,1,-1):
    fact=fact*i
print(fact)"""



#Sugarcane
"""t=int(input())
def prof(M):
        N=M*50
        spending=N*0.2+N*0.2+N*0.3
        profit=N-spending
        return int(profit)
def test(t):
    if (t>0):
        k=int(input())
        print(prof(k))
    else:
        return
    test(t-1)
test(t)"""


#2X
"""t=int(input())
for i in range(t):
    X,Y=map(int,input().split(" "))
    movie_time(X,Y)
def movie_time(X,Y):
  print(X-(Y//2))"""


#lucky four
"""T=int(input())
def cont(a):
    count=0
    while(a>0):
        num=a%10
        if num==4:
            count+=1
        a=a//10
    return count
def test(T):
    if T>0:
        L=int(input())
        print(cont(L))
    else:
        return
    test(T-1)
test(T)"""

#factorial
"""n=int(input())
fact=1
while(n>0):
    fact=fact*n
    n-=1
print(fact)"""


#fact with recursion
"""n=int(input())
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))"""


#next even number
"""n=int(input())
if n%2==0:
    print(n+2)
else:
    print(n+1)"""

#append three
"""n=int(input())
num=n
count=0
while(n>0):
    rem=n%10
    count+=1
    n=n//10
req=3*pow(10,count)+num
print(req*10+3)"""
#for appending a number at the last we have to multiply the number with 10 and the we have to add the number

#Append 3 using reverse function
"""N=int(input())
def rev(N):
    revs=0
    while(N>0):
        rem=N%10
        revs=revs*10+rem
        N=N//10
    return revs
req=N*10+3
K=rev(req)
K=K*10+3
print(rev(K))"""





    




























