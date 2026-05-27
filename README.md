# CO₂ Emissions & Energy Transition: Who's Decoupling?

**Module 1 Capstone — Data Wrangling & Retrieval | Ironhack Data Analytics Bootcamp**  
**Team:** Diana Yule · Irene Fafian  
**Week:** 4 | **Status:** 🔬 EDA & Hypothesis Testing In Progress

---

## Project Overview

Can countries grow their economies without growing their carbon footprint?

This project investigates whether countries are successfully **decoupling GDP growth from CO₂ emissions** — one of the defining questions of the post-Paris Agreement era. Using global emissions, energy, GDP, and electricity access data spanning 2014–2024, we clean, merge, and analyse multi-source datasets to test this hypothesis across world regions.

The analysis uses the **post-Paris Agreement window (2014–2024)** as the evaluation frame — a period where policy momentum should, in theory, be visible in the data.

---

## Research Questions & Hypotheses

### Hypothesis 1 — CO₂ Intensity Decline
> **Has CO₂ intensity of GDP (co2 / GDP) declined across regions from 2014–2021?**

Metric: `co2_int = co2 / GDP` (Scenario A — fossil + industrial only, optimistic view)  
Metric: `co2_luc_int = co2_luc / GDP` (Scenario B — full footprint including land-use change, honest view)

> If decoupling holds in Scenario A but weakens in Scenario B → high-income countries shifted emissions, not eliminated them.

### Hypothesis 2 — Renewable Penetration as the Mechanism
> **Which regions show evidence that renewable penetration explains CO₂ intensity decline — and where is the gap largest?**

