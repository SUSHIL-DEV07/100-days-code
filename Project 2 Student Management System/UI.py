import tkinter as T
import json
def add_student () :
    print ("Hello")
    








def Save1 (E1 ,E2 , E3 , E4 , R) : 

    roll_no = E1.get ()
    name = E2.get ()
    age = E3.get ()
    cource = E4.get ()   

    student = {
        "rollno" : roll_no ,
        "name" : name,
        "age" : age ,
        "cource" : cource 
    }

    with open ("Student.json" , "r") as F : 
        Students = json.load (F)

    Students.append (student)

    with open ("Student.json" , "w") as F : 
        json.dump (Students , F ) 

    R.config (text = "STUDENT DATA SAVE SUCCESSFULLY")            























def ADD_BUTTON () :

    

    win = T.Toplevel (root)

    win.geometry ("400x400")
    
    T.Label (win , text = "Enter Roll No  ").pack ()
    E1 = T.Entry (win)
    E1.pack ()

    T.Label (win , text = "Enter Name  ").pack ()
    E2 = T.Entry (win)
    E2.pack ()

    T.Label (win , text = "Enter Age  ").pack ()
    E3 = T.Entry (win)
    E3.pack ()

    T.Label (win , text = "Enter Cource  ").pack ()
    E4 = T.Entry (win)
    E4.pack ()

   
    


    R = T.Label (win ,text="")
    R.pack () 

    B = T.Button (win,
              text = "SAVE",
              command = lambda: Save1(E1,E2,E3,E4,R))
    
    B.pack ()


     
    





root = T.Tk ()

root.title ("Student Management System")
root.geometry ("700x650")
root.config (bg="#e8f0fe")


B1 = T.Button (root ,
               text = "ADD STUDENT",
               command = ADD_BUTTON 
               ).pack ()


B2 = T.Button (root ,
               text = "VIEW STUDENT",
               command = ADD_BUTTON 
               ).pack () 




B3 = T.Button (root ,
               text = "SEARCH STUDENT",
               command = ADD_BUTTON 
               ).pack ()


B4 = T.Button (root ,
               text = "DELETE STUDENT",
               command = ADD_BUTTON 
               ).pack () 


B5 = T.Button (root ,
               text = "UPDATE STUDENT",
               command = ADD_BUTTON 
               ).pack () 



root.mainloop ()