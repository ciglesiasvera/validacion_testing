Ejercicio: Crear suite básica de tests para un pipeline simple

Verificación: 
1. ¿Por qué es importante testear pipelines de datos? 
Respuesta:

Basado en la teoría de que "los pipelines procesan datos críticos", el testing es vital por tres razones fundamentales:

- Confianza en la toma de decisiones: Si un pipeline alimenta un dashboard de ventas para el CEO, un error de cálculo (como sumar doble) puede llevar a decisiones financieras erróneas. El testing asegura la Exactitud.

- Regresión (Regression Testing): En Data Science, los códigos cambian constantemente. El testing asegura que, al agregar una nueva funcionalidad (ej. soporte para múltiples monedas), no se haya roto la lógica de suma existente ("Los cambios no rompen funcionalidad existente").

- Ahorro de Costos: Detectar un error en la etapa de desarrollo (Unit Test) es exponencialmente más barato que detectarlo en Producción, donde podría requerir reprocesar terabytes de datos históricos.

2. ¿Qué tipos de errores son más comunes en pipelines y cómo detectarlos con tests?

Aquí se conectan los tipos de errores con los tipos de testing:

|-----------------------------------|--------------------------------------------|-------------------------------------------------------------------------------------------|
| Tipo de Error				        | Descripción				                 | Cómo detectarlo (Tipo de Test)                                                            |
|-----------------------------------|--------------------------------------------|-------------------------------------------------------------------------------------------|
|Cambios en el Schema (Schema Drift)|Por error, la columna llega como            |Validación de Calidad / Contrato: Verificar que las claves del diccionario existan antes   | 
|                                   |precio_usd en lugar de precio.              |de procesar.                                        |
|-----------------------------------|--------------------------------------------|-------------------------------------------------------------------------------------------|
|Datos Sucios (Data Quality)		|Precios negativos, nulos (Null) o formatos  |Validación (Task 2): Tests que verifiquen precio > 0 o completitud.                        |
|                                   |de fecha erróneos.                          |                                                                                           |
|-----------------------------------|--------------------------------------------|-------------------------------------------------------------------------------------------|
|Errores de Lógica de Negocio		|El cálculo del total excluye impuestos      |Testing Unitario (Task 1): Casos de prueba como test_calculo_totales donde se sabe         |
|                                   |cuando debería incluirlos, o suma mal los   |matemáticamente cuál debe ser el resultado.                                                |
|                                   |duplicados.                                 |                                                                                           |
|-----------------------------------|--------------------------------------------|-------------------------------------------------------------------------------------------|
|Fallos de Conexión				    |La base de datos de destino está caída      |Testing de Integración (Task 3): Simular el flujo completo (test_pipeline_completo) para   |
|                                   |o la API cambió sus permisos.               |ver si los componentes "hablan" entre sí.                                                  |
|-----------------------------------|--------------------------------------------|-------------------------------------------------------------------------------------------|