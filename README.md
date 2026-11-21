# Ecobici CDMX: ¿quién y cuándo se mueve?

Análisis exploratorio (EDA) reproducible de los viajes de Ecobici en la Ciudad de México.
Proyecto integrador del Módulo I del diplomado *Métodos estadísticos y matemáticos para la ciencia de datos*.

## Contribuciones

| Integrante | Aportación sustantiva | Secciones del notebook | 
| <Abril Helena Ortiz Soto> | | |
| <Aranza Fernanda Ortiz Lozada> | | |
| <Diego Morando Perez> | | |
| <Rodrigo Perez Perez> | | |
| <Rosalinda> | | |

## Objetivo

Explorar los viajes registrados por Ecobici y responder dos preguntas descriptivas:

1. ¿Qué género realiza más viajes por día?
2. ¿En qué horario se moviliza más la ciudad y hay diferencias entre días entre semana y fines de semana?

## Datos

Los datos se extrajeron de fuentes oficiales 
| Dataset | Descripción | Fuente |
|---|---|---|
| ecobici_2026_%% | Cada fila es un viaje de la estación de retiro (A) a la estación de arribo (B), con género, fecha y hora| <https://ecobici.cdmx.gob.mx/en/open-data/> |
| Estaciones | Georreferenciación (nombre, latitud, longitud) de cada estación por ID. | <https://datos.cdmx.gob.mx/dataset/cicloestaciones-ecobici-nuevo-sistema/resource/e764a27c-2043-42e8-a17f-5a04674b0f1b?view_id=91c9d729-4d80-43c3-ac38-f234bdb147ea> |

- **Periodo analizado:** <01/2026 – 03/2026>
- **Unidad de observación:** Viajes
## Procedencia
Datos abiertos de viajes de Ecobici (CDMX), meses 2026-01 a 2026-03.
Fuente: https://ecobici.mx/datos-abiertos/ (consultado el 21/nov/2026).
Se descargan con `src/descarga.py`.

## Licencia y condiciones de uso
El sitio de la fuente no especifica una licencia para los datos históricos.
Los archivos se incluyen sin modificar y con fines académicos, con atribución
a Ecobici como fuente original. Los derechos sobre los datos pertenecen a sus
publicadores.


## Estructura del repositorio

```
ecobici-eda/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/               # datos originales 
├── notebooks/
│   └── 01_eda_ecobici.ipynb
├── src/                   # funciones auxiliares y extracción de la data
├── results/
│   ├── figures/           # gráficas exportadas
│   └── tables/            # tablas resumen
└── docs/
    └── decisiones_limpieza.md
```

## Cómo reproducir el análisis

**Requisitos:** Python 3.12 o superior y Git.

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Roy8976/proyecto_ecobici.git
   cd proyecto_ecobici
   ```
2. Crear y activar un entorno virtual:
   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   python --version     # debe mostrar 3.12 o superior       # Windows: .venv\Scripts\activate
   ```
3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Abrir y ejecutar el notebook completo (*Kernel → Restart & Run All*):
   ```bash
   jupyter lab notebooks/01_eda_ecobici.ipynb
   ```

Las figuras y tablas se guardan en `results/` 

## Contenido del análisis

0. Configuración de los datos
1. Comprensión de los datos
2. Exploración y estadística descriptiva
3. Calidad, limpieza y transformación (decisiones justificadas en `docs/decisiones_limpieza.md`)
4. Visualizaciones con interpretación
5. Conclusiones y limitaciones

## Resultados principales

<RESUMIR EN 2-3 VIÑETAS LOS HALLAZGOS Y ENLAZAR UNA FIGURA DE `results/figures/`>

## Limitaciones

<EJ.: periodo acotado, registros sin género, no se infiere causalidad>


