# CO₂ Emissions & Energy Consumption: Who's Decoupling?

**Module 1 Capstone — Data Wrangling & Retrieval | Ironhack Data Analytics Bootcamp**  
**Team:** Diana Yule · [Irene Fafian]  
**Week:** 4 | **Status:** 🚧 In Progress

---

## Project Overview

Can countries grow their economies without growing their carbon footprint?

This project investigates whether high-income countries are successfully **decoupling GDP growth from CO₂ emissions** — one of the defining questions of the energy transition. Using global emissions and energy data spanning 2014–2024, we clean, merge, and analyse multi-source datasets to test this hypothesis across world regions.

---

## Research Questions

1. Are high-income countries reducing CO₂ emissions while maintaining GDP growth?
2. Which world regions show the strongest decoupling trends between 2014 and 2024?
3. How does primary energy consumption relate to CO₂ intensity per unit of energy across countries?

---

## Data Sources

| File | Description | Source |
|------|-------------|--------|
| `energy_co2_data.csv` | Annual CO₂ emissions, energy mix, and GDP indicators per country (1750–2024) | [Our World in Data — CO₂ & GHG Emissions](https://github.com/owid/co2-data) |
| `e_co2_codebook.csv` | Column definitions, units, and source metadata for the main dataset | [OWID CO₂ Codebook](https://github.com/owid/co2-data/blob/master/owid-co2-codebook.csv) |
| `wregion_mapping.csv` | Country-to-world-region mapping used for regional aggregation | [Our World in Data — World Region Definitions](https://ourworldindata.org/world-region-map-definitions) |

---

## Project Management

📋 **Kanban Board:** [Trello — Data Wrangling Project Week 4](https://trello.com/invite/b/6a140a85c4baf8ce1b4b4c33/ATTI34b2ec4474650fcb84d88b3223c983ce1D21A984/my-trello-board)

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/repository_name.git
```

### 2. Install UV

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (Anaconda Powershell Prompt):**
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. Create and activate the virtual environment

```bash
uv venv
```

**macOS / Linux (bash):**
```bash
source ./venv/bin/activate
```

**macOS / Linux (csh/tcsh):**
```bash
source ./venv/bin/activate.csh
```

**Windows:**
```bash
.\venv\Scripts\activate
```

### 4. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 5. Register the Jupyter kernel

```bash
python -m ipykernel install --user --name=venv
```

### 6. Launch Jupyter

```bash
jupyter notebook
```

---

## Repository Structure

```
first_project/
├── README.md
├── config.yaml                  # Paths and project-wide parameters
├── pyproject.toml               # Production dependencies
├── data/
│   ├── raw/                     # Original unmodified source files
│   └── clean/                   # Processed output: energy_co2_data_cleaned.csv
├── notebooks/
│   ├── raw_eCO2data_cleaning_Diana.ipynb   # Data loading, cleaning, region mapping
│   └── functions.py             # Reusable helper functions
└── figures/                     # Generated plots and visualisations
```

---

## Data Cleaning Methodology

Cleaning is performed programmatically in `raw_eCO2data_cleaning_Diana.ipynb` using Python and Pandas. All steps are reproducible — no manual edits were made to source files.

### Techniques applied

| # | Technique | Detail |
|---|-----------|--------|
| 1 | **Column selection** | Reduced 79 raw columns to 11 relevant features |
| 2 | **Time window filtering** | Kept only rows for years 2014–2024 |
| 3 | **Column renaming** | Shortened verbose column names for readability (e.g. `co2_including_luc` → `co2_luc`) |
| 4 | **Null investigation & row removal** | Identified and dropped regional aggregates (e.g. "Africa", "OECD") that lacked ISO codes — kept Kosovo as a valid country |
| 5 | **Microstate exclusion** | Dropped Monaco, San Marino, and Vatican — their emissions are absorbed into France/Italy in the source data |
| 6 | **Antarctica exclusion** | Removed Antarctica — no government, no emissions data, not relevant to analysis |
| 7 | **Region mapping merge** | Joined country-level data with OWID world region definitions to enable continental aggregation |

### Key dataset decisions

- **Regional rows removed:** The source dataset contains 36 aggregate entries (continents, income groups, GCP blocs). These were excluded in favour of building our own regional groupings via the OWID region mapping file.
- **Kosovo preserved:** Despite having no ISO code, Kosovo is a recognised country and retained in the dataset.
- **Missing `prim_ener_cons` values:** 136 countries have no primary energy consumption data. These rows are retained but flagged — imputation strategy TBD.

---

## Dataset Issues & Solutions

| Issue | Solution |
|-------|----------|
| Source data mixes countries with regional aggregates in the `country` column | Filtered on `iso_code` nulls; retained Kosovo explicitly |
| Microstates (Monaco, San Marino, Vatican) have no independent emissions data | Dropped — their data is embedded in France/Italy |
| Antarctica has no policy-relevant energy data | Dropped |
| 136 countries missing `prim_ener_cons` | Retained with NaN — under review |

---

## Key Findings

> 🚧 To be completed after EDA (Day 4)

---

## Conclusions

> 🚧 To be completed after EDA (Day 4)

---

## Next Steps

