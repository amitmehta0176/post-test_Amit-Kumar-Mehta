
cities=["Delhi","Mumbai","Chennai","Kolkata","Pune","Jaipur","Surat","Bhopal"]
print("First 4 cities  :",cities[:4])
print("last  4 cities :",cities[4:])
cities.append("Hyderabad")
print("After adding one city",cities)
cities.remove("Bhopal")
print("After deleting one city :",cities)
city_tuple=tuple(cities)
print("converted to tuple :",city_tuple)