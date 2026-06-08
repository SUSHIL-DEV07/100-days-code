import json

Students =[ {
    "roll_no" : 1 ,
    "name" : "Sushil" ,
    "Age" : 20 ,
    "cource" : "CSE" 
}
]

with open ("Student.json" , "w" ) as F :
    json.dump (Students,F)




Students =[ {
    "roll_no" : 2 ,
    "name" : "Sushil" ,
    "Age" : 20 ,
    "cource" : "CSE" 
}
]


with open ("Student.json" , "w" ) as F :
    json.dump (Students,F)



with open ("Student.json","r") as F :
    Data = json.load (F)
    
print (Data)

