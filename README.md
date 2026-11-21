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
| Viajes | Cada fila es un viaje de la estación de retiro (A) a la estación de arribo (B), con género, fecha y hora. Solo incluye el número de estación. | <https://ecobici.cdmx.gob.mx/en/open-data/> |
| Estaciones | Georreferenciación (nombre, latitud, longitud) de cada estación por ID. | <https://datos.cdmx.gob.mx/dataset/cicloestaciones-ecobici-nuevo-sistema/resource/e764a27c-2043-42e8-a17f-5a04674b0f1b?view_id=91c9d729-4d80-43c3-ac38-f234bdb147ea> |

- **Periodo analizado:** <01/2026 – 03/2026>
- **Unidad de observación:** Viajes.

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

**Requisitos:** Python 3.10 o superior y Git.

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Roy8976/proyecto_ecobici.git
   cd proyecto_ecobici
   ```
2. Crear y activar un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   ```
3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Abrir y ejecutar el notebook completo (*Kernel → Restart & Run All*):
   ```bash
   jupyter lab notebooks/01_eda_ecobici.ipynb
   ```

Las figuras y tablas se guardan en `results/` y los datos limpios en `data/processed/`.

## Contenido del análisis

1. Comprensión de los datos
2. Exploración y estadística descriptiva
3. Calidad, limpieza y transformación (decisiones justificadas en `docs/decisiones_limpieza.md`)
4. Visualizaciones con interpretación
5. Conclusiones y limitaciones

## Resultados principales

<RESUMIR EN 2-3 VIÑETAS LOS HALLAZGOS Y ENLAZAR UNA FIGURA DE `results/figures/`>

## Limitaciones

<EJ.: periodo acotado, registros sin género, no se infiere causalidad>

## Versión final

Etiqueta (tag): `v1.0-entrega`

## Equipo

Ver [`CONTRIBUCIONES.md`](CONTRIBUCIONES.md).
