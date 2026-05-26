# Dict and set

# DICT 

D =  {
    1:"A",
    2:"B",
    3:"C",
    3 : "D"
}

print (D)


D1 = {
    "Subject" : ["M1" ,"M2" ,"DBMS"],
    "topic" : ("Dict","Set")
}

print ( type(D1))

# UNOrDered 
# mutable 

# Do not allow same key duplicate 


# Access 
print (D1 ["topic"])


# assine new vale 

D1 [3] = "Hellow"

print (D1)



# create empty Dict 

D1 = {}

print (type (D1))

D1 ['A'] = 10 


# Nested Dict

Student = {
    "name" : "Rahul",
    "subject" : {
        "M1" : 90,
        "M2" : 95,
        "DBMS" : 100 
    }    
}

print (Student)
print (Student ["subject"])



D =  {
    1:"A",
    2:"B",
    3:"C",
    4 : "D"
}



# methods 

print (list (D.keys()))

print (list (D.values()))

print (list(D.items ())) # Return Has Tuple

print (D.get(1))
print (D.get (199)) # Return None not error 

D.update ({5:"E",
           6 :"F",
           7: "G"})

print (D)








# Set

S = {1,2,3,4,5,4,1,2,3}

# Store unique Value 
# UNORDERED
# Set Mutable
# element immutable 

# not accept List and dict because that is Mutable 


 
# Empty set 

S1 = set()

print ( type (S1) )
print ( len (S))
print (S)




# Method 

S = {1,2,3,4}

S.add (5)
print (S)

S.remove (5)
print (S)

S.pop ()
print (S)

S.clear ()
print (S)



# Unique Method 

S1 = {1,2,3,4}
S2 = {3,4,5,6}

print (S1.union (S2))
print (S1.intersection (S2))



# Practice Questions 1 

D = {
    "table": ["A Piece of Furniture" , "List of facts amd figure"],
    "cat" : "A Small Animaal"
}

print (D)


# Practice Questions 2

Sub = {
    "Python","Java","C++","Python",
    "Javascript","Java","C++","C"
}

print ("Classroom : " , len (Sub))

# Practice Questions 3

# Sub = {}

# Sub["M1"] = int (input ("Emter Marks of M1 : "))
# Sub["M2"] = int (input ("Emter Marks of M2 : "))
# Sub["DBMS"] = int (input ("Emter Marks of DBMS : "))

# print (Sub)



# Practice Questions 4
S = {9 ,"9.0"}
S = {
    ("Float","9.0"),
    ("Int","9")
}

print (S)
