import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import zipfile

# Settings
url = 'https://www.google.com/search?q=sad+people&sca_esv=176d6bad4133e5b3&udm=2&biw=1707&bih=775&sxsrf=AE3TifOXTogJRrCohc7TmUr8HaGSY03hmQ%3A1749299411801&ei=0zBEaIrQMJWchbIPx-T9kAk&ved=0ahUKEwjKha-QqN-NAxUVTkEAHUdyH5IQ4dUDCBE&uact=5&oq=sad+people&gs_lp=EgNpbWciCnNhZCBwZW9wbGUyBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHkiWLFDvFVj0JHACeACQAQCYAfQGoAHoDaoBCTItMS4yLjYtMbgBA8gBAPgBAZgCBaAC1AfCAgcQIxgnGMkCwgINEAAYgAQYsQMYQxiKBZgDAIgGAZIHBzIuMC4xLjKgB-MXsgcFMi0xLjK4B6gHwgcFMy00LjHIB0w&sclient=img'  # Replace with the target page
folder = 'downloaded_images'
os.makedirs(folder, exist_ok=True)

# Get page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find and download all images
images = soup.find_all('img')
for i, img in enumerate(images):
    img_url = urljoin(url, img.get('src'))
    img_data = requests.get(img_url).content
    img_name = os.path.join(folder, f'image_{i}.jpg')
    with open(img_name, 'wb') as f:
        f.write(img_data)
    print(f'Downloaded: {img_name}')

# Zip them
zip_name = folder + '.zip'
with zipfile.ZipFile(zip_name, 'w') as zipf:
    for img_file in os.listdir(folder):
        zipf.write(os.path.join(folder, img_file), arcname=img_file)

print(f'All images downloaded and zipped as {zip_name}')


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import mimetypes
import zipfile

# === Paramètres ===
target_url = 'https://www.google.com/search?q=sad+people&sca_esv=176d6bad4133e5b3&udm=2&biw=1707&bih=775&sxsrf=AE3TifOXTogJRrCohc7TmUr8HaGSY03hmQ%3A1749299411801&ei=0zBEaIrQMJWchbIPx-T9kAk&ved=0ahUKEwjKha-QqN-NAxUVTkEAHUdyH5IQ4dUDCBE&uact=5&oq=sad+people&gs_lp=EgNpbWciCnNhZCBwZW9wbGUyBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHkiWLFDvFVj0JHACeACQAQCYAfQGoAHoDaoBCTItMS4yLjYtMbgBA8gBAPgBAZgCBaAC1AfCAgcQIxgnGMkCwgINEAAYgAQYsQMYQxiKBZgDAIgGAZIHBzIuMC4xLjKgB-MXsgcFMi0xLjK4B6gHwgcFMy00LjHIB0w&sclient=img'  # 🔁 Remplace par l’URL que tu veux scraper
output_dir = 'images_downloaded'

# === Préparer le dossier de sortie ===
os.makedirs(output_dir, exist_ok=True)

# === Télécharger la page ===
headers = {
    'User-Agent': 'Mozilla/5.0'
}
response = requests.get(target_url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# === Extraire toutes les balises <img> ===
img_tags = soup.find_all('img')
downloaded_count = 0

print(f"[+] {len(img_tags)} images trouvées. Téléchargement en cours...")

for i, img in enumerate(img_tags):
    img_src = img.get('src') or img.get('data-src') or ''
    if not img_src:
        continue

    # Construire une URL complète
    img_url = urljoin(target_url, img_src)

    try:
        img_response = requests.get(img_url, headers=headers, timeout=10)
        if img_response.status_code == 200:
            # Déduire l’extension du format MIME
            content_type = img_response.headers.get('Content-Type', '')
            ext = mimetypes.guess_extension(content_type.split(';')[0]) or '.jpg'

            # Générer un nom de fichier unique
            img_filename = os.path.join(output_dir, f'image_{i}{ext}')

            with open(img_filename, 'wb') as f:
                f.write(img_response.content)

            print(f"[✓] {img_filename}")
            downloaded_count += 1
    except Exception as e:
        print(f"[✗] Erreur avec {img_url}: {e}")

# === ZIP des fichiers ===
zip_filename = f'{output_dir}.zip'
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in os.listdir(output_dir):
        zipf.write(os.path.join(output_dir, file), arcname=file)

print(f"\n✅ Téléchargement terminé : {downloaded_count} image(s) téléchargée(s).")
print(f"📦 ZIP généré : {zip_filename}")

