from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/kingspec-1tb-xf-series/p/0D9-000D-00153?Item=9SIB1V9HRT3089"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text = "$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)
"""with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
    
tags = doc.find_all("p")[0]


print(tags.find_all("b"))"""
