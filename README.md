# B Corp Social Impact Analysis

An exploratory data analysis project examining the social and environmental impact of certified B Corporations worldwide, with outputs prepared for Tableau visualization.

## Overview

This project processes raw B Corp certification data to surface insights about company performance across countries, industries, and impact areas. The dataset covers **7,039 unique certified B Corps** across **97 countries** and **22 industry categories**.

### Key Findings

- **Top impact areas** (by mean score): Workers (24.2) > Community (23.1) > Environment (16.2) > Governance (15.6) > Customers (11.3)
- **Geographic concentration**: ~72% of companies are in the US, UK, or Canada
- **Highest-scoring industries**: Energy/Heating (116.5), Water/Sewerage (102.0), Finance (101.7)
- **Score distribution**: Most companies fall in the 80–99.9 range; notable outlier — Dr. Bronner's at 206.7

---

## Project Structure

```
B-Crop-Social-Impact/
├── data/
│   ├── raw/
│   │   └── B-Corp-Impact-Data.csv        # Original dataset (13,694 rows, 135 columns)
│   └── processed/
│       ├── bcorp_clean.csv               # Cleaned, all certification statuses
│       ├── bcorp_certified.csv           # Filtered to certified companies only
│       ├── bcorp_certified_latest.csv    # One record per company (most recent)
│       └── bcorp_certified_latest_tableau.csv  # Tableau-ready with engineered features
├── notebooks/
│   ├── bcrop_cleaning.ipynb              # Data cleaning and deduplication
│   ├── bcorp_eda.ipynb                   # Initial exploratory analysis
│   └── bcrop_certified_latest_eda.ipynb  # Deep EDA with feature engineering
├── scripts/
│   ├── country_summary.py               # Aggregations by country
│   ├── industry_summary.py              # Aggregations by industry
│   ├── impact_summary.py                # Mean scores per impact area
│   └── industry_impact_summary.py       # Impact scores cross-tabulated by industry
├── outputs/
│   ├── country_summary.csv
│   ├── country_summary_filtered.csv     # Countries with >= 10 companies
│   ├── industry_summary.csv
│   ├── industry_summary_filtered.csv    # Industries with >= 10 companies
│   ├── impact_summary.csv
│   └── industry_impact_summary.csv
└── tableau/                             # Tableau workbooks
```

---

## Data Pipeline

### 1. Cleaning (`bcrop_cleaning.ipynb`)
- Reads raw data (13,694 rows, 135 columns)
- Selects 19 core columns
- Filters to `certified` status only (10,754 records)
- Deduplicates by `company_id`, keeping the most recent record → **7,039 unique companies**

### 2. Exploratory Analysis (`bcrop_certified_latest_eda.ipynb`)
- Descriptive statistics and missing value assessment
- Score distribution and banding (Below 80 / 80–89.9 / 90–99.9 / 100–119.9 / 120+)
- Feature engineering: certification year extraction, `years_since_first_certification`, `score_band`
- Country and industry breakdowns
- Exports `bcorp_certified_latest_tableau.csv` for Tableau

### 3. Summary Scripts (`scripts/`)
Each script reads `bcorp_certified_latest.csv` and writes to `outputs/`:

| Script | Output |
|--------|--------|
| `country_summary.py` | Company count + avg score by country |
| `industry_summary.py` | Company count + avg score by industry |
| `impact_summary.py` | Mean score per impact area (community, customers, environment, governance, workers) |
| `industry_impact_summary.py` | Impact area scores cross-tabulated by industry |

---

## Dataset

**Source**: B Corp Impact Data (publicly available from B Lab)

**Core columns used:**

| Column | Description |
|--------|-------------|
| `company_id` | Unique company identifier |
| `company_name` | Company name |
| `country` | Country of operation |
| `industry_category` | Industry classification |
| `size` | Employee size band |
| `overall_score` | Total B Impact Assessment score |
| `impact_area_community` | Community impact score |
| `impact_area_customers` | Customers impact score |
| `impact_area_environment` | Environment impact score |
| `impact_area_governance` | Governance impact score |
| `impact_area_workers` | Workers impact score |
| `date_first_certified` | Date of first certification |
| `current_status` | Certification status |

---

## Requirements

- Python 3.x
- pandas
- matplotlib / seaborn (for notebook visualizations)
- Tableau (for dashboard visualization)
