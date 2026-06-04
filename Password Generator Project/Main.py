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

    with open ("Save.txt" ,"a") as F :
        F.write (Password + "\n")







def Saved_password ():

    try : 

        with open ("Save.txt" , "r") as F :
            Data = F.read ()

        if Data : 
            print (Data)

        else : 
            print ('No Password Save')    

    except FileNotFoundError :
        print ("NO File Save yet .")            








def satistics_pass () :
    try :
    
        with open ("Save.txt" , "r") as F :
        
            Data = F.read ()

            L = [i for i in Data.split("\n") if i ]

            print ()
            print ("Total Password : ",len (L))

            No = 0
            S = 0
            W = 0
            N = 0 

            for i in L : 

                No = No + len(i)
                mark = 0 

                if len(i) >= 8 :
                    mark = mark + 1

                if any(j.islower() for j in i):
                    mark = mark + 1 

                if any (j.isupper() for j in i) : 
                    mark = mark + 1  

                if any (j.isdigit() for j in i) : 
                    mark = mark + 1           

                if any (j in string.punctuation for j in i):
                    mark = mark + 1   

                if mark == 5 : 
                    S = S + 1

                elif mark >= 3 : 
                    N = N + 1

                else : 
                    W = W +1  
        
                if len (L) > 0 :
                    A = No / len(L)
        
                else :
                    A = 0   


            Longest = max (len(i) for i in L)
            Smallest = min (len (i)for i in L )


            print ("Total Strong Password : ",S)
            print ("Total weak Password : ",W)
            print ("Total Normal Password : ",N)
            print ("Average Length of all Password : ",A)
            print ("Longest Password length : " , Longest)
            print ("Smallest Password length : " , Smallest)

    except FileNotFoundError : 
        print ("No Saved Password Found .")
        return

        

           







while (True) :

    print ("===== PASSWORD MANAGER =====")
    print ()
    print ("1 Generated Password")
    print ("2 Check Password Strength ")
    print ("3 View Saved Password")
    print ("4 Satistics Passwords")
    print ("5 Exit")
    print ()

    choice = int (input ("Enter Choice : "))

    if choice == 1 :
        Generate_pass()

    elif choice == 2 : 
        Check_Strength ()

    elif choice == 3 : 
        Saved_password ()

    elif choice == 4 :
        satistics_pass()

    elif choice == 5 :
        break      

    else : 
        print ("Invalid Choice .")




            
 

