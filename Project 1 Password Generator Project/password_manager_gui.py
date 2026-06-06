import tkinter as T 

import random
import string






def satistics_pass():

    try:

        with open("Save.txt", "r") as F:

            Data = F.read()

            L = [i for i in Data.split("\n") if i]

            No = 0
            S = 0
            W = 0
            N = 0

            for i in L:

                No += len(i)

                mark = 0

                if len(i) >= 8:
                    mark += 1

                if any(j.islower() for j in i):
                    mark += 1

                if any(j.isupper() for j in i):
                    mark += 1

                if any(j.isdigit() for j in i):
                    mark += 1

                if any(j in string.punctuation for j in i):
                    mark += 1

                if mark == 5:
                    S += 1

                elif mark >= 3:
                    N += 1

                else:
                    W += 1

            if len(L) > 0:
                A = No / len(L)

                Longest = max(len(i) for i in L)
                Smallest = min(len(i) for i in L)

            else:
                A = 0
                Longest = 0
                Smallest = 0

            return (
                f"Total Password : {len(L)}\n"
                f"Strong Password : {S}\n"
                f"Weak Password : {W}\n"
                f"Normal Password : {N}\n"
                f"Average Length : {A:.2f}\n"
                f"Longest Password Length : {Longest}\n"
                f"Smallest Password Length : {Smallest}"
            )

    except FileNotFoundError:

        return "No Saved Password Found."















def Saved_password ():

    try : 

        with open ("Save.txt" , "r") as F :
            Data = F.read ()

        if Data : 
            return Data

        else : 
            return 'No Password Save'    

    except FileNotFoundError :
        return "NO File Save yet ."            













def Check_Strength (Pass):

    

    MSG = ""
    Mark = 0 

    
    if len (Pass) >= 8 : 
        Mark = Mark + 1  

    if any(i.islower () for i in Pass) :
        Mark = Mark + 1

    if any(i.isupper () for i in Pass ) :
        Mark = Mark + 1

    if any(i.isdigit () for i in Pass ) :
        Mark = Mark + 1 

    if any(i in string.punctuation for i in Pass ) : 
        Mark = Mark + 1              
       

    if Mark == 5 :
        MSG = "Strong"

    elif Mark >= 3:
        MSG = "Normal"

    else : 
        MSG = "weak"

    return MSG         
        









def Generate_pass (Len):
   

    if Len < 8:
        return"Password length must be at least 8"
        

    Character = string.ascii_letters + string.digits + string.punctuation 


    S = True

    while S :
    
        Password = ""
    
        for i in range (Len): 
            Password = Password + random.choice(Character)

        u = 0 
        l = 0 
        d = 0 
        p = 0 

        for j in Password :

            if  j.isupper () :
                u = u + 1

            if  j.islower () :
                l = l + 1    

            if  j.isdigit () :
                d = d + 1

            if j in string.punctuation : 
                p = p + 1


        if u>1 and l>1 and d>1 and p > 1 :
            S = False 

    

    with open ("Save.txt" ,"a") as F :
        F.write (Password + "\n")

    return Password




















def Result1 () :
    Len_Pass = E.get ()

    if (Len_Pass == "") :
        R.config (text = "Plese Enter a Length ")

    else :    


        p = Generate_pass (int(Len_Pass))

        if int (Len_Pass)< 8 :
            R.config (text = p ) 

        else :
            R.config (text = "Password : "+ p ) 
            E2.delete(0, T.END)
            E2.insert(0, p)












def result2 ():

    Data = str (E2.get ())

    if (Data == "" ):
       
        R2.config (text ="Please Enter Password First . ")

    else :

        

        Result = Check_Strength (Data)

        R2.config (text ="Strength : "+ Result )











def Result3 () :

    Data = Saved_password ()
    
    if Data == 'No Password Save' or Data == "NO File Save yet .":
        R3.config (text= Data )
        R4.config (text="")

    else :
        R3.config (text = "Password History : \n\n " + Data)  
        R4.config (text="")















def Result4 () :

    Data = satistics_pass ()
    
    if Data == 'No Saved Password Found .':
        R4.config (text= Data )
        R3.config (text="")

    else :
        R4.config (text = "Password Satistics : \n\n " + str(Data))  
        R3.config (text="")









root = T.Tk()



root.title("Smart Password Manager")
root.geometry("700x650")
root.configure(bg="#e8f0fe")










Title = T.Label(
    root,
    text="SMART PASSWORD MANAGER",
    font=("Arial", 20, "bold"),
    bg="#e8f0fe"
)
Title.pack(pady=15)



label = T.Label (root , text="Enter Password Length  : ",font=("Arial", 12, "bold") , bg="#e8f0fe" )
label.pack ()

E = T.Entry (root ,  font=("Arial", 12),
    width=25 )
E.pack ()


R = T.Label (root , text= " ",
             
             font=("Consolas", 12, "bold"),
    bg="#e8f0fe",
    wraplength=600
             )
R.pack ()

B1 = T.Button (root ,
              text="Generate Password" ,
              command = Result1,
              
              width=25,
font=("Arial", 11, "bold")
              )
B1.pack(pady =5 )



L2 = T.Label (root , text = "Enter Password : ",font=("Arial", 12, "bold"),bg="#e8f0fe")
L2.pack(pady=(20, 5))

E2 = T.Entry (root ,  font=("Arial", 12),
    width=25)
E2.pack(pady = 5)

R2 = T.Label (root , text = "" ,font=("Consolas", 12, "bold"),
    bg="#e8f0fe",
    wraplength=600)
R2.pack (pady = 5)


B2 = T.Button (root,
              text = "Check Strength  ",
               command = result2 
               ,width=25,
font=("Arial", 11, "bold")
               )
B2.pack (pady= 5)






R3 = T.Label (root ,
              text = "",
               font=("Consolas", 12, "bold"),
    bg="#e8f0fe",
    wraplength=600)

R3.pack ()



B3 = T.Button (root ,
               text= "Show Password History ",
               command = Result3,
               width=25,
font=("Arial", 11, "bold")
)

B3.pack ()


Footer = T.Label(
    root,
    text="Developed by Sushil Zangade",
    font=("Arial", 9),
    bg="#e8f0fe"
)

Footer.pack(side="bottom", pady=10)






R4 = T.Label(
    root,
    text="",
    justify="left",
    anchor="w",
    font=("Consolas", 12),
    bg="#e8f0fe"
)

R4.pack ()



B4 = T.Button (root ,
               text= "Show Statistics ",
               command = Result4,
               width=25,
font=("Arial", 11, "bold"))

B4.pack ()









root.mainloop ()