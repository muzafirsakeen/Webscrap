import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

url = "https://www.flipkart.com/offers-list/top-offers?screen=dynamic&pk=themeViews%3DEvents-Topoffers%3ADeal-card~widgetType%3DdealCard~contentType%3Dneo"

driver.get(url)

# Wait for the page to load completely
wait = WebDriverWait(driver, 60)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

# Find all <a> tags
a_tags = driver.find_elements(By.CLASS_NAME, "_6WQwDJ")

# Extract and store the links from the href attributes
links = []

for a_tag in a_tags:
    link = a_tag.get_attribute("href")
    if link:
        links.append(link)

# Save the list of links to a CSV file
csv_filename = "websites_selenium.csv"
with open(csv_filename, "w", newline='', encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Link"])

    for link in links:
        csv_writer.writerow([link])

# Close the browser
driver.quit()
