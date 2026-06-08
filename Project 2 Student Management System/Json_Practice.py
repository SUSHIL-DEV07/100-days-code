import json 

with open ("S.json" ,"w") as F :
    pass

F = open ("S.json" , "r") 
Data = json.load (F)
print (Data)
F.close ()

Data .append ({
    "roll_no" : 2 ,
    "name" : "Sushil" ,
    "Age" : 20 ,
    "cource" : "CSE" 
})


F = open ("S.json" , "w") 
json.dump (Data,F)
F.close ()
