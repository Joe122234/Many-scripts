from bs4 import BeautifulSoup
import requests
import random

# Fetch the webpage content
url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

# Extract the table body containing the cryptocurrency information
tbody = doc.tbody
trs = tbody.contents

# Greet the user and ask if they want to see the top cryptocurrencies
ask = input("Welcome to Henry's Crypto Shop! Do you want to see the top crypto today? (y/n): ").lower()

if ask == "y":
    for index, tr in enumerate(trs[:10], start=1):
        name, price = tr.contents[2:4]
        print(f"Top {index}: {name.p.string}")
else:
    print("Well, if you need anything don't be shy to ask! 👍")
    quit()

# Ask if the user wants to see the prices as well
user_input = input("Do you want to see the prices of that too? (y/n): ").lower()
if user_input == "y":
    for index, tr in enumerate(trs[:10], start=1):
        tds = tr.find_all('td')
        name_tag = tds[2].find("p")
        price_tag = tds[3].find("span")
        
        if name_tag:
            name = name_tag.string.strip()
        else:
            name = "N/A"

        if price_tag:
            price_value = price_tag.string.strip()
        else:
            price_value = "N/A"
        
        print(f"Top {index}: {name}, Price: {price_value}")

# Ask if the user wants to see the volume percentage as well
user_input2 = input("Do you want to see its volume too? (y/n): ").lower()
if user_input2 == "y":
    for index, tr in enumerate(trs[:10], start=1):
        tds = tr.find_all('td')
        name_tag = tds[2].find("p")
        volume_percent_tag = tds[4].find("span")  # Adjust class name as needed
        
        if name_tag:
            name = name_tag.string.strip()
        else:
            name = "N/A"

        if volume_percent_tag:
            volume_percent = volume_percent_tag.text.strip()
        else:
            volume_percent = "N/A"
        
        print(f"Top {index}: {name}, Volume Percentage: {volume_percent}")


tips = [
    "Do Your Research (DYOR): Understand the fundamentals of the cryptocurrency you're interested in. Read whitepapers, follow the project's developments, and stay informed about the team behind it.",
    "Diversify Your Portfolio: Avoid putting all your funds into one cryptocurrency. Diversifying helps spread risk across different assets.",
    "Be Wary of Scams: The crypto space is rife with scams and fraudulent schemes. Be cautious of offers that seem too good to be true and always verify sources.",
    "Consider Long-Term Holding (HODL): For many investors, holding onto cryptocurrencies for the long term can be more profitable than frequent trading. This approach reduces the impact of short-term market volatility.",
    "Educate Yourself Continuously: The crypto market evolves quickly. Continuously educate yourself about new developments, trends, and technologies in the space to make informed decisions."
]

print(f"Here's a free tip for you when you invest in crypto💸: {random.choice(tips)}")
print("Thank you for checking the crypto details today! Have a great day! 😊")