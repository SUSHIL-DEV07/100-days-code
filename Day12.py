# Step 1 

import random
import string



def Check_Strength ():

    Pass = input ("Enter Password : ")

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

    print ("PASSWORD STRENGTH : ", MSG)         
        

    











def Generate_pass ():
    Len = int (input ("Enter Password Length : "))

    if Len < 8:
        print("Password length must be at least 8")
        return

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

    print ("Generated Password : ", Password )

           







while (True) :

    print ("===== PASSWORD MANAGER =====")
    print ()
    print ("1 Generated Password")
    print ("2 Check Password Strength ")
    print ("3 Exit")
    print ()

    choice = int (input ("Enter Choice : "))

    if choice == 1 :
        Generate_pass()

    elif choice == 2 : 
        Check_Strength ()

    elif choice == 3 :
        break  

    else : 
        print ("Invalid Choice .")




            
 

