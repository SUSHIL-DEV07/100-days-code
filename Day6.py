# Function  

def A () :
    print ("FUNCTION A")


A ()


def Sum (a , b ):
    c = a + b 
    print (c)

Sum (11,11) 
   

def S ( a , b ):
    return a + b

c = S (10,20)
print (c)


def printHello ():
    print ("Hello")

printHello ()
printHello ()
printHello ()
printHello ()
printHello ()

print (printHello ()) # Return None

def cavg (a ,b,c) :
    sum = a + b + c
    a = sum / 3 
    print ("Average : " , a)

cavg (10,20,30)    
    








# Type of Function 

# Buid in 
# user Defined 

# build in 

print ("Hellow" , "World" , sep = " .. " , end = "$")
print ("Next Lines |||")


print ( len ([1,2,3,4,5]))


# user Defined Function 










# Default Argument 
def Add_Two (a = 1 , b = 1) :
    print (a + b)

Add_Two (10,10)
Add_Two (10)
Add_Two (b = 10)


def fun_B (a  , b = 1 ) :
    print (a , b)

fun_B (19 , 20 )


# def fun_C (a = 1  , b  ) :  ## Error Not Possible 
#     print (a , b)

# fun_C (19 , 20 )




# Practice Question 1
def FunA ( L ):
    print ( len (L) )

FunA ([1,2,3,4,5])

# Practice Question 2
def FunB ( L ):
    print ( L )

FunB ([1,2,3,4,5])

# practice Question 3 
def Factorial ( n ) :
    
    F = 1 
    for i in range (1 , n+1 ):
        F = F * i 

    print ("FACTORIAL : " , F)

Factorial (5)     


#  practice Question 4
def FunC (USD) :
    IND = USD * 95.99
    print (USD ," USD = " , IND , " IND")

FunC (10000)







# Recursion 

def show ( n ):
    if n == 0 : # Base Case
        return  # Return Control
    print (n)
    show (n-1)
    print ("END")

show (5)


def F ( n ):
    if n == 0 or n == 1 :
        return 1 
    else :
        return n * F ( n-1 )
    

a = F (5)
print (a)


# Practice Question 1 


# Sum = 0 
# for i in range (1 , n + 1) :
#     Sum = Sum + i
# print (Sum)


def D (n) :
    
    if n == 1 : 
        
        return 1
    else : 
        return  n + D(n - 1 ) 
        

b = D (5) 
print (b)





# Practice Question 2

 
def f1 (ind , L):

    if ind  == -1 :
        return 
    print (L[ind])
    f1 (ind - 1, L)

L = [12,15,16,76,44]
f1 ( 4 , L)

print ()

def f2 ( L ,ind = 0 ):

    if ind  == len (L) :
        return 
    print (L[ind])
    f2 (L , ind + 1 )

L = [12,15,16,76,44]
f2 (  L)

    