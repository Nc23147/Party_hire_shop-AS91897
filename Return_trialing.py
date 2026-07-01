import tkinter as tk 
from tkinter import ttk, messagebox
from datetime import date

active_hires = [] 
#Handles when the User wants to return an item
def process_return():
    selected_name = return_dropdown.get()



    if not selected_name:
        messagebox.showerror("Input error", "No user selected for return")
        return

   

    print_to_return()

    return_to_txt()

    new_names= [hire["name"]for hire in active_hires]
    return_dropdown['values'] = new_names
    if new_names:
        return_dropdown.current(0)
    else:
        return_dropdown.set("")





#Creates the heading in the .txt file
def print_heading():
    today = date.today()
    statement = f"Hire Data ({today})"        
    heading= f"|================{ statement }================|"                

    heading_output = heading + "\n"
    heading_output += "\nName       | Item Hired | Number Hired    | Recipt Number   \n"
        
    with open("Hire_data.txt", "w") as file:
        file.write(heading_output)
        file.flush()

#Data from inputs. Stores it into a .txt
def print_to_txt(name,item_hired,items,receipt_num):
    output = f"{name:<12} | {item_hired:<12} | {items:<12} | {receipt_num:<12}|\n"
    with open("Hire_data.txt", "a")as file:
        file.write(output)
    print(output)

def print_to_return():
    today = date.today()
    statement = f"Returned item archive ({today})"        
    heading= f"|================{ statement }================|"                
    heading_output = heading + "\n"
    heading_output += "\nName       | Item Hired  |  Number Hired    | Recipt Number  |\n"
        
    with open("Return_data.txt", "w") as file:
        file.write(heading_output)
        file.flush()

def return_to_txt(active_hires):
    output_return = f"{name:<12} | {item_hired:<12} | {items:<12} | {receipt_num:<12}|\n"
    with open("Return_data.txt", "a")as file:
        file.write(output_return)
    print(output_return)


#Handles any invalid inputs in the entry fields
def submit_item():
    name= name_entry.get().strip()
    item_hired= selected_item.get()
    items = number_hired_entry.get().strip()
    receipt_num = receipt_entry.get().strip()
    
    #If the name is blank shows an error
    if not name:
        messagebox.showerror("Input Error", "Name cannot be blank")
        return

    #Handles the number of items hired
    if items == "":
        messagebox.showerror("Input Error","Number of items cannot be blank")    
        return
    
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
        return
    
    #Appending the data to a list to keep track of the hired items
    active_hires.append({
        "name":name,
        "item": item_hired,
        "quantity":items,
        "receipt" :receipt_num
    })
    return_dropdown['values']=[hire["name"]for hire in active_hires]
    return_dropdown.current(0)


    print_to_txt(name,item_hired,items,receipt_num)
    return_to_txt(active_hires)
print_heading()


    

#--------------------------------------------------------| Tkinter |----------------------------------------------------------

#Colours 
BG_Colour= "#646464"
Border_Colour= "#ededed"
FG_Colour= "#ffffff"
Txt_Colour= "#000000"


#Main window 
root=tk.Tk()
root.title("Hire Shop")
root.geometry("800x200")
root.config(background=BG_Colour)

#Gets the name from the user
lbl_age = tk.Label(root, text="Name:", borderwidth=2, relief="solid", fg="black")
lbl_age.grid(row = 0, column= 0, padx=10, pady=5, sticky="e")

name_entry = tk.Entry(root)
name_entry.grid(row = 0, column= 1, padx=10, pady=5)

#Gets the recipt number from the user 
lbl_receipt_num=tk.Label(root, text="Receipt Number:",borderwidth=2, relief="solid",fg="black")
lbl_receipt_num.grid(row = 1, column= 0, padx=10, pady=5, sticky="e")

receipt_entry = tk.Entry(root)
receipt_entry.grid(row = 1, column= 1, padx=10, pady=5)

#Dropdown for the items avalible to hire
lbl_item_hire=tk.Label(root, text="Item hired:",borderwidth=2, relief="solid",fg="black")
lbl_item_hire.grid(row = 2, column= 0, padx=10, pady=5, sticky="e")

selected_item = ttk.Combobox(root, values=["Football","Basketball","Roadcone","Pineapple pen"], state="readonly")
selected_item.grid(row = 2, column = 1, sticky="e")
selected_item.current(0)

#Number of the item hired
lbl_number = tk.Label(root, text="Number hired:",borderwidth=2, relief="solid",fg="black")
lbl_number.grid(row = 3, column= 0, padx=10, pady=5, sticky="e")

number_hired_entry = tk.Entry(root)
number_hired_entry.grid(row = 3, column= 1, padx=10, pady=5)


#Lets the user return an item
lbl_return=tk.Label(root, text="Returns",borderwidth=2, relief="solid",fg="black")
lbl_return.grid(row =0, column= 3, padx=10, pady=5, sticky="e")

return_dropdown = ttk.Combobox(root, state="readonly")
return_dropdown.grid(row=0,column=4,padx=10, pady=5)

btn_return = tk.Button(root, text = "Return", command=process_return)
btn_return.grid(row=1, column=4,padx=10,pady=5,sticky="w")



#Takes the data that the user has entered 
submit_details_button = tk.Button(root, text="Submit details", command= submit_item)
submit_details_button.grid(row=4,column=1 , columnspan= 1, pady=10)

#Ends the program
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.grid(row=4,column=0 , columnspan= 1, pady=10)







root.mainloop()