# Generador de Reportes ZASCA

Esta aplicación Streamlit genera reportes estructurados para los centros ZASCA de INNPULSA, analizando datos de diagnóstico y cierre para evaluar el impacto del programa en las unidades productivas participantes.

## Características Principales

- Carga y procesamiento de archivos Excel con datos de diagnóstico y cierre
- Análisis automático de variables clave en seis dimensiones:
  * Optimización operativa
  * Calidad del producto
  * Gestión del talento humano
  * Prácticas gerenciales
  * Desempeño financiero
  * Asociatividad empresarial
- Generación de interpretaciones basadas en datos
- Creación de contenido narrativo usando IA
- Exportación de resultados en formato JSON

## Requisitos Previos

- Python 3.13.1 o superior
- Cuenta de OpenAI con API key
- Acceso a los datos de diagnóstico y cierre de ZASCA

## Instalación

1. Clonar el repositorio:
    ```sh
    git clone https://github.com/innpulsa/zasca-report-generator.git
    cd zasca-report-generator
    ```

2. Crear y activar el entorno virtual:
    ```sh
    conda create --name .innpulsa python=3.13.1
    conda activate .innpulsa
    ```

3. Instalar dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Configurar la API key de OpenAI:
    ```sh
    # Linux/Mac
    export OPENAI_API_KEY='tu-api-key'
    
    # Windows
    set OPENAI_API_KEY=tu-api-key
    ```

## Uso

1. Acceder a la aplicación:
   - Versión en producción: [innpulsa-igl.dap-tools.uk](https://innpulsa-igl.dap-tools.uk)
   - Versión local (desarrollo): 
     ```sh
     streamlit run app.py
     ```
     Luego acceder a través del navegador: `http://localhost:8501`

2. Cargar el archivo Excel con los datos de diagnóstico y cierre

3. Completar la información del centro ZASCA:
   - Nombre del centro
   - Número de cohorte
   - Sector productivo
   - Información adicional relevante

4. Seleccionar el modelo de OpenAI a utilizar

5. Generar el reporte

## Estructura del Proyecto

```
zasca-report-generator/
├── app.py                 # Aplicación principal Streamlit
├── src/
│   ├── models.py         # Modelos de datos
│   ├── openai_api.py     # Integración con OpenAI
│   ├── prompts_config.py # Configuración de prompts
│   ├── sections_config.py # Configuración de secciones
│   └── utils.py          # Funciones auxiliares
├── assets/               # Recursos gráficos
└── requirements.txt      # Dependencias del proyecto
```

## Tipos de variables

- **numeric**: Variables numéricas con valores antes/después
- **boolean**: Variables Sí/No
- **dummy**: Variables con respuestas múltiples
- **categorical**: Variables con categorías predefinidas
- **array**: Variables con múltiples opciones separadas por punto y coma

## Configuración de variables

El archivo `sections_config.py` define las variables a analizar en cada sección. Ejemplo:

```python
sections_config = {
    "Optimización operativa": [
        (("produccion_antes", "produccion_despues"), "numeric", 
         {"description": "producción mensual"}),
        (("eficiencia_antes", "eficiencia_despues"), "numeric", 
         {"description": "eficiencia operativa"}),
    ],
    # ... otras secciones
}
```

## Contribuciones

Para contribuir al proyecto:

1. Fork del repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Este proyecto es propiedad del Innovation Growth Lab. Todos los derechos reservados.

## Soporte

Para soporte técnico o consultas, contactar a:
- Data and Technology Unit at the Innovation Growth Lab
- Email: [innovationgrowthlab@nesta.org.uk](mailto:innovationgrowthlab@nesta.org.uk)