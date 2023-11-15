import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
from urllib.parse import unquote
from PIL import Image
# Get the HTML content of the page
url = ("https://www.nuevaamericana.com.py/categoria/812/construccionbloque")
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
            try:
                with Image.open(image_path) as img:
                    img = img.convert("RGB")
                    img.save(image_path.replace(".jpg", ".jpeg"))
            except Exception as e:
                print(f"No se pudo convertir la imagen {image_path}: {str(e)}")
            # Convert to JPEG
    else:
        print(f"Ignorando URL no válida: {image_url}")
# mostrar un mensaje de porcentaje de descarga
print("Descarga finalizada")
