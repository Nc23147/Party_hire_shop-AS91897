#--------------------------------------------------------| Tkinter |----------------------------------------------------------
import tkinter as tk
from tkinter import ttk, messagebox

#Colours 
BG_Colour= "#5768bd"
Border_colour= "#1c296b"
FG_Colour= "#1d8a88"


#Main window 
root=tk.Tk()
root.title("Hire Shop")
root.geometry("500x200")
root.config(background=BG_Colour)

#Gets the name from the user
lbl_age = tk.Label(root, text="Name:", font=("Verdana", 18, "bold"),borderwidth=2, relief="solid")
lbl_age.grid(row = 0, column= 0, padx=10, pady=5, sticky="e")
lbl_age.config(background=FG_Colour)

name_entry = tk.Entry(root)
name_entry.grid(row = 0, column= 1, padx=10, pady=5)

#Gets the recipt number from the user 
lbl_receipt_num=tk.Label(root, text="Receipt Number:",font=("Verdana", 18, "bold"),borderwidth=2, relief="solid")
lbl_receipt_num.grid(row = 1, column= 0, padx=10, pady=5, sticky="e")
lbl_receipt_num.config(background=FG_Colour)


receipt_entry = tk.Entry(root)
receipt_entry.grid(row = 1, column= 1, padx=10, pady=5)

#Dropdown for the items avalible to hire
lbl_item_hire=tk.Label(root, text="Item hired:")
lbl_item_hire.grid(row = 2, column= 0, padx=10, pady=5, sticky="e")
lbl_item_hire.config(background=FG_Colour)

selected_item = ttk.Combobox(root, values=["Football","Basketball","Roadcone","Pineapple pen"], state="readonly")
selected_item.grid(row = 2, column = 1)
selected_item.current(0)

#Number of the item hired
tk.Label(root, text="Number hired:").grid(row = 3, column= 0, padx=10, pady=5, sticky="e")
number_hired_entry = tk.Entry(root)
number_hired_entry.grid(row = 3, column= 1, padx=10, pady=5)

#Takes the data that the user has entered 
submit_details_button = tk.Button(root, text="Submit details",) #command= submit_item
submit_details_button.grid(row=4,column=1 , columnspan= 1, pady=10)

#Ends the program
quit_button = tk.Button(root, text="Quit")
quit_button.grid(row=4,column=0 , columnspan= 1, pady=10)