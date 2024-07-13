import csv
import bs4
import requests

# Define the new URL and perform the request
url = "https://www.apple.com/"
data = requests.get(url)

# Create a BeautifulSoup object
soup = bs4.BeautifulSoup(data.text, 'html.parser')

# Extract the data you need
# For example, let's extract all the links on the page
links = soup.find_all('a')

# Define the filename for your CSV file
csv_filename = 'apple_links.csv'  # Update filename as needed

# Write the data to CSV
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Link Text', 'URL'])  # Write header
    for link in links:
        link_text = link.text.strip()
        link_url = link.get('href')
        # Ensure link_text and link_url are strings
        if link_url:
            csv_writer.writerow([link_text, link_url])

print(f"CSV file '{csv_filename}' has been saved.")