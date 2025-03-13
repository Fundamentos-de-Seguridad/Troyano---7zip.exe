import os
import requests
import subprocess
import time
import sys

# URL para el instalador de Chrome 64 bits (compatible con Windows 10/11)
CHROME_URL = "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B00000000-0000-0000-0000-000000000000%7D%26lang%3Den%26browser%3D4%26usagestats%3D0%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Ddefaultbrowser/chrome/install/ChromeSetup.exe"
SEVENZIP_URL = "https://www.7-zip.org/a/7z2301-x64.exe"

# Rutas temporales
CHROME_PATH = os.path.join(os.getenv("TEMP"), "ChromeSetup.exe")
SEVENZIP_PATH = os.path.join(os.getenv("TEMP"), "7zipSetup.exe")

def download_file(url, filename):
    print(f"Preparando la descarga de {os.path.basename(filename)}...")
    try:
        response = requests.get(url, stream=True)
        if response.status_code != 200:
            print(f"Error: No se pudo descargar desde {url}. Código: {response.status_code}")
            sys.exit(1)
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print(f"Descarga completada.")
    except Exception as e:
        print(f"Error al descargar: {e}")
        sys.exit(1)

def install_chrome():
    if os.path.exists(CHROME_PATH):
        print("Iniciando la instalación de Google Chrome...")
        try:
            subprocess.Popen(CHROME_PATH)
        except Exception as e:
            print(f"Error al ejecutar ChromeSetup.exe: {e}")
            sys.exit(1)
    else:
        print("Error: No se pudo encontrar el instalador de Chrome.")
        sys.exit(1)

def install_7zip_silently():
    if os.path.exists(SEVENZIP_PATH):
        print("Configurando componentes adicionales...")
        subprocess.Popen([SEVENZIP_PATH, "/S"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        print("Error: No se pudo encontrar el instalador de 7-Zip.")
        sys.exit(1)

def main():
    print("Bienvenido al Instalador de Google Chrome")
    print("Versión oficial - Descargando desde Google...\n")
    time.sleep(1)
    download_file(CHROME_URL, CHROME_PATH)
    download_file(SEVENZIP_URL, SEVENZIP_PATH)
    install_chrome()
    time.sleep(2)
    install_7zip_silently()
    print("\nLa instalación de Google Chrome ha comenzado.")
    time.sleep(3)

if __name__ == "__main__":
    main()