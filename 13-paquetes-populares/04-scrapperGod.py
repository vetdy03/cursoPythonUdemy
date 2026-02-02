import requests
from bs4 import BeautifulSoup
import time

def safe_scrape():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    # Añadir un delay aleatorio
    time.sleep(1)
    
    try:
        response = requests.get(
            "https://stackoverflow.com/questions", 
            headers=headers,
            timeout=15
        )
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Método más genérico: buscar cualquier título
            titles = soup.find_all(['h1', 'h2', 'h3'])
            print("Títulos encontrados en la página:")
            for title in titles[:10]:
                text = title.get_text(strip=True)
                if text and len(text) > 10:
                    print(f"- {text}")
                    
        else:
            print(f"Error {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")

safe_scrape()