# OOP Part 2


# del keyword

class Student :

    def __init__ (self,name) :
        self.name = name 
        print ("Object is created")

S1 = Student ("Sushil")
del S1 
# print (S1.name )
        




# Public and Private  

class Account :
    
    def __init__ (self , no , pas):
        self.no = no 
        self.__pas = pas # Private

    def No (self) :
        print ("Account No : " , self.no)

    def Pas (self) :
        print ("Password : ", self.__pas)

    # def __change (self) :
    #     new = input ("Enter new pass")
    #     self.pas = new 
    #     print ("Password Change")

    def Admin (self) :
        pass
        # self.__change ()  

A1 = Account ("12345" , "ABC")

print (A1.no)
# print (A1.__pas)

A1.No ()
A1.Pas ()
# A1.__change ()
# A1.Admin () 
A1.Pas () 

# print (A1.pas)




            


# Inheritance 
# Type of Inheritance 

# Single Inheritance 

# class A : 
#     def FunA (self) :
#         print ("Class A")


# class B (A) :
#     def FunB (self) :
#         print ("Class B")        

# ob = B ()

# ob.FunA ()
# ob.FunB ()




# Multi Level


class A : 
    def FunA (self) :
        print ("Class A")


class B (A) :
    def FunB (self) :
        print ("Class B")        

class C (B) : 
    def FunC (self) :
        print ("Class C")

ob = C ()

ob.FunA ()
ob.FunB ()
ob.FunC ()





# Multiple 


# class A : 
#     def FunA (self) :
#         print ("Class A")


# class B  :
#     def FunB (self) :
#         print ("Class B")        

# class C (A,B) : 
#     def FunC (self) :
#         print ("Class C")

# ob = C ()

# ob.FunA ()
# ob.FunB ()
# ob.FunC ()









# Super Method  
class A : 

    def __init__ (self , a ,b) :
        print ("Class A Constructor")


class B (A) :

    def __init__ (self , a ,b) :
        super().__init__(a , b) # Note : not write self Parameter 
        print ("Class B Contructor " )


ob = B (10,20)





# Class Method 

class Person : 

    name = "Blank"

    # def ChangeName (self , name) : 
       
        # Method 1 
        # Person.name = name 
        
        # Method 2
        # self.__class__.name = name
     

    # Method 3     
    @classmethod 
    def ChangeName (cls , name):
        cls.name = name 
                 

ob = Person ()
ob.ChangeName ("Dhanu")
  
print (Person.name )    







# Property decorator method 

class Collage :

    def __init__ (self , S1 , S2 , S3):
        self.S1 = S1
        self.S2 = S2
        self.S3 = S3

    @property
    def Percentage (self) :
        return str((self.S1 + self.S2 + self.S3 ) / 3 ) + " % "

ob1 = Collage (90,90,90)
print (ob1.Percentage )







# Polymorphism 

# Operator Overloading 

class Poly :

    def __add__ (self, b ) :
        print ("Addition")

    def __sub__ (self, b ) :
        print ("Subtraction")

    def __mul__ (self , b ):
        print ("Multiplication")

    def __truediv__ (self , b) : 
        print ("Division")

    def __mod__ (self, b) :
        print ("Reminder")                  

    
del ob
ob = Poly ()

ob + 5 # Simgle Parameter

ob - 5

ob * 5

ob / 5

ob % 5







# Practice Question 1 
import math
class Circle :

    def __init__ (self,r) :
        self.r = r

    def Area (self) :
        self.A =  3.14 * (self.r * self.r)
        print ("Area : " , self.A)

    def Perimeter (self) :
        self.P = 2 * math.pi * self.r
        print ("Perimeter : " , self.P)


C1 = Circle (14)

C1.Area ()
C1.Perimeter ()



# Practice Quetion 2 

class Employee : 

    def __init__ (self , role , department , salary ):
        self.role = role 
        self.department = department
        self.salary = salary 

    def showDetails (self) : 
        print ("Role : " , self.role)
        print ("Department : " , self.department)
        print ("Salary : " , self.salary)

class Engineer (Employee) : 
    def __init__ (self , role , department , salary , name , age) :
        super ().__init__ (role ,department , salary)
        self.name = name 
        self.age = age 

    def showDetails (self) : 
        print ("Role : " , self.role)
        print ("Department : " , self.department)
        print ("Salary : " , self.salary)
        print ("Name : ",self.name) 
        print ("Age : " , self.age)


del ob

ob = Engineer ("DATA SCIENTIEST" ,"IT" ,10000,"ABDUL",25)
ob.showDetails ()



# Practice Quetion 3

class Order : 
    
    def __init__ (self , item , price) :
        self.item = item
        self.price = price

        
    def __gt__ (self , ob):
        if self.price > ob.price :
           
            print ("Item " , self.item , " Has High Price" )

        else : 

            print ("Item " , ob.item , " Has High Price" )


del ob1 

ob1 = Order ("Pizza" , 210)
ob2 = Order ("Cold Coffie" , 70)

ob1 > ob2 