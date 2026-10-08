# Week 2 Task – Data Collection, Cleaning, and Preprocessing for Logistics Analysis

## Project
Logistics Data Quality and Preprocessing Pipeline

## Objective
Prepare a logistics shipment dataset for reliable downstream analytics by simulating data collection, identifying data-quality issues, cleaning records, handling missing values, detecting/correcting outliers, standardizing fields, and applying normalization.

## Dataset
The project includes `data/logistics_raw.csv`, a simulated logistics dataset designed in the style of publicly available transport/shipping datasets. It contains shipment IDs, dates, origins/destinations, transport modes, carriers, distances, weights, shipment volumes, promised and actual delivery times, transportation cost, and delivery status.

The raw dataset intentionally contains realistic quality problems so the preprocessing pipeline can demonstrate the required techniques.

## Files
- `Week2_Logistics_Data_Preprocessing_Report.docx` – complete submission report.
- `data/logistics_raw.csv` – raw/simulated data with intentional quality issues.
- `data/logistics_cleaned.csv` – processed dataset ready for analysis.
- `src/preprocess_logistics.py` – reproducible Python preprocessing pipeline.
- `REPORT_DESCRIPTION_200_WORDS.txt` – submission-form description.
- `README.md` – project instructions.

## How to run
1. Install Python 3.x.
2. Install pandas and numpy:
   `pip install pandas numpy`
3. From the project folder run:
   `python src/preprocess_logistics.py`

## Main techniques
- Data inspection and profiling
- Duplicate detection/removal
- Missing-value treatment using median/mode
- Invalid-value handling
- IQR-based outlier detection and capping
- Text/category standardization
- Min-Max normalization
- Final data-quality validation

## Note
The dataset is simulated for educational/internship purposes and is not presented as an official company dataset.
