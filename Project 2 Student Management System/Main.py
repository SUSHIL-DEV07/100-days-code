import json



def add_student ():

    with open ("Students.json" , "r") as F :
        Students = json.load (F)
        

    student = {}


    while True:

        rollno = int (input ("Enter Roll no : "))

        if rollno <= 0 :
            print ("Rollno Must be Positive ") 
            continue   

        if  any(i["rollno"] == rollno for i in Students) :
            print ("this roll no Already exist")

        else :
            student["rollno"] = rollno
            break    

    student ["name"]  = input ("Enter Name : ")
    student ["age"] = int (input ("Enter Age : "))
    student ["cource"] = input ("Enter Cource : ")

    Students.append (student)
    print ("Student Added Successfully ")

    with open ("Students.json" , "w") as F : 
        json.dump(Students , F)


















def view_student() :

    with open ("Students.json","r") as F :
        Students = json.load (F)

    if len (Students) == 0 : 
        print ("No Student Record Present ..")

    else :

        for i in range (len (Students)) :


            print ("Student " , (i + 1))
            print ("Rollno : " , Students [i]["rollno"])
            print ("Name : " , Students [i]["name"])
            print ("Age : " , Students [i]["age"])
            print ("Cource : " , Students [i]["cource"])
            print ()










def search_student () :


    with open ("Students.json" ,"r") as F :
        Students = json.load (F)
        
    print ()
    print ("Search Student")
    Search = int (input ("Enter a roll no : "))




    for i in Students :

        if (i["rollno"] == Search ):

            print ()
            print ("Student Found ") 
            print ()
            print ("Name : " , i["name"] )
            print ("Age : " , i["age"] )
            print ("Cource : " , i["cource"] )

            with open ("Students.json" , "w") as F :
                json.dump (Students , F)

            break 

    else : 
        print ("Student Not Found . ")









def delete_student () :

    with open ("Students.json","r") as F :
        Students = json.load (F)

    print ()
    print ("Deleted Student")
    Search = int (input ("Enter a roll no : "))




    for i in Students :

        if (i["rollno"] == Search ):

            Students.remove (i)
            print ("Student Record Delete Successfully ")

            with open ("Students.json" , "w") as F :
                json.dump (Students , F)
            break 

    else : 
        print ("Student Not Found. ")















def update_student ():

    with open ("Students.json" ,"r") as F : 
        Students = json.load (F)

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

            with open ("Students.json" , "w") as F :
                json.dump (Students , F)
            break 

    else : 
        print ("Student Not Found. ")
    








while (True) :
    print ("============STUDENT MANAGEMENT SYSTEM=============")
    print ()
    print ("1 Add Student")
    print ("2 View Student Information")
    print ("3 Search Student")
    print ("4 Delete Student ")
    print ("5 Update Student ")
    print ("6 Exit")
    print ()

    choice = int (input ("Enter Choice : " ))
    print ()

    if choice == 1 :
        add_student ()

    elif choice == 2 :
        view_student ()

    elif choice == 3 :
        search_student ()

    elif choice == 4 : 
        delete_student ()

    elif choice == 5 :
        update_student () 

    elif choice == 6 : 
        break

    else : 
        print ("Invalid Input ..")
        print ()

print ("Thank You For Using Our System ")


