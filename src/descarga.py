from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://ecobici.mx/datos-abiertos/"
MESES = ["2026-01", "2026-02", "2026-03"]
RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def descargar(periodo: str, url: str) -> None:
    destino = RAW_DIR / f"ecobici_{periodo}.csv"
    if destino.exists():
        print(f"[omitido] {periodo} ya existe")
        return

    print(f"[descargando] {periodo}")
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    destino.write_bytes(resp.content)
    print(f"[guardado] {destino.name}")


RAW_DIR.mkdir(parents=True, exist_ok=True)

response = requests.get(URL, timeout=30)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

print("Conexión exitosa")

archivos = []
for enlace in soup.find_all("a", href=True):
    periodo = enlace.get_text(strip=True)
    if periodo in MESES:
        archivos.append({"periodo": periodo, "url": urljoin(URL, enlace["href"])})

df_archivos = pd.DataFrame(archivos).sort_values("periodo").reset_index(drop=True)
print(df_archivos)
print("Total de archivos encontrados:", len(df_archivos))

for fila in df_archivos.itertuples():
    descargar(fila.periodo, fila.url)
    