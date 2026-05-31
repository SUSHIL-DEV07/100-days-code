# # OOP IN PYTHON 

# # Class 

# class Student : 

#     name = "Sushil"


# S1 = Student () 

# print (S1.name)

# S2 = Student ()

# print (S2.name )


# class Car :

#     color = "blue"
#     brand = "Bmw"

# C1 = Car ()
# print (C1.color)







# # Constructor 

# class A : 
#     def __init__ (self) :
#         print ("CONSTRUCTOR CALL")
#         print (self)

# A1 = A ()
# A2 = A ()        



# class Stud :

#     def __init__ (self) :
#         print ("Default")

#     def __init__ (self , name ) :
#         self.name = name
#         print ("Parameterized Constructor") 

# Ramesh = Stud ("Ramesh")
# print (Ramesh.name)

# Suresh = Stud ("Suresh")








# cLASS AND Object Attribute

class Collage :

    Clg_Name = "ABC Collage"
    name = "Anomeous"

    def __init__ (self , name , mark) :
        self.name = name
        self.mark = mark

S1 = Collage ("Sushil" ,"210")
print (S1.name)
print (S1.mark)
print (S1.Clg_Name)

S2 = Collage ("Suresh" , "207")
S2.Clg_Name = "GCOEJ"
print (S2.name)
print (S2.mark)
print (S2.Clg_Name)

print (Collage.name)





# Method 

class Car : 

    def Start (self) :
        print ("Car Start")

    def Stop (self) :
        print ("Car Stop")

C1 = Car ()
C1.Start ()
C1.Stop ()





# Practice Question 1 
class Student :

    def __init__ (self , name , s1 ,s2 ,s3) :
        self.name = name 
        self.s1 = s1 
        self.s2 = s2
        self.s3 = s3

    def mark_Avg (self) :
        self.Total = (self.s1 + self.s2 + self.s3 )
        self.Average = self.Total / 3 
        print ("Average Marks : ", self.Average)

S1 = Student ( "Sushil" , 90 , 91 , 94 )    
S1.mark_Avg ()           





# Ststic method 

class A : 

    @staticmethod 
    def hello () :
        print ("Hellow world" )

ob = A ()
ob.hello ()       







# Practice Question 2

class Account : 

    def __init__ (self , bal ) :
        self.bal = bal 

    def credit (self) :
        C = int (input ("Enter Amount For Credit : "))
        self.bal = self.bal + C

    def debit (self) :
        D = int (input ("Enter Debit Amount : "))

        if self.bal < D : 
            print ("Not Enough Cash")
        else :     
            self.bal = self.bal - D 

    def check_bal (self) :
        print ("Balance : " , self.bal) 


A1 = Account (10000)

A1.credit ()
A1.check_bal ()

A1.debit ()
A1.check_bal ()
