Students =  []



choice = int (input ("Total Student : "))

for i in range (choice):
    student = {}

    student ["rollno"] = int (input ("Enter Roll no : "))
    student ["name"]  = input ("Enter Name : ")
    student ["age"] = int (input ("Enter Age : "))
    student ["cource"] = input ("Enter Cource : ")

    Students.append (student)
    
    



for i in range (len (Students)) :

    
    print ("Student " , (i + 1))
    print ("Rollno : " , Students [i]["rollno"])
    print ("Name : " , Students [i]["name"])
    print ("Age : " , Students [i]["age"])
    print ("Cource : " , Students [i]["cource"])
    print ()

print ()
print ("Search Student")
Search = int (input ("Enter a roll no : "))




for i in Students :

    if (i["rollno"] == Search ):

        print ()
        print ("Student Found ") 
        print ("Name : " , i["name"] )
        print ("Age : " , i["age"] )
        print ("Cource : " , i["cource"] )

        break 

else : 
    print ("Student Not Found . ")
    
    




print ()
print ("Deleted Student")
Search = int (input ("Enter a roll no : "))




for i in Students :

    if (i["rollno"] == Search ):

        Students.remove (i)
        print ("Student Record Delete Successfully ")

        break 

else : 
    print ("Student Not Found. ")
    
    








print ()
print ("Updated Student")
Search = int (input ("Enter a roll no : "))




for i in Students :

    if (i["rollno"] == Search ):

        i ["name"] = (input ("Enter User Updated name : "))
        i ["age"] = int (input ("Enter User Updated Age : "))
        i ["cource"] = input ("Enter User Updated couece : ")

        print ()
        print("Student Record Updated Successfully")


        break 

else : 
    print ("Student Not Found. ")
    
    
print(Students)





















