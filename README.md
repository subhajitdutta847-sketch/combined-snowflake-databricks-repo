# combined-snowflake-databricks-repo
combined-snowflake-databricks-repo
# 🚀 Snowflake Gold Dashboard (Streamlit App)

A modern **data analytics dashboard built with Streamlit and Snowflake**, designed to query, transform, and visualize country-level data from a Gold-layer table.

---

## 📌 Project Overview

This project is an end-to-end data application that connects to **Snowflake**, reads processed data from a Gold layer table, and displays insights in an interactive **Streamlit dashboard**. https://app-gold-dashboard-jatlhyuulappt6g8g4rszvv.streamlit.app/

It demonstrates:
- Cloud data warehouse integration (Snowflake)
- SQL-based analytics
- Python data processing
- Interactive web app development using Streamlit

---
## 📚 Data Source
This project is based on the DataCamp course **"Joining Data in SQL"**  
https://www.datacamp.com/learn/courses/joining-data-in-sql

## 🏗️ Architecture

Snowflake (Gold Layer Table)
↓
Snowpark / Snowflake Connector
↓
Python Backend (Pandas)
↓
Streamlit UI Dashboard 

## 📊 Features

- 🔗 Secure connection to Snowflake using credentials
- 📥 Fetch data from `GOLD.GOLD_COUNTRY_COMPARISON` table
- 🔍 Filter data by country or other attributes
- 📊 Interactive visualizations (tables, charts)
- ⚡ Real-time data refresh on rerun
- 🧩 Modular Python code structure

---

## 🧰 Tech Stack

- **Python 3.10+**
- **Streamlit**
- **Snowflake Snowpark / Connector**
- **Pandas**
- **SQL (Snowflake)**

---

## 📁 Project Structure
snowflake-gold-dashboard/
│
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── .streamlit/
│ └── secrets.toml # Snowflake credentials (NOT pushed to GitHub)
├── README.md # Project documentation


---

## ⚙️ Setup Instructions

### Clone the repository
```bash
git clone https://github.com/your-username/snowflake-gold-dashboard.git
cd snowflake-gold-dashboard
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
.streamlit/secrets.toml

Add
[snowflake]
account = "YOUR_ACCOUNT"
user = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
role = "YOUR_ROLE"
warehouse = "YOUR_WAREHOUSE"
database = "YOUR_DATABASE"
schema = "YOUR_SCHEMA"
```
---

# 🚀 Databricks Data Engineering Pipeline (S3 + Delta Lake)

A cloud-based data engineering pipeline built using Databricks (Apache Spark) and AWS S3, designed to process, transform, and enrich country-level economic and population data.

## 📌 Project Overview

This project builds an end-to-end ETL pipeline in Databricks that:

- Reads raw CSV data from AWS S3  
- Cleans and transforms datasets using Spark  
- Joins multiple datasets (fact + dimension model)  
- Creates enriched datasets  
- Stores output in Delta Lake format  
- Makes data available for analytics and dashboards

## 🏗️ Architecture

AWS S3 (Raw Data)
↓
Databricks (Spark ETL)
↓
Data Transformation + Joins
↓
Delta Lake (Enriched Tables)
↓
Databricks SQL Dashboard

## 📊 Datasets

### 1. Economies Dataset (Fact Table)

Contains key economic indicators:

- GDP per capita  
- Inflation rate  
- Gross savings  
- Imports / exports  
- Unemployment rate  
- Yearly country-level data  

---

### 2. Countries Dataset (Dimension Table)

Contains country metadata:

- Country name  
- Continent  
- Region  
- Capital city  
- Government form  
- Surface area  

---

### 3. Population Dataset

Contains population statistics by country and year:

- Population values over time  
- Country-wise yearly population trends

## 🔗 Data Pipeline Steps

### 1. Read data from S3

```python
economies_df = spark.read.csv(
    "s3://srh-data-engineering-project-storage/raw/economies/",
    header=True,
    inferSchema=True
)

countries_df = spark.read.csv(
    "s3://srh-data-engineering-project-storage/raw/countries/",
    header=True,
    inferSchema=True
)
```
---

### 2. Join datasets (Fact + Dimension)

```python
joined_df = economies_df.join(
    countries_df,
    economies_df["country_code"] == countries_df["code"],
    "left"
)
```

---

### 3. Write to Delta Lake

The transformed and joined dataset is stored in **Delta Lake format** on AWS S3. This ensures ACID transactions, scalability, and efficient querying in Databricks.

```python
joined_df.write.format("delta") \
    .mode("overwrite") \
    .save("s3://srh-data-engineering-project-storage/delta/economies_enriched/")
```

---

### 4. Register as Databricks Table

The Delta Lake output is registered as a **Databricks table**, making it accessible for SQL queries, analytics, and dashboards.

```sql
CREATE TABLE IF NOT EXISTS economies_enriched
USING DELTA
LOCATION 's3://srh-data-engineering-project-storage/delta/economies_enriched/';
```

---

## 📈 Output Table Schema

The final enriched dataset stored in Delta Lake contains the following fields:

- country_code  
- country_name  
- continent  
- region  
- year  
- gdp_percapita  
- inflation_rate  
- unemployment_rate  
- imports  
- exports

---

## ⚙️ Tech Stack

- Apache Spark (Databricks)  
- Delta Lake  
- AWS S3  
- Python  
- SQL (Databricks SQL)

---

## 📁 Project Structure

```bash
databricks-pipeline/
│
├── notebooks/
│ ├── economies_pipeline.py
│ ├── population_pipeline.py
│
├── delta_tables/
│ ├── economies_enriched/
│ ├── population_enriched/
│
├── README.md
```

---

## 👨‍💻 Author

Subhajit Dutta & Syed Afnan Hasan
