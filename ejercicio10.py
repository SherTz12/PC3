import requests
import zipfile
import os

url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
nombre_imagen = "perro.jpg" 


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/117.0.0.0 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  
   
    with open(nombre_imagen, "wb") as f:
        f.write(response.content)
    print(f"Imagen descargada como '{nombre_imagen}'")
except requests.RequestException as e:
    print(f"Error al descargar la imagen: {e}")

nombre_zip = "perro.zip"
with zipfile.ZipFile(nombre_zip, "w") as zipf:
    zipf.write(nombre_imagen)
print(f"Imagen guardada en el ZIP '{nombre_zip}'")

carpeta_destino = "descomprimido"
os.makedirs(carpeta_destino, exist_ok=True)

with zipfile.ZipFile(nombre_zip, "r") as zipf:
    zipf.extractall(carpeta_destino)
print(f"ZIP descomprimido en la carpeta '{carpeta_destino}'")
