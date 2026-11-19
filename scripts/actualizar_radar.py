
import json
import re
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from html import unescape

# REGISTRO MX | Radar informativo
# Noticias externas, separadas de los datos oficiales.

ARCHIVO = Path("radar.json")

BUSQUEDAS = [
    "contrataciones públicas México licitaciones",
    "adjudicación directa gobierno México",
    "Auditoría Superior Federación contratos",
    "INE contratos proveedores auditoría",
    "Compras MX transparencia contrataciones",
]

def limpiar(texto):
    texto = re.sub(r"<[^>]+>", " ", texto or "")
    return re.sub(r"\s+", " ", unescape(texto)).strip()

def buscar_noticias(consulta):
    parametros = urllib.parse.urlencode({
        "q": consulta,
        "hl": "es-419",
        "gl": "MX",
        "ceid": "MX:es-419",
    })
    url = "https://news.google.com/rss/search?" + parametros

    solicitud = urllib.request.Request(
        url,
        headers={"User-Agent": "REGISTRO-MX-Radar/0.1"}
    )

    with urllib.request.urlopen(solicitud, timeout=25) as respuesta:
        contenido = respuesta.read()

    raiz = ET.fromstring(contenido)
    resultados = []

    for item in raiz.findall(".//channel/item"):
        titulo = limpiar(item.findtext("title"))
        enlace = item.findtext("link", "").strip()
        fecha_original = item.findtext("pubDate", "")
        fuente = item.find("source")
        medio = limpiar(fuente.text if fuente is not None else "")

        try:
            fecha = parsedate_to_datetime(
                fecha_original
            ).astimezone(timezone.utc).isoformat()
        except (TypeError, ValueError):
            continue

        if not titulo or not enlace:
            continue

        resultados.append({
            "id": item.findtext("guid", enlace),
            "titulo": titulo,
            "medio": medio or "Fuente no identificada",
            "fecha": fecha,
            "url": enlace,
            "categoria": "Cobertura periodística",
            "tipo_fuente": "Medio de comunicación",
            "estado": "Información publicada por terceros",
            "resumen": "",
        })

    return resultados

def main():
    noticias = {}

    if ARCHIVO.exists():
        try:
            anteriores = json.loads(
                ARCHIVO.read_text(encoding="utf-8")
            )
            for noticia in anteriores.get("noticias", []):
                noticias[noticia["id"]] = noticia
        except (OSError, ValueError, KeyError):
            print("No se pudo leer el radar anterior.")

    exitos = 0

    for consulta in BUSQUEDAS:
        try:
            encontrados = buscar_noticias(consulta)
            exitos += 1
            for noticia in encontrados:
                noticias[noticia["id"]] = noticia
            print(f"{consulta}: {len(encontrados)} resultados")
        except Exception as error:
            print(f"Error consultando {consulta}: {error}")

    if exitos == 0:
        raise RuntimeError("No se pudo consultar ninguna fuente.")

    ordenadas = sorted(
        noticias.values(),
        key=lambda noticia: noticia["fecha"],
        reverse=True
    )[:150]

    salida = {
        "proyecto": "REGISTRO MX",
        "actualizado": datetime.now(timezone.utc).isoformat(),
        "advertencia": (
            "Estas referencias son cobertura periodística externa. "
            "No constituyen evidencia concluyente de irregularidades "
            "ni forman parte de los datos oficiales de contratos."
        ),
        "noticias": ordenadas,
    }

    ARCHIVO.write_text(
        json.dumps(salida, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"Radar actualizado: {len(ordenadas)} noticias")

if __name__ == "__main__":
    main()
