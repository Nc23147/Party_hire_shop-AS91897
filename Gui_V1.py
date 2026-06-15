import tkinter as tk 

#Main window 
root =tk.Tk()
root.title("Party Hire Shop")
root.geometry("750x500")

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

tk.Label(root, text="Number hired:").grid(row = 3, column= 0, padx=10, pady=5, sticky="e")
number_hired_entry = tk.Entry(root)
number_hired_entry.grid(row = 3, column= 1, padx=10, pady=5)



root.mainloop()