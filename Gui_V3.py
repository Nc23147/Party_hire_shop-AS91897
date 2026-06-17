import tkinter as tk 
from tkinter import ttk, messagebox


#functions
def submit_item():
    name= name_entry.get().strip()
    item_hired = item_entry.get().strip()
    items = number_hired_entry.get().strip()
    if name== "":
        messagebox.showerror("Input Error", "Name cannot be blank")
        return
    #Handles what Item is hired
    if item_hired == "":
        messagebox.showerror("Input Error", "Item hired cannot be blank")
        return

    #Handles the amount of Items hired
    if isinstance(items, str) or isinstance(items, float):
        messagebox.showerror("Input Error", "please enter an integer (ie: a number which does not have a decimal part)")
        return
    elif items < 1:
        messagebox.showerror("Input Error", "please enter an integer that is more than (or equal to) 1")
        return
    elif items > 500:
        messagebox.showerror("Input Error","please enter an integer that is less than 500.")
        return

    print(name)
    print(item_hired)    
    print(items)









#Main window 
root=tk.Tk()
root.title("Party Hire Shop")
root.geometry("700x200")

#Main entry fields 
tk.Label(root, text="Name:").grid(row = 0, column= 0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row = 0, column= 1, padx=10, pady=5)

tk.Label(root, text="Recipt Number:").grid(row = 1, column= 0, padx=10, pady=5, sticky="e")
recipt_entry = tk.Entry(root)
recipt_entry.grid(row = 1, column= 1, padx=10, pady=5)

tk.Label(root, text="Item hired:").grid(row = 2, column= 0, padx=10, pady=5, sticky="e")
item_entry = tk.Entry(root)
item_entry.grid(row = 2, column= 1, padx=10, pady=5)

tk.Label(root, text="Row #").grid(row = 2, column= 3, padx=10, pady=5, sticky="e")
row_entry = tk.Entry(root)
row_entry.grid(row = 2, column= 5, padx=10, pady=5)

tk.Label(root, text="Number hired:").grid(row = 3, column= 0, padx=10, pady=5, sticky="e")
number_hired_entry = tk.Entry(root)
number_hired_entry.grid(row = 3, column= 1, padx=10, pady=5)

#Buttons
append_details_button = tk.Button(root, text="Append details")
append_details_button.grid(row=0,column=3 , columnspan= 2, pady=10, padx=10)

print_details_button = tk.Button(root, text="Print details", command= submit_item)
print_details_button.grid(row=0,column=4 , columnspan= 2, pady=10, padx=10)

quit_button = tk.Button(root, text="Quit")
quit_button.grid(row=0,column=6 , columnspan= 2, pady=10, padx=11)

delete_row_button = tk.Button(root, text= "Delete Row")
delete_row_button.grid(row= 2, column= 7,)




root.mainloop()