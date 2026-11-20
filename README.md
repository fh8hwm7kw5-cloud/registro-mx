# REGISTRO MX 0.8 (base de análisis y Observatorio de Precios)

## Instalación
Subir los archivos del ZIP a la raíz del repositorio GitHub, conservando `.github/`, `scripts/`, `radar.html` y `radar.json` existentes. No subir el ZIP como archivo único.

## Módulos
- `analisis.html`: filtros combinables, gráficas de registros por dependencia, porcentajes y exportación CSV. **Basado en muestra**, no en todo el universo de contratos.
- `presupuestos.html` + `presupuestos.json`: estructura 2020–2026; cifras sin verificar permanecen `null`. No se publican cifras inventadas.
- `precios.html` + `comparaciones_precios.json`: Observatorio de Precios, preparado para comparaciones verificadas, actualmente sin resultados.
- `perfiles.html`: perfiles de proveedores y dependencias 2025.

## Para añadir comparaciones de precios
Solo incorporar registros verificados a `comparaciones_precios.json`, con los campos `anio`, `producto`, `dependencia`, `precio_gobierno_mxn`, `precio_mercado_mxn`, `url_contrato`, `url_mercado`, `fecha_precio_mercado`. Antes de publicar verificar equivalencia de especificaciones, cantidades, IVA, moneda, vigencia, garantía y servicios incluidos. El administrador edita el JSON desde GitHub. No se incluye scraping automático ni autenticación administrativa en esta versión.

## Limitaciones
La suma monetaria en `analisis.html` solo usa importes numéricos con moneda explícita MXN en los registros de la muestra. No implica presupuesto ejercido ni sobreprecio. El Radar existente se conserva.
