import tkinter as T 

import random
import string





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

        if len (Len_Pass)< 8 :
            R.config (text = p ) 

        else :
            R.config (text = "Password : "+ p ) 













def result2 ():

    Data = str (E2.get ())

    if (Data == "" ):
       
        R2.config (text ="Please Enter Password First . ")

    else :

        

        Result = Check_Strength (Data)

        R2.config (text ="Strength : "+ Result )















root = T.Tk()

root.title ("Password Generator")
root.geometry ("600x600")

label = T.Label (root , text="Enter Password Length  : " )
label.pack ()

E = T.Entry (root )
E.pack ()


R = T.Label (root , text= " ",
             font= ("Arial",14),
             wraplength=500
             )
R.pack ()

B1 = T.Button (root ,
              text = "Submit" ,
              command = Result1
              )
B1.pack()



L2 = T.Label (root , text = "Enter Password : ")
L2.pack ()

E2 = T.Entry (root)
E2.pack()

R2 = T.Label (root , text = "")
R2.pack ()


B2 = T.Button (root,
              text = "Check Strength  ",
               command = result2 
               )
B2.pack ()







root.mainloop ()