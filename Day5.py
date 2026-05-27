#  Loops 

i = 0
while i <= 5 :
    print ("Hellow")
    i = i + 1 

# practice Question 1
print ( "1 to 100 ")
i = 1 
while i <= 100 :
    print (i , end= "   ")
    i = i + 1

# practice Question 2
print ( "100 to 1 " ) 
i = 100 
while i >= 1 :
    print (i , end = "  ")
    i = i - 1 

# practice Question 3
# x = int ( input ("Enter a num : "))
# i = 1 
# while ( i <= 10 ):
#     print (x , " x " , i , " = ", (i*x) )
#     i = i + 1

# practice Question 4
# print ()
# i = 1 
# while ( i <= 10 ):
#     print (i* i , end=" , ")
#     i = i + 1

# practice question 5
# T = ( 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100  )

# S = int (input ("Search Element : "))

# i = 0
# while (i < 10) :
#     if (T[i] == S) :
#         print ("Element Found At : " ,i ," Index")
#     i = i + 1    






# Break OR Continue 

i = 1

while i <= 5 :
       
    if i == 4 :
        print ("Loop Break")
        i = i + 1
        break 

    if i == 2 : 
        print ("Loop Continue ")
        i = i + 1
        continue 

    print (i)    
    i = i + 1   








# For Loop 


L = [1,2,3,4,5]

for i in L : 
    print (i)

Fruit = ["Mango"  ,"banana" ,"Gauva"]

for i in Fruit : 
    print (i)
    if i == "apple" :
        print ("Break Loop")
        break 

else :
    print ("Do not break loop ")
   

# practice question 1 

# L = [ 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100]
# for i in L : 
#     print (i)
    

# practice question 2
# T = ( 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100)

# S = int ( input ("Enter a Search Element : "))

# for i in T : 

#     if i == S :
#         print ("Element Present in Tuple .")
#         break

#     print ("Finding ......")
# else :
#     print ("Element Not Present in Tuple . ")









# range function 

L = range ( 5 ) 

print (L[0])
print (L[1])
print (L[2])
print (L[3])
print (L[4])

print ()
for i in range (5) : 
    print (i )

for i in range (1 , 10 + 1) :
    print (i)    

for i in range (10 , 1 - 1 , -1) :
    print (i)



# practice Question 1 
print ()
for i in range (1, 101):
    print (i , end = " ") 

print () 
for i in range (100, 0 , -1) :
    print (i , end = " ")

print () 
# x = int (input ("Enter a Number : "))
# for i in range (1 , 11 ):
#     print (x , " x " , i , " = " , x*i) 








# Pass

for i in range (5) : # Creae Empty Loop 
    pass


# practice Question 1
n = 6
i = 1
sum = 0 
while i <= n :
    sum = sum + i
    i = i + 1
print ("SUM OF N NUMBER : ", sum)    

# practice question 2 
n = 5
fact = 1 
for i in range (1, n+1) :
    fact = fact * i
print ("Factorial of " , n , " = ", fact)    