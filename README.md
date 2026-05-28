# CO₂ Emissions & Energy Transition: Who's Decoupling?

**Module 1 Capstone — Data Wrangling & Retrieval | Ironhack Data Analytics Bootcamp**  
**Team:** Diana Yule · Irene Fafian  
**Week:** 4 | **Status:** 📊 EDA Complete (H1 & H2) | H3 Pending

---

## Project Overview

Can countries grow their economies without growing their carbon footprint?

This project investigates whether countries are successfully **decoupling GDP growth from CO₂ emissions** — one of the defining questions of the post-Paris Agreement era. Using global emissions, energy production and consumption, GDP, and electricity access data spanning 2014–2024, we clean build, clean, and analyse a unified dataset to test this question accross world region.

The analysis uses the **post-Paris Agreement window (2014–2020)** as the evaluation frame — a period where climate policy momentum should, in theory, be visible in the data. The three hypotheses below move from diagnosis (is decoupling happening?) to mechanism (what explains it?) to consequence (who actually bears the cost?).

---

## Research Questions & Hypotheses

### Hypothesis 1 — CO₂ Intensity Decline
> **Has the CO₂ intensity of GDP declined across regions between 2014 and 2020, and does the answer change depending on how we measure emissions?**

Metric: `co2_int = co2 / GDP` (Scenario A — fossil + industrial only, optimistic view)  
Metric: `co2_luc_int = co2_luc / GDP` (Scenario B — full footprint including land-use change, honest view)

> If decoupling holds in Scenario A but weakens in Scenario B → high-income countries shifted emissions, not eliminated them.

### Hypothesis 2 — Renewable Penetration as the Mechanism
> **Which regions show evidence that renewable penetration explains CO₂ intensity decline and where is the gap largest?**

