
#oops
#for recursive function we have to use helper function
#prime or not
"""class classn:
    def __init__(self,n):
        self.n=n
    def isprime(self):
        for i in range(2,self.n):
            if self.n%i==0:
                return "No"
        else:
            return "Yes"
    
ob1=classn(20)
ob2=classn(12)
print(ob1.isprime())
print(ob2.isprime())"""

#palindrome string

"""class a:
    def __init__(self,s):
        self.s=s
    def palindrome(self):
        if self.s==(self.s)[::-1]:
            print("Yes")
        else:
            print("No")
s1=a("mom")
s2=a("hello")
s1.palindrome()
s2.palindrome()"""
        

"""class a:
    def __init__(self,s):
        self.s=s
    def palindrome(self):
        
        s1=list(self.s)
        list(self.s).reverse()
        
        if s1==list(self.s):
            print("Yes")
        else:
            print("No")
s1=a("mom")
s2=a("hello")
s1.palindrome()
s2.palindrome() """


#prime and palindrome
"""class total:
    def __init__(self,n):
        self.n=n
    def palindrome(self):
        if str(self.n)==str(self.n)[::-1]:
            print("Yes")
        else:
            print("No")
    def isprime(self):
        for i in range(2,self.n):
            if self.n%i==0:
                print("No")
                break
        else:
            print("Yes")
    
ob1=total(22)
ob1.palindrome()
ob1.isprime()"""

"""class total:
    def __init__(self,n,s):
        self.n=n
    def palindrome(self):
        if self.s==(self.s)[::-1]:
            print("Yes")
        else:
            print("No")
    def isprime(self):
        for i in range(2,self.n):
            if self.n%i==0:
                print("No")
                break
        else:
            print("Yes")
    
ob1=total(22,"SAS")
ob1.isprime()
ob1.ispalindrome()"""

#Access specifiers
#public
"""class Car:
    maxspeed=0
    name=""
    def __init__(self):
        self.maxspeed=200
        self.name="Hi"
    def drive(self):
        print(self.maxspeed)
c1=Car()
c1.drive()
c1.maxspeed=10
c1.drive()"""

#private specifiers
"""class Car:
    __maxspeed=0
    name=""
    def __init__(self):
        self.__maxspeed=200
        self.name="Hi"
    def drive(self):
        print(self.__maxspeed)
c1=Car()
c1.drive()
c1.__maxspeed=10
c1.drive()"""

#instance class,instance variable,instance method

#super() function
"""class a:
    def __init__(self):
        print("parent class")
class b(a):
    def __init__(self):
        super().__init__()
        print("child class")
b1=b()"""


#single inheritance
"""class dob:
    def __init__(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y
    def display1(self):
        D={1:"January",2:"February",3:"March",4:"april",5:"may",6:"june",7:"july",8:"august",9:"september",10:"october",11:"November",12:"December"}
        print(D[self.m])
class details(dob):
    def __init__(self,name,age,d,m,y):
         self.name=name
         self.age=age
         self.d=d
         self.m=m
         self.y=y
         super().__init__(d,m,y)
    def display(self):
        print(self.name)
        print(self.age)
        print(self.d)
        print(self.m)
        print(self.y)
        
ob=details("abc",24,24,8,2001)
ob.display()
ob.display1()"""

#hierarical inheritance
#abstraction
"""from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(shape):
    def area(self,l,b):
        self.l=l
        self.b=b
        print(self.l*self.b)
class square(shape):
    def area(self,s):
        self.s=s
        print(self.s*self.s)

ob1=rectangle()
ob1.area(2,3)"""


#we can use more than one except block

#exception handling

"""try:
    c=10//0
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("Hello")"""



















        
