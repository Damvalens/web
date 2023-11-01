import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
from urllib.parse import unquote
# Get the HTML content of the page
url = ("https://www.paramountplasticos.com.br/categoria-produto/organizacao/")
response = requests.get(url)
html_content = response.content
# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")
# Find all the images on the page
images = soup.find_all("img")
# Create a directory to store the images
if not os.path.exists("images"):
    os.mkdir("images")
# Download the images
for image in images:
    image_url = image.get("src")
    if image_url.startswith("http://") or image_url.startswith("https://"):
        image_name = unquote(os.path.basename(urlparse(image_url).path))  # Decode URL-encoded characters

        image_path = os.path.join("images", image_name)
        response = requests.get(image_url)
        with open(image_path, "wb") as f:
            f.write(response.content)
    else:
        print(f"Ignorando URL no válida: {image_url}")
print("Descarga finalizada")