Following Hypothesis 1, this asks *why* intensity fell (or didn't): is renewable adoption the driver?  
Metrics: `d_co2_int` (annual Δ CO₂ intensity) vs `d_renew_share` (annual Δ renewable consumption share).

### Hypothesis 3 — Electricity Access & CO₂
> **Do high CO₂ emissions always reflect development and improved living standards, or can they coexist with energy poverty?**

Metrics:
- gdp_per_cap vs prct_access_elec → Tests whether richer countries and regions tend to have better electricity access.
- gdp_group vs prct_access_elec → Compares poor, middle-income, and rich countries to see whether development is associated with higher access, total emissions, and personal carbon footprints.
- co2 (total, not per capita) vs prct_access_elec → Identifies countries with high total emissions but below-median electricity access.
- co2_per_cap as a control → Helps distinguish between countries where emissions are high because individuals consume a lot, and countries where total emissions are high mainly because of population size or industrial scale.

>If countries with low or middle gdp_per_cap and below-median prct_access_elec still show significant total co2, then emissions are not necessarily translating into universal energy access. If co2_per_cap emains relatively low in those same countries, the pattern suggests that the carbon burden is spread across a large population that may not be receiving proportional welfare benefits.

---

## Data Sources

| Dataset | Description | Source | Method |
|---------|-------------|--------|--------|
| `energy_co2_data.csv` | Annual CO₂ emissions, energy mix, GDP, LUC emissions per country (1750–2024) | [Our World in Data — CO₂ & GHG Emissions](https://github.com/owid/co2-data) | Direct download (API/CSV) |
| `wregion_mapping.csv` | Country-to-world-region mapping | [Our World in Data — Region Definitions](https://ourworldindata.org/world-region-map-definitions) | Direct download |
| `world_bank_energy.csv` | Access to electricity (%), renewable energy production (%), renewable energy consumption (%), renewable production (kWh) — World Bank | [World Bank Open Data](https://data.worldbank.org/) | Web scraping / API |
| `UN_GDP.csv` | GDP at current prices (US$) per country 2014–2020 | [UN Stats — National Accounts Main Aggregates](https://unstats.un.org/unsd/snaama/Basic) | Direct download |
| `UN_Population.csv` | Population per country 2014–2024 | [UN Stats — National Accounts Main Aggregates](https://unstats.un.org/unsd/snaama/Basic) | Direct download |
| `world_bank_energy.csv` | Access to electricity (%), renewable energy production (%), renewable energy consumption (%) per country | [World Bank DataBank — World Development Indicators](https://databank.worldbank.org/reports.aspx?source=2&series=EG.ELC.ACCS.UR.ZS) | Direct download |
| `world_bank_car.csv` | GDP, GDP per capita and population for Central African Republic (gap-fill) | [World Bank DataBank — World Development Indicators](https://databank.worldbank.org/reports.aspx?source=2&series=SP.POP.TOTL&country=CAF) | Direct download |

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
| 1 | Null check | Confirmed zero nulls in GDP source before any transformation |
| 2 | Duplicate check | Confirmed zero duplicates across all source files |
| 3 | Column renaming | Standardised to `country`, `year`, `GDP`, `prct_access_elec`, `prct_renew_prod`, `prct_renew_cons` |
| 4 | Unit column drop | Removed `Unit` metadata column (currency label, not needed for analysis) |
| 5 | Wide-to-long reshape | World Bank data pivoted from year-as-columns to long format using `pd.melt()` on year columns |
| 6 | Long-to-wide pivot | Melted rows pivoted back on `series_name` to produce one column per indicator per country-year |
| 7 | Type conversion | `..` strings (World Bank missing marker) converted to NaN and dropped; `year` enforced as integer |
| 8 | GDP per capita | Computed `gdp_per_cap = GDP / population` |
| 9 | Config-driven I/O | All file paths managed via `cfg.yaml` — no hardcoded paths in the notebook |

### Team — `final_clean_merge.ipynb`

| 1 | Multi-source merge | Joined renewables + GDP/population + CO₂/energy datasets on `country` + `year` |
| 2 | Country name harmonisation | Resolved naming mismatches across UN, World Bank, and OWID conventions |
| 3 | Secondary source merge | World Bank GDP/population data merged as a secondary source to fill gaps left by UN data |
| 4 | Null imputation | Missing `GDP`, `gdp_per_cap`, and `population` values filled from the secondary World Bank source using `.fillna()` before dropping redundant columns |
| 5 | Duplicate column cleanup | Post-merge `_x`/`_y` suffixed columns collapsed and renamed to clean final names |
| 6 | Final null check | Confirmed zero nulls across all 13 columns after imputation |
| 7 | Final shape | 1,323 rows × 13 columns — clean, zero nulls, exported via config path |

---

## Derived Metrics (EDA Notebook)

| Column | Formula | Purpose |
|--------|---------|---------|
| `co2_int` | `co2 / GDP` | CO₂ intensity — Scenario A (fossil + industrial only) |
| `co2_luc_int` | `co2_luc / GDP` | CO₂ intensity — Scenario B (full footprint) |
| `d_co2_int` | year-over-year diff of `co2_int` per country | Rate of decoupling |
| `d_co2_luc_int` | year-over-year diff of `co2_luc_int` per country | Rate of decoupling (full footprint, Scenario B) |
| `d_renew_share` | year-over-year diff of `prct_renew_cons` per country | Rate of renewable adoption |
| `co2_per_cap` | `co2 / population` | CO₂ burden per person |
| `welfare_ratio` | `prct_access_elec / co2_per_cap` | Energy benefit per unit of emissions — H3 exploitation index |

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

> ⚠️ Formal statistical tests still pending. These are preliminary observations from EDA.

### H1 — CO₂ Intensity Decline (Scenarios A & B)
- **Europe** is the only region showing a consistent downward CO₂ intensity trend across the full 2014–2020 window.
- **Asia** holds the highest CO₂ intensity by far, with a sharp spike in 2019–2020.
- **South America** diverges upward after 2017, bucking the global trend.
- Most regions declined 2015–2018, then reversed after 2018 — the 2020 dip in some regions is partly COVID-driven, not structural decoupling.
- **Scenario A vs B:** adding land-use change (Scenario B) shifts the absolute intensity values; regions where co2_luc_int diverges significantly from co2_int are likely displacing emissions, not eliminating them.

### H2 — Renewable Penetration as the Mechanism
- Renewable growth correlates with CO₂ intensity decline in **Asia [2016–2019]** and **Europe [2016–2017]**, but not in North America or Oceania.
- A consistent **production/consumption gap** is visible — several regions produce more renewables than they consume domestically, suggesting export rather than domestic decarbonisation.
- **Verdict:** H2 is partially supported. Renewables are a contributing factor, not the sole driver of decoupling.

### H3 — Electricity Access & CO₂ (Pending)
> To be completed once Irene's analysis is delivered.

---

## Known Limitations

- **COVID 2020:** the CO₂ dip visible in 2020 for some regions is partly driven by the economic contraction, not structural decoupling — interpretation of H1 endpoint deltas requires this caveat.
- **GDP metric:** OWID PPP (2011 international $) — absolute intensity values are not current USD. Cross-country comparisons and time-series trends are valid, but headline numbers shouldn't be read as present-day dollar values.
- `prct_renew_prod` (kWh) and `prct_renew_prod` (%) are from different World Bank series — units confirmed before use.
- **Africa data anomalies:** CO₂ patterns for some African countries look inconsistent — flagged during H2 analysis, under investigation.
- Country name mismatches between UN, World Bank, and OWID required manual harmonisation in `final_clean_merge.ipynb`.
- **H3 pending:** electricity access ↔ CO₂ analysis not yet completed (Irene).

---

## Contributors

| Name | Notebooks | Responsibilities |
|------|-----------|-----------------|
| Diana Yule | `raw_eCO2data_cleaning_Diana.ipynb`, `eda_hypothesis_testing_Diana.ipynb` | CO₂ data cleaning, region mapping, EDA, hypothesis 1 & 2 |
| Irene Fafian | `wrangle_clean_irene.ipynb` | GDP, population, renewables cleaning; hypothesis 3 |
| Both | `final_clean_merge.ipynb` | Final merge, country name harmonisation |
