import tkinter as tk

def hello () :
    
    print ("Function")
    length = int(length_entry.get())
    result .config (text=length )


# Create Window 
root = tk.Tk()

root.title("Password Manager")
root.geometry ("500x300")



# Label Create 
label = tk.Label(root, text="Enter Password Length")
label.pack()


# input
length_entry = tk.Entry (root)
length_entry.pack()


result = tk.Label(root ,text=" ")
result.pack ()





# button = tk.Button (root , text= "Generated Password")

# Button connect with Function
button= tk.Button (
    root ,
    text = "Generated Password",
    command = hello
)
button.pack ()



# Read input value




 


root.mainloop ()





