from bs4 import BeautifulSoup
 
print("\n---- Scraping Quotes ----")
 
all_quotes = []
 
try:
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
 
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")
 
        for q in quotes:
            text   = q.find("span", class_="text").get_text()
            author = q.find("small", class_="author").get_text()
            all_quotes.append({"quote": text, "author": author})
 
        print("---- Quotes by Albert Einstein ----")
        for item in all_quotes:
            if item["author"] == "Albert Einstein":
                print(item["quote"])
                print()
 
        with open("quotes.json", "w") as f:
            json.dump(all_quotes, f, indent=4)
 
        print("Total quotes scraped:", len(all_quotes))
        print("Data saved to quotes.json")
 
    else:
        print("Failed to fetch page. Status code:", response.status_code)
 
except requests.exceptions.ConnectionError:
    print("No internet connection.")
 
except Exception as e:
    print("An error occurred:", e)