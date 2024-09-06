import requests
from bs4 import BeautifulSoup

# Step 1: Specify the URL of the website you want to scrape
url = 'https://example.com'  # Replace with the URL of the site you want to scrape

# Step 2: Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Successfully retrieved the website!")
else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")
    exit()

# Step 3: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Extract the data you want
# For example, extracting the <h1> tag from the page
h1_tag = soup.find('h1')  # This finds the first <h1> tag on the page

if h1_tag:
    print("Extracted H1 tag text:", h1_tag.text)
else:
    print("No H1 tag found on the page.")

# Step 5: (Optional) Extract multiple elements, like all <p> tags
paragraphs = soup.find_all('p')  # This finds all <p> tags on the page
print("\nExtracted Paragraphs:")
for p in paragraphs:
    print(p.text)

# Step 6: Handle any further processing or saving the data
# For example, you could write the data to a file