Following Hypothesis 1, this asks *why* intensity fell (or didn't): is renewable adoption the driver?  
Metrics: `d_co2_int` (annual Δ CO₂ intensity) vs `d_renew_share` (annual Δ renewable consumption share).

### Hypothesis 3 — Electricity Access & CO₂ *(Pending — Irene)*
> **Do countries with low electricity access correlate with high CO₂ emissions?**

Linking `prct_access_elec` to `co2` / `co2_luc` to identify whether energy poverty and high emissions co-exist or diverge across regions.

---

## Data Sources

| Dataset | Description | Source | Method |
|---------|-------------|--------|--------|
| `energy_co2_data.csv` | Annual CO₂ emissions, energy mix, GDP, LUC emissions per country (1750–2024) | [Our World in Data — CO₂ & GHG Emissions](https://github.com/owid/co2-data) | Direct download (API/CSV) |
| `wregion_mapping.csv` | Country-to-world-region mapping | [Our World in Data — Region Definitions](https://ourworldindata.org/world-region-map-definitions) | Direct download |
| `world_bank_energy.csv` | Access to electricity (%), renewable energy production (%), renewable energy consumption (%), renewable production (kWh) — World Bank | [World Bank Open Data](https://data.worldbank.org/) | Web scraping / API |
| `UN_GDP.csv` | GDP at current prices (US$) per country 2014–2024 | [UN Data — National Accounts](https://data.un.org/) | Web scraping / API |
| `UN_Population.csv` | Population per country 2014–2024 | [UN Data — Population](https://data.un.org/) | Web scraping / API |

---

## Project Management

📋 **Kanban Board:** [Trello — Data Wrangling Project Week 4](https://trello.com/invite/b/6a140a85c4baf8ce1b4b4c33/ATTI34b2ec4474650fcb84d88b3223c983ce1D21A984/my-trello-board)

---

## Repository Structure

```
first_project/
├── README.md
├── cfg.yaml                          # Paths and project-wide parameters
├── pyproject.toml                    # Production dependencies
├── uv.lock                           # Pinned dependency lock file
├── .gitignore
├── data/
│   ├── raw/                          # Original unmodified source files
│   └── clean/                        # Processed outputs (merged_final.csv etc.)
├── notebooks/
│   ├── raw_eCO2data_cleaning_Diana.ipynb   # Diana: OWID CO₂ data cleaning + region mapping
│   ├── wrangle_clean_irene.ipynb           # Irene: GDP, population, renewables cleaning
│   ├── final_clean_merge.ipynb             # Team: final merge + country name harmonisation
│   ├── eda_hypothesis_testing_Diana.ipynb  # Diana: EDA, CO₂ intensity, hypothesis testing
│   └── functions.py                        # Shared reusable helper functions
├── figures/                          # Generated plots and visualisations
├── slides/
│   └── project_presentation.pptx
└── sql_scripts/
    ├── ERD_Miro.png                  # Entity-Relationship Diagram (Miro)
    └── MiniProject_GDP_CO2_schema.sql # SQL schema (drawDB export)
```

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

**macOS / Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
uv pip install -r pyproject.toml
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

## Data Pipeline — How to Run

Run notebooks **in this order** to reproduce the full pipeline:

| Step | Notebook | Owner | Output |
|------|----------|-------|--------|
| 1 | `raw_eCO2data_cleaning_Diana.ipynb` | Diana | `data/clean/co2_clean.csv` |
| 2 | `wrangle_clean_irene.ipynb` | Irene | `data/clean/gdp_pop_clean.csv` |
| 3 | `final_clean_merge.ipynb` | Team | `data/clean/merged_final.csv` |
| 4 | `eda_hypothesis_testing_Diana.ipynb` | Diana | Figures + findings |

All paths are managed via `cfg.yaml` — no hardcoded paths in any notebook.

---

## Data Cleaning Methodology

### Diana — `raw_eCO2data_cleaning_Diana.ipynb`

Source: Our World in Data CO₂ dataset (79 columns, 1750–2024).

| # | Technique | Detail |
|---|-----------|--------|
| 1 | Column selection | Reduced 79 raw columns to 11 relevant features |
| 2 | Time window filtering | Kept only 2014–2024 |
| 3 | Column renaming | Shortened verbose names (e.g. `co2_including_luc` → `co2_luc`) |
| 4 | Regional aggregate removal | Dropped 36 non-country rows (continents, income groups) using ISO code filter |
| 5 | Microstate exclusion | Removed Monaco, San Marino, Vatican (emissions absorbed into France/Italy) |
| 6 | Antarctica exclusion | No government, no policy-relevant data |
| 7 | Region mapping | Joined OWID region file to enable continental aggregation |
| 8 | Kosovo preserved | No ISO code but valid sovereign country — retained explicitly |

### Irene — `wrangle_clean_irene.ipynb`

Sources: UN GDP data, UN Population data, World Bank renewables data.

| # | Technique | Detail |
|---|-----------|--------|
| 1 | Column renaming | Standardised to `country`, `year`, `GDP`, `population` etc. |
| 2 | Unit column drop | Removed metadata columns not needed for analysis |
| 3 | Duplicate check | Confirmed zero duplicates across all three source files |
| 4 | Null handling | "Western Africa" aggregate row had no population match → dropped (regional aggregate, not a country) |
| 5 | GDP per capita | Computed `gdp_per_cap = GDP / population` |
| 6 | Wide-to-long reshape | World Bank data pivoted from year-as-columns to long format |
| 7 | Type conversion | Numeric columns enforced as float; `..` strings (World Bank missing marker) converted to NaN and dropped |

### Team — `final_clean_merge.ipynb`

| # | Technique | Detail |
|---|-----------|--------|
| 1 | Inner merge | Joined renewables + GDP/pop + CO₂ datasets on `country` + `year` |
| 2 | Country name harmonisation | Resolved mismatches between UN, World Bank, and OWID naming conventions |
| 3 | Remaining null removal | Rows without a match across all three sources dropped |
| 4 | Final shape | 1,323 rows × 13 columns — clean, zero nulls |

---

## Derived Metrics (EDA Notebook)

| Column | Formula | Purpose |
|--------|---------|---------|
| `co2_int` | `co2 / GDP` | CO₂ intensity — Scenario A (fossil + industrial only) |
| `co2_luc_int` | `co2_luc / GDP` | CO₂ intensity — Scenario B (full footprint) |
| `d_co2_int` | year-over-year diff of `co2_int` per country | Rate of decoupling |
| `d_renew_share` | year-over-year diff of `prct_renew_cons` per country | Rate of renewable adoption |

---

## Database Schema

The relational schema is fully designed and normalised to **3NF**. No database was instantiated for this project phase — schema only.

**Schema design tools:** Miro (ERD diagram) + drawDB (SQL DDL export)  
**Files:** `sql_scripts/ERD_Miro.png` · `sql_scripts/MiniProject_GDP_CO2_schema.sql`

### Tables

| Table | Role |
|-------|------|
| `fact_energy` | Energy metrics per record: electricity access, primary consumption, renewable production/consumption |
| `fact_emissions` | CO₂ and CO₂-LUC values |
| `fact_economy` | GDP, population, GDP per capita |
| `region` | Region name + ISO code lookup |
| `country` | Central dimension linking all fact tables + region via foreign keys |

---

## Key Findings

> 🚧 To be completed after hypothesis testing is finalised

---

## Known Limitations

- `2020–2021` COVID dip artificially suppresses CO₂ — trend interpretation requires this caveat
- `prct_renew_prod` (kWh) and `prct_renew_prod` (%) are from different World Bank series — units confirmed before use
- Country name mismatches between UN, World Bank, and OWID required manual harmonisation in `final_clean_merge.ipynb`
- Hypothesis 3 (electricity access ↔ CO₂) is pending Irene's contribution

---

## Contributors

| Name | Notebooks | Responsibilities |
|------|-----------|-----------------|
| Diana Yule | `raw_eCO2data_cleaning_Diana.ipynb`, `eda_hypothesis_testing_Diana.ipynb` | CO₂ data cleaning, region mapping, EDA, hypothesis 1 & 2 |
| Irene Fafian | `wrangle_clean_irene.ipynb` | GDP, population, renewables cleaning; hypothesis 3 (pending) |
| Both | `final_clean_merge.ipynb` | Final merge, country name harmonisation |
