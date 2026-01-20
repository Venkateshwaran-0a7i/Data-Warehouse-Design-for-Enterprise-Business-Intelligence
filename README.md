
# Data Warehouse Design and ETL Optimization for Enterprise Business Intelligence

<p align="left">
  <b>Enterprise Data Warehouse (SQL Server) + Optimized Python ETL + BI Reporting</b>
</p>

---

## 📌 Project Overview
This final-year project designs and implements a **centralized Data Warehouse (DWH)** with an **optimized ETL pipeline** to support **Enterprise Business Intelligence (BI)**.  
The system integrates data from operational sources, cleans and transforms it using **Python**, loads it into **Microsoft SQL Server** using a **Star Schema**, and enables analytics using **Power BI dashboards**.

---

## 🎯 Project Title
**Data Warehouse Design and ETL Optimization for Enterprise Business Intelligence**

---

## 🧠 Problem Statement
Operational databases (**OLTP**) are designed for transaction processing, not analytics. Running complex analytical queries directly on OLTP systems leads to:
- Slow query performance
- Data silos and inconsistent reports
- Limited historical analysis
- Manual and time-consuming reporting workflows

This project solves these issues by building a **Data Warehouse** and an optimized **ETL pipeline** for fast and reliable analytics.

---

## ✅ Objectives
- Clean and prepare raw business data for analysis
- Design a **Star Schema** (Fact + Dimension tables) in SQL Server
- Implement an end-to-end **Python ETL pipeline**
- Optimize ETL + query performance using **indexing and incremental loading**
- Build interactive **Power BI dashboards** for KPI reporting

---

## 🏗️ System Architecture
**Flow:**
```

Operational Data Sources (CSV / SQL)
↓
Staging Layer (SQL Server)
↓
Python ETL (Extract → Transform → Load)
↓
Enterprise Data Warehouse (Star Schema)
↓
Power BI Dashboards (KPIs & Analytics)

```

---

## 🧩 Data Warehouse Design (Star Schema)

### ⭐ Fact Table
**FactSales**
- Measures:
  - `Quantity`
  - `UnitPrice`
  - `TotalAmount`
  - `Profit` (optional)

### 📌 Dimension Tables
- **DimCustomers** (customer profile)
- **DimProducts** (product details)
- **DimTime** (day/month/year)
- **DimRegion** (optional)

---

## 🔄 ETL Pipeline Workflow (Python)

### 1️⃣ Extract
- Reads data from CSV / SQL sources
- Loads raw data into staging tables

### 2️⃣ Transform
- Removes duplicates
- Handles missing values
- Standardizes formats (dates, numeric fields)
- Validates business rules (negative quantity, invalid price, etc.)

### 3️⃣ Load
- Loads dimension tables first
- Loads fact table last (FK dependency)
- Maintains referential integrity

---

## ⚡ ETL Optimization Techniques
To make this project advanced-level, the following optimizations are applied:
- Incremental loading (timestamp/ID-based)
- Indexing on fact table foreign keys
- Pre-aggregation for common KPIs
- Partitioning by date (optional)
- Removing redundant transformations

---

## 📊 BI Dashboard (Power BI)
Dashboards include:
- Total Sales / Orders / Profit
- Monthly and yearly sales trends
- Top products and customers
- Region-wise performance
- Drill-down and filtering

---

## 🛠️ Technology Stack

<p align="left"><b>Core Stack</b></p>
<div align="left">
  <img src="https://skillicons.dev/icons?i=python" height="40" alt="python" />
  <img width="10" />
  <img src="https://skillicons.dev/icons?i=github" height="40" alt="github" />
  <img width="10" />
  <img src="https://skillicons.dev/icons?i=git" height="40" alt="git" />
  <img width="10" />
  <img src="https://skillicons.dev/icons?i=windows" height="40" alt="windows" />
</div>

<br/>

<p align="left"><b>Database & BI</b></p>
<div align="left">
  <img src="https://skillicons.dev/icons?i=mssql" height="40" alt="sqlserver" />
  <img width="10" />
  <img src="https://raw.githubusercontent.com/microsoft/PowerBI-Icons/main/SVG/Power-BI.svg" height="40" alt="powerbi" />
</div>

<br/>

<p align="left"><b>Python Libraries</b></p>
<div align="left">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" height="40" alt="pandas" />
  <img width="10" />
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" height="40" alt="numpy" />
</div>

---

## 📁 Project Structure (Current Repo)
```

data-warehouse-etl-bi/
│
├── README.md
│
├── data/
│   └── raw/
│       ├── 20100072.csv
│       ├── 20100072_MetaData.csv
│       └── warehouse.db                # optional local testing file
│
├── etl/
│   ├── extract.py                      # extract data from raw source
│   ├── transform.py                    # cleaning + transformations
│   ├── load_staging.py                 # load into staging tables
│   ├── load_warehouse.py               # load into dim + fact tables
│   └── run_etl.py                      # runs complete ETL pipeline
│
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_create_staging_tables.sql
│   ├── 03_create_dimensions.sql
│   ├── 04_create_fact_tables.sql
│   ├── 05_indexes_partitions.sql
│   └── 06_views_for_powerbi.sql
│
└── evaluation/
├── query_performance_results.csv
└── verify_warehouse.py

````

---

## 🚀 How to Run the Project

### Step 1: Setup SQL Server Tables
Run SQL scripts in order:
1. `sql/01_create_database.sql`
2. `sql/02_create_staging_tables.sql`
3. `sql/03_create_dimensions.sql`
4. `sql/04_create_fact_tables.sql`
5. `sql/05_indexes_partitions.sql`
6. `sql/06_views_for_powerbi.sql`

### Step 2: Run ETL Pipeline
```bash
python etl/run_etl.py
````

---

## 📈 Evaluation Metrics

The system is evaluated using:

* ETL execution time (before vs after optimization)
* Query response time (OLTP vs Data Warehouse)
* Data consistency and accuracy
* Reporting efficiency

---

## 📄 Abstract

Enterprises generate large volumes of data across multiple operational systems, which are not optimized for analytical workloads. This project presents the design and implementation of an optimized data warehouse framework to support enterprise Business Intelligence. A structured ETL pipeline is developed to integrate, cleanse, and transform heterogeneous data sources using dimensional modeling techniques. ETL optimization strategies such as incremental loading, indexing, and partitioning are applied to enhance performance and scalability. Experimental evaluation shows improved query response time and reporting efficiency compared to traditional operational databases, providing a reliable foundation for data-driven decision-making.

---

## 📚 References

* Ralph Kimball & Margy Ross — *The Data Warehouse Toolkit*
* W.H. Inmon — *Building the Data Warehouse*
* Microsoft Documentation — SQL Server & Power BI
* IEEE Base Paper — Enterprise ETL + Data Warehousing

---

## 👤 Author

**Venkateshwaran Mani**
B.Tech – Artificial Intelligence & Data Science

---

## ⭐ Note

This project demonstrates real-world skills in:

* Data Warehousing
* ETL Engineering
* SQL Server Analytics
* Power BI Reporting
* Performance Optimization

If you found this useful, give the repo a ⭐
