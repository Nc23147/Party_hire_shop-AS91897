    

def number_hired(items_input):
    try:
        if isinstance(items_input,float)or (isinstance(items_input, str) and "." in items_input):
            raise ValueError
        
        
        items = int(items_input)
    except ValueError:
        return"please enter an integer (ie: a number which does not have a decimal part)"
        
    if items < 1:
        return "please enter an integer that is more than (or equal to) 1"
    elif items > 500:
        return"please enter an integer that is less than 500."
    return"thank you"


if __name__ == "__main__":
    items_input = input("Please enter the amount of items you want to hire (Cannot be more than 500): ")
    print(number_hired(items_input))