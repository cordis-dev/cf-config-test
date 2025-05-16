def match_case_test():
    car = "Patriot"
    
    match car:
        case "Focus":
            manufacturer = "Ford"
        case "Navigator":
            manufacturer = "Lincoln"
        case "Camry":
            manufacturer = "Toyota"
        case "Civic":
            manufacturer = "Honda"
        case "Patriot":
            manufacturer = "Jeep"
        case "Jetta":
            manufacturer = "VW"
        case "Ceyene":
            manufacturer = "Porsche"
        case "Outback":
            manufacturer = "Subaru"
        case "520i":
            manufacturer = "BMW"
        case "Tundra":
            manufacturer = "Nissan"
        case "Tundra2":
            manufacturer = "Nissan2"
        case "Tundra3":
            manufacturer = "Nissan3"
        case "Tundra4":
            manufacturer = "Nissan4"
        case "Tundra5":
            manufacturer = "Nissan5"
        case "Tundra6":
            manufacturer = "Nissan6"
        case _:
            manufacturer = "Unknown"
    
    return manufacturer

def if_elseif_test():
    car = "Patriot"

    if car == "Focus":
        manufacturer = "Ford"
    elif car == "Navigator":
        manufacturer = "Lincoln"
    elif car == "Camry":
        manufacturer = "Toyota"
    elif car == "Civic":
        manufacturer = "Honda"
    elif car == "Patriot":
        manufacturer = "Jeep"
    elif car == "Jetta":
        manufacturer = "VW"
    elif car == "Ceyene":
        manufacturer = "Porsche"
    elif car == "Outback":
        manufacturer = "Subaru"
    elif car == "520i":
        manufacturer = "BMW"
    elif car == "Tundra":
        manufacturer = "Nissan"
    elif car == "Tundra2":
        manufacturer = "Nissan2"
    elif car == "Tundra3":
        manufacturer = "Nissan3"
    elif car == "Tundra4":
        manufacturer = "Nissan4"
    elif car == "Tundra5":
        manufacturer = "Nissan5"
    elif car == "Tundra6":
        manufacturer = "Nissan6"        
    else:
        manufacturer = "Unknown"

    return manufacturer
