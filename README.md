# REGISTRO MX 0.6

## Contenido
- `index.html`: nuevo resumen de datos procesados de 2020–2026.
- `demo.html`: copia de la página anterior con datos ficticios, claramente separada.
- `datos-historicos.html` y `datos-2025.html`: exploradores de la versión 0.5.
- `resumen_2020_2026.json`, `resumen_2025.json`: estadísticas derivadas de CSV aportados.
- `muestra_2020_2026.json`, `muestra_2025.json`: muestras para navegación, no bases completas.
- `plantilla_relaciones.csv`: plantilla original.

## INSTALACIÓN EN GITHUB
Sube los 10 archivos de este ZIP a la **raíz** de tu repositorio `registro-mx` usando Add file > Upload files y Commit changes. Reemplaza los archivos homónimos existentes. NO borres ni reemplaces `.github/workflows/radar-semanal.yml`, `scripts/actualizar_radar.py`, `radar.json` ni `radar.html`: esos archivos ya están en GitHub y se preservan.

## Advertencias metodológicas
Los recuentos son filas de los archivos, no contratos únicos. No representan necesariamente gasto público total. 2020–2022 tienen cobertura limitada; 2026 YTD es provisional y su archivo original puede estar incompleto. Los montos monetarios no se agregan en el resumen porque requieren validación de monedas, duplicados y reglas de importes. Las noticias son externas y no constituyen prueba de irregularidades. La página demostrativa permanece aislada en `demo.html`.

## Automatización
El Radar automático existente continúa operando con `radar.json` y `radar.html`; este paquete NO cambia el workflow ni automatiza la importación de contratos. Para actualizar contratos se requiere un proceso independiente de descarga, validación y publicación.


## REGISTRO MX 0.7

Nuevo explorador `perfiles.html` que lee `perfiles_2025.json`, generado a partir del CSV oficial 2025 completo. Incluye perfiles por nombre de proveedor o dependencia, recuentos de filas, contrapartes, procedimientos y hasta 8 enlaces a registros originales por perfil. No se calculan montos ni se infieren irregularidades. Los datos del radar automático se mantienen en GitHub y no se incluyen en este ZIP; no borrar `radar.json`, `radar.html`, `.github` ni `scripts`.
