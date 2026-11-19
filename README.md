# REGISTRO MX — MVP 0.1

Primera versión local y sin costo de la plataforma de transparencia.

## Cómo abrir
1. Descarga y descomprime `registro_mx_mvp.zip`.
2. Abre la carpeta `registro_mx_mvp`.
3. Haz doble clic en `index.html`. Se abrirá en tu navegador.

No necesitas instalar Node.js ni crear cuentas para probar esta versión.

## Qué incluye
- Dashboard de contrataciones.
- Explorador con búsqueda y filtros.
- Vistas agregadas de empresas y dependencias.
- Indicadores calculados.
- Expediente detallado de cada registro.
- Importación y exportación CSV local.

## Importante
Los seis registros incluidos son completamente ficticios y solo sirven para probar el funcionamiento. No son datos de contratos reales ni afirmaciones sobre entidades, empresas o personas existentes. La aplicación no se conecta todavía a Compras MX ni a ninguna base gubernamental.

## Formato CSV esperado
Encabezados recomendados:
`id,objeto,dependencia,empresa,procedimiento,sector,fecha,anio,monto,estado,fuente,monto_original,monto_modificado`

También reconoce algunos alias como `descripcion`, `titulo`, `entidad`, `proveedor`, `importe` y `url`.

La importación ocurre en el navegador y reemplaza los registros de demostración durante esa sesión. No hay backend ni persistencia entre sesiones todavía.

## Próximo paso técnico
Validar un archivo público de Compras MX, documentar su estructura y crear un importador específico que conserve identificadores de origen, fecha de descarga, URL de fuente y trazabilidad de transformaciones.

## Actualización 0.2: Red de Contrataciones
- Nueva sección para comparar la concentración de proveedores por dependencia.
- Importación local de relaciones empresariales documentadas mediante un segundo CSV.
- Cada vínculo requiere dos entidades, tipo de relación, evidencia y, de ser posible, URL y fecha.
- La aplicación distingue concentración contractual de relaciones corporativas: no deduce parentescos, propiedad ni conflictos de interés.
- Se muestra cuántas empresas relacionadas aparecen también como proveedoras en los contratos cargados.

### CSV de relaciones empresariales
Encabezados aceptados:
`entidad_a,entidad_b,tipo_relacion,evidencia,fuente,fecha`

Ejemplo de estructura (no usar datos ficticios como evidencia):
`Empresa A,Empresa B,representante legal común,Acta o registro público que lo acredita,https://...,2025-01-15`

La importación es local y temporal. Los datos no se envían a un servidor ni se guardan al cerrar el navegador. La versión aún no descarga automáticamente información de Compras MX.


## Radar informativo (v0.3)

La versión incluye una sección separada de enlaces a publicaciones periodísticas y cobertura de investigaciones públicas sobre contrataciones del INE. Cada tarjeta muestra medio, fecha, tema, tipo de publicación, resumen editorial y enlace a la nota original. Estas notas son referencias informativas: **no se importan como datos contractuales ni alimentan los indicadores**. La selección es inicial y debe actualizarse y verificarse periódicamente.


## REGISTRO MX 0.4: datos oficiales 2025

Se añade `datos-2025.html`, un panel independiente que analiza las 129,074 filas del archivo fuente `CONTRATOS_COMPRASMX_2025.CSV` aportado para el proyecto. Contiene estadísticas sobre todas las filas y un explorador limitado explícitamente a las primeras 2,500 filas. La página principal conserva la demo y ofrece un enlace al nuevo panel. No se incorpora el CSV original de 150 MB al repositorio.

Los montos son una suma exploratoria del campo `Monto sin imp./mínimo` para registros con moneda MXN y valor numérico no negativo; no son gasto ejecutado ni contratos únicos. La clasificación por instituciones y proveedores utiliza nombres tal como aparecen en el CSV. No hay actualización automática ni revisión documental de cada contrato.

Para publicar, sube los archivos de esta carpeta a la raíz del repositorio GitHub Pages, reemplazando `index.html` y `README.md` y añadiendo `datos-2025.html`, `resumen_2025.json`, `muestra_2025.json`.
