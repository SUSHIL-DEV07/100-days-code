import tkinter as T 


def fun () :
    name = E.get ()
    R.config (text = name ) 

root = T.Tk()

root.title ("Password Gwnwrator")
root.geometry ("600x600")

label = T.Label (root , text="Enter Name : " )
label.pack ()

E = T.Entry (root )
E.pack ()


R = T.Label (root , text= " ")
R.pack ()

B = T.Button (root ,
              text = "Submit" ,
              command = fun
              )
B.pack()




root.mainloop ()