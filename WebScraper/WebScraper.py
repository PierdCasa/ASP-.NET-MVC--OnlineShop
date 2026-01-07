import json
import requests
import re
import hashlib 
from bs4 import BeautifulSoup

g = open("WB.txt", "w", encoding="utf-8")

##############################################
url = "https://www.emag.ro/laptopuri/p2/c"
categ = "Electronice"
###############################################
#Change to your desired site/category 

#The STOCK IS DEFAULT 100

#Headers to avoid being blocked by IP

headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

target_domain = "https://s13emagst.akamaized.net/products/"

def generate_seed_id_hash(name, description, image_url):

    base = name.lower()
    ###########################################
    base = re.sub(r'Laptop\s*', '', base)
    #Edit this regexp for each desired product 
    ############################################
    base = re.sub(r'[^a-z0-9\s]', '', base)
    base = re.sub(r'\s+', '-', base.strip())[:40]
    unique_str = f"{name}|{description}|{image_url}"
    hash_suffix = hashlib.md5(unique_str.encode()).hexdigest()[:6]
    
    return f"{base}-{hash_suffix}"


products = []

# 1. Find the images with the target domain
images = soup.find_all('img', src=re.compile(re.escape(target_domain)))

for img in images:
    # --- IMAGE & TITLE LOGIC ---
    full_src = img.get('src')
    clean_url = full_src.split('?')[0]
    alt_text = img.get('alt', '')
    
    if ',' in alt_text:
        parts = alt_text.split(',', 1)
        name = parts[0].strip()
        description = parts[1].strip()
    else:
        name = alt_text.strip()
        description = "ERROR"

    # --- PRICE EXTRACTION LOGIC ---
    # We find the closest parent container (the product card) 
    # and then find the price paragraph inside it.
    parent_card = img.find_parent('div', class_='card-item')
    price_val = None
    
    if parent_card:
        price_tag = parent_card.find('p', class_='product-new-price')
        if price_tag:
            # .get_text() extracts: "649,99 Lei"
            # We remove "Lei", swap the comma for a dot, and strip spaces
            raw_price = price_tag.get_text(strip=True).replace('Lei', '').strip()
            # Replace European decimal comma with a dot and drop thousand separators
            normalized = raw_price.replace(',', '.')
            parts = normalized.split('.')
            if len(parts) > 2:
                # Join all but the last part as the integer portion, keep final decimal part
                normalized = ''.join(parts[:-1]) + '.' + parts[-1]
            try:
                price_val = float(normalized)
            except ValueError:
                price_val = None

    seed_id = generate_seed_id_hash(name, description, clean_url)
    if price_val is not None and description != "ERROR":
        products.append({
            "SeedId": seed_id,
            "Title": name,
            "Description": description,
            "Price": price_val,
            "Stock": 100,
            "CategoryName": categ,
            "Status": 1,
            "ImagePath": clean_url,
        })

json.dump({"Products": products}, g, ensure_ascii=True, indent=2)
g.close()
