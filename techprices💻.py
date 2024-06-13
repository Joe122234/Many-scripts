from bs4 import BeautifulSoup
import requests
import re

def get_total_pages(doc):
    try:
        page_text = doc.find(class_="list-tool-pagination-text").strong
        return int(str(page_text).split("/")[-2].split(">")[-1][:-1])
    except AttributeError:
        return 1  # Default to 1 if pagination is not found

def fetch_page(url):
    page = requests.get(url).text
    return BeautifulSoup(page, "html.parser")

def extract_items(doc, search_term):
    items_found = {}
    item_containers = doc.select(".item-container")

    for container in item_containers:
        item = container.find(text=re.compile(search_term, re.I))
        if item:
            parent = item.parent
            if parent.name == "a":
                link = parent['href']
                try:
                    price = container.find(class_="price-current").find("strong").string
                    items_found[item] = {"price": int(price.replace(",", "")), "link": link}
                except AttributeError:
                    pass

    return items_found

def main():
    search_term = input("What product do you want to search for? ")
    url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"

    doc = fetch_page(url)
    total_pages = get_total_pages(doc)

    items_found = {}

    for page in range(1, total_pages + 1):
        url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
        doc = fetch_page(url)
        items_found.update(extract_items(doc, search_term))

    sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

    for item in sorted_items:
        print(item[0])
        print(f"${item[1]['price']}")
        print(item[1]['link'])
        print("-------------------------------")

if __name__ == "__main__":
    main()
