from datetime import date



def make_statement(statement, decoration):
    return f"{decoration * 3} {statement} {decoration * 3}"

def save_to_file(output):
    file = open("Hire_data.txt", "w")
    file.write(output)
    file.close()

def print_to_file(name, item_hired, items, receipt_num):
    today = date.today()
    heading = make_statement(f"Hire Data ({today})", "=")

    output = heading + "\n"
    output += "\nName       | Item Hired | Number Hired    | Recipt Number     | \n"
    output += f"{name:<10} | {item_hired:<10} | {items:<15} | {receipt_num:<18}|\n"
    
    save_to_file(output)
    print(output)

name= "Noah Clark"
item_hired = "Football"
items= 5
receipt_num= 2534555
print_to_file(name, item_hired, items, receipt_num)