def to_camel_case(text: str) -> str: 
    new_arr: list[str] = []

    for i, el in enumerate(text):
        if i-1 >= 0 and text[i-1] in ("-", '_'):
            new_arr.append(el.upper())
        elif el not in ("_", '-'):
            new_arr.append(el)
    
    return "".join(new_arr)

def to_camel_case_2(text: str) -> str:
    arr = text.replace("_", "-").split("-")
    return arr[0] + "".join([i.title() for i in arr[1:]]) 


assert to_camel_case_2("the-stealth-warrior") == "theStealthWarrior", to_camel_case_2("the-stealth-warrior")
assert to_camel_case_2("The_Stealth_Warrior") == "TheStealthWarrior", to_camel_case_2("The_Stealth_Warrior")
assert to_camel_case_2("The_Stealth-Warrior") == "TheStealthWarrior", to_camel_case_2("The_Stealth-Warrior")

