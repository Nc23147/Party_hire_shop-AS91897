import tkinter as tk 
from tkinter import ttk, messagebox

def submit_item():
    name= name_entry.get().strip()
    item_hired = selected_item.get().strip()
    items = number_hired_entry.get().strip()
    receipt_num = receipt_entry.get().strip()
    
    #If the name is blank shows an error
    if name== "":
        messagebox.showerror("Input Error", "Name cannot be blank")
        return
    
    #Handles the number of items hired
    try:
        items = int(items)
    except ValueError:
        messagebox.showerror("Input Error", "please enter an number without a decimal")
        return
    if items < 1:
        messagebox.showerror("Input Error", "please enter an number that is more than (or equal to) 1")
        return
    elif items > 500:
        messagebox.showerror("Input Error","please enter an number that is less than 500.")
        return

    #Handles the receipt number
    if receipt_num == "":
        messagebox.showerror("Input Error",  "Receipt number cannot be empty")
        return
    try:
        receipt_num = int(float(receipt_num))
    except ValueError:
        messagebox.showerror("Input Error", "Receipt number must be a number")
    


    print(name)
    print(item_hired)    
    print(items)
    print(receipt_num)






#--------------------------------------------------------| Tkinter |----------------------------------------------------------


#Main window 
root=tk.Tk()
root.title("Hire Shop")
root.geometry("500x200")

#Gets the name from the user
tk.Label(root, text="Name:").grid(row = 0, column= 0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row = 0, column= 1, padx=10, pady=5)

#Gets the recipt number from the user 
tk.Label(root, text="Receipt Number:").grid(row = 1, column= 0, padx=10, pady=5, sticky="e")
receipt_entry = tk.Entry(root)
receipt_entry.grid(row = 1, column= 1, padx=10, pady=5)

#Dropdown for the items avalible to hire
tk.Label(root, text="Item hired:").grid(row = 2, column= 0, padx=10, pady=5, sticky="e")
selected_item = ttk.Combobox(root, values=["Football","Basketball","Roadcone","Pineapple pen"], state="readonly")
selected_item.grid(row = 2, column = 1)
selected_item.current(0)

#Number of the item hired
tk.Label(root, text="Number hired:").grid(row = 3, column= 0, padx=10, pady=5, sticky="e")
number_hired_entry = tk.Entry(root)
number_hired_entry.grid(row = 3, column= 1, padx=10, pady=5)

#Takes the data that the user has entered 
submit_details_button = tk.Button(root, text="Submit details", command= submit_item)
submit_details_button.grid(row=4,column=1 , columnspan= 1, pady=10)

#Ends the program
quit_button = tk.Button(root, text="Quit")
quit_button.grid(row=4,column=0 , columnspan= 1, pady=10)





root.mainloop()