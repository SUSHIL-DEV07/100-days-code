# Sting 
S1 = "S1"
S2 = 'S2'
S3 = '''Hellow "Urope "world'''
S4 = """S4"""

print (S3)


S2 = "SENTANCE 1 \n Sentence 2 \n Sentence 3"
S3 = "SENTANCE 1 \t Sentence 2 \t Sentence 3"
print (S3)


# Operations

S1 = "Hellow"
S2 = "World"

print (S1 + S2)

print ( len ( S1 ) )

# String is iMutable 

S1 = "string"

print (S1)
print (S1 [0:6])
print (S1 [0:])
print (S1[:6])
print (S1[:])
print (S1[::-1])

print (S1 [-6: -1])


print (S1.endswith ("ing"))

print (S1.capitalize ()) # not change in original String 
S1 = S1. capitalize ()

print (S1.replace ("String" , "Array"))
print (S1.replace ("i" , "AAA"))

print (S1.find ("i"))

S2 = "I  Learn am Learn PythonLearn"
print (S2.count ("n"))



# prcatice Question 1 

# name = input ("Enter Name : ")
# print ("Length : ",len (name))

# practice Question 2 

A = "I $ Have Salary In $ in USA $$ "
print ( A.count ("$"))







# Conditional Statement 

Age = 16

if Age >= 100 : 
    print ("Not Vote")

elif (Age >= 18):
    print ("Vote ")

else : 
    print ("Not Vote")    



# Light = input ("Enter Color : ")

# if Light == "red" :
#     print ("Stop") 

# elif Light == "yellow" :
#     print ("Slow Down")

# elif Light == "green"  :  
#     print ("GO")  

# else :
#     print ("Light is broken")



Marks = 99

if Marks > 100 : 
    print ("Not Possible") 

elif Marks >= 90 :
    print ("Grade A")

elif Marks >= 80 :
    print ("Grade B")

elif Marks >= 70 :
    print ("Grsde C")

elif Marks > 50 :
    print ("Grade D")

else :
    print ("Fail")





Age = 17

if Age >= 18 : 
    
    L = bool ( input ("do you have licence : "))
    if L == True :
        print ("Drive")
    else :
        print ("Can Not Drive ")

else :
    print ("not Drive")



# Practice Question 1 
a = 55

if a % 2 == 0 :
    print ("Even")
else : 
    print ("Odd")


# practice Question 2 
num1 = 10
num2 = 50
num3 = 100

if num1 > num2 and num1 > num3 :
    print (num1 , " Greater than other Numbers ")

elif num2 > num1 and num2 > num3 : 
    print (num2 , " Greater then other Numbers ")

else :
    print (num3 , " Greater Then Other numbers ")    


# practice Question 3
    
num = int ( input ( "Enter Num : " ))

if num % 7 == 0 :
    print ("Number Devided by Seven")
else : 
    print ("Number Not devided by Seven")