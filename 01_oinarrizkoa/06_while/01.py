prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
city_list=[]

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    
    elif city == '':
        print("You must enter a city name.")
        
    elif city in city_list:
        print(f"You have already entered {city}.")
        
    elif city == 'show':    
        print("\nHere is the list of cities you have visited:")
        for city in city_list:
            print(city)
            
    elif city == 'del':
        print("\nHere is the list of cities you have visited:")
        for city in city_list:
            print(city)
            
        del_city = input("Which city would you like to remove? ")
        if del_city in city_list:
            city_list.remove(del_city)
            print(f"{del_city} has been removed from the list.")
        else:
            print(f"{del_city} is not in the list.")
    else:
        city = city.title()
        print(f"I'd love to go to {city}!")
        city_list.append(city)
        