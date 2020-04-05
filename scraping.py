# Website scraping using requess and beautifulsoups4
import requests 

my_url = input("Enter the url to scrape: ")

print("Grabbing...", my_url)

response = requests.get(my_url)
print("Status is", response.status_code) #200 201 202
# if response.status_code == 200:
#     print("Go ahead and scrape")
# else:
#     print("You can't scrape this.", response.status_code)

if response.status_code != 200:
    print("You can't scrape this", response.status_code)
else:
    print("Scraping...")
    print(response.text)