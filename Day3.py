# List

M1 = 87
M2 = 34
M3 = 89
M4 = 90 

Marks = [87,34,89, 90]

print (Marks)
print (type (Marks))


# index 

print ( Marks [0] )
print ( Marks [1] )


# len

print (len (Marks) )


# store diff datatype values

L = ["Sushil",86.60,210 ,True]

# list is mutable 

Str = "hellow"

# Str[0] = "X" error 

L[3] = "New"



# Slice

print ( L [0:3])
print (L[-3 : -1])



# Methods 

L1 = [1,2,3,4,5]

L1.append (6)

# L1.sort ()

# L1.sort ( reverse = True) # Return None 

# L1.reverse ()
print (L1)

S1 = ['A',"L","M","K", "B"]

S1.sort ()
S1.sort(reverse=True )
print (S1)


L1.insert (2,"New")
print (L1)

L1.remove ("New")
print (L1)

L1.pop (5)
print (L1)



# TUPLES

T = (1,2,3,4,5,2,2,2)

# Immutable 

T2 = ()
T2 = (1) # int 
T2 = (1,) 

print (type(T2))

# Slicing 

print (T[0:4])

# method 

print (T.index (2))
print (T.count (2))


# Practice Question 1 

# Movie = [
#     input ("Enter 1 Fev Movie : "),
#     input ("Enter 1 Fev Movie : "),
#     input ("Enter 1 Fev Movie : ")
# ]

# print (Movie)   



# Practice Question 2

L1 = [1,2,3,2,1]

L2 = L1.copy ()
L2 = L2.reverse ()

if L1 == L2 :
    print ("PARALLEDROME")
else :    
    print ("NOT PARALLEDROME")


# Practice Question 3

Grade = ('C','D','A','A','B','B','A')

print ("Count A : ", Grade.count ("A") )


# Practice Question 4

L = list (Grade)


L.sort ()

print (L)

