def item_hired(item):
    if isinstance(item, str) or isinstance(item, float):
        return "please enter an integer (ie: a number which does not have a decimal part)"
    elif item < 1:
        return "please enter an integer that is more than (or equal to) 1"
    elif item > 500:
        return "please enter an integer that is less than 500."


item = input("How many items do you want to hire?")

print(item_hired(item))