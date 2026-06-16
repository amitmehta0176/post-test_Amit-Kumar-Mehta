import requests
import json
 
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
 
    if response.status_code == 200:
        users = response.json()
 
        print("---- User Details ----")
        for user in users:
            print("Name  :", user["name"])
            print("Email :", user["email"])
            print("Phone :", user["phone"])
            print()
 
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)
 
        print("Total users fetched:", len(users))
        print("Data saved to users.json")
 
    else:
        print("Failed to fetch data. Status code:", response.status_code)
 
except requests.exceptions.ConnectionError:
    print("No internet connection.")
 
except requests.exceptions.Timeout:
    print("Request timed out.")
 
except Exception as e:
    print("An error occurred:", e)