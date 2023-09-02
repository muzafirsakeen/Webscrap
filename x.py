from selenium import webdriver
from bs4 import BeautifulSoup
import csv

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/offers-list/top-offers")

soup = BeautifulSoup(driver.page_source, "html.parser")

product_names = soup.find_all("div", class_="_3LU4EM")
product_prices = soup.find_all("div", class_="_3khuHA")

for i in range(len(product_names)):
    product_name = product_names[i].text
    product_price = product_prices[i].text

    if product_name is not None:
        product_name = product_name.text
    else:
        product_name = "The product name is not available."

    if product_price is not None:
        product_price = product_price.text
    else:
        product_price = "The product price is not available."

    with open("products.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Product Name", "Product Price"])
        writer.writerow([product_name, product_price])

driver.close()
