import requests
from bs4 import BeautifulSoup
from time import sleep
import sys

def typing_print(text, delay=0.05):
    for char in text:
        sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write('\n')

def get_star_rating(rating_class):
    rating_mapping = {
        'One': '⭐',
        'Two': '⭐⭐',
        'Three': '⭐⭐⭐',
        'Four': '⭐⭐⭐⭐',
        'Five': '⭐⭐⭐⭐⭐'
    }
    rating = rating_class.split()[-1]
    return rating_mapping.get(rating, '')

def get_books_within_budget(url, budget):
    response = requests.get(url)
    response_content = response.content
    soup = BeautifulSoup(response_content, 'html.parser')

    # Find the list of all articles (books) on the page
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')

    # Extract the title, price, and rating from each article
    books_within_budget = []
    for article in articles:
        # Find the title
        title_tag = article.find('h3').find('a')
        title = title_tag['title']
        
        # Find the price
        price_tag = article.find('p', class_='price_color')
        price_text = price_tag.text
        price = float(price_text[1:])  # Convert price from string to float (excluding the currency symbol)

        # Find the rating
        rating_tag = article.find('p', class_='star-rating')
        rating_class = rating_tag['class']
        rating = get_star_rating(rating_class[1])  # The second class contains the rating
        
        # Check if the book price is within the user's budget
        if price <= budget:
            books_within_budget.append((title, price_text, rating))

    return books_within_budget

def main():
    # Ask the user for their budget
    typing_print("What is your budget in pounds (e.g., 20.00)? ")
    budget = float(input())

    url = "https://books.toscrape.com/catalogue/page-1.html"
    books_within_budget = get_books_within_budget(url, budget)

    # Display the books within the budget
    if books_within_budget:
        typing_print(f"Books within your budget of £{budget}:")
        for title, price, rating in books_within_budget:
            typing_print(f"Title: {title}, Price: {price}, Rating: {rating}")
    else:
        typing_print(f"No books found within your budget of £{budget}.")

if __name__ == '__main__':
    main()
