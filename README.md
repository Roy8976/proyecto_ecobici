# Ecobici CDMX: ¿quién y cuándo se mueve?

Análisis exploratorio (EDA) reproducible de los viajes de Ecobici en la Ciudad de México.
Proyecto integrador del Módulo I del diplomado *Métodos estadísticos y matemáticos para la ciencia de datos*.

## Objetivo

Explorar los viajes registrados por Ecobici y responder dos preguntas descriptivas:

1. ¿Qué género realiza más viajes por día?
2. ¿En qué horario se moviliza más la ciudad y hay diferencias entre días entre semana y fines de semana?

## Datos

| Dataset | Descripción | Fuente |
|---|---|---|
| Viajes | Cada fila es un viaje de la estación de retiro (A) a la estación de arribo (B), con género, fecha y hora. Solo incluye el número de estación. | <ENLACE A LA FUENTE OFICIAL> |
| Estaciones | Georreferenciación (nombre, latitud, longitud) de cada estación por ID. | <ENLACE> |

- **Periodo analizado:** <MES/AÑO – MES/AÑO>
- **Unidad de observación:** un viaje.
- **Condiciones de uso / licencia:** <COPIAR LA LICENCIA O TÉRMINOS DE LA FUENTE>
- Más detalle y diccionario de variables en [`data/README.md`](data/README.md).

## Estructura del repositorio

```
ecobici-eda/
├── README.md
├── CONTRIBUCIONES.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── README.md          # procedencia, licencia, diccionario de variables
│   ├── raw/               # datos originales (no se modifican)
│   └── processed/         # datos limpios generados por el notebook
├── notebooks/
│   └── 01_eda_ecobici.ipynb
├── src/                   # funciones auxiliares (opcional)
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
