import tkinter as T



def ADD_BUTTON () :

    win = T.Toplevel (root)
    
   
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



root = T.Tk ()

root.title ("Student Management System")
root.geometry ("700x650")
root.config (bg="#e8f0fe")


B1 = T.Button (root ,
               text = "ADD STUDENT",
               command = ADD_BUTTON 
               ).pack () 



root.mainloop ()