# Data Warehouse Design and ETL Optimization for Enterprise Business Intelligence

## 📌 Project Overview
This final-year project designs and implements a **centralized Data Warehouse (DWH)** with an **optimized ETL pipeline** to support **Enterprise Business Intelligence (BI)**.  
The system integrates data from multiple operational sources, cleans and transforms it using **Python**, loads it into **Microsoft SQL Server** using a **Star Schema**, and visualizes insights through **Power BI dashboards**.

---

## 🎯 Project Title
**Data Warehouse Design and ETL Optimization for Enterprise Business Intelligence**

---

## 🧠 Problem Statement
Operational databases (OLTP) are optimized for transaction processing, not analytics. Running complex analytical queries on OLTP systems leads to:
- Slow query performance
- Data silos and inconsistent reporting
- Limited historical trend analysis
- Manual, time-consuming reporting processes

This project solves the problem by building an **Enterprise Data Warehouse** with an optimized ETL pipeline to enable fast, accurate, and scalable analytics.

---

## ✅ Objectives
- Clean and prepare raw business data for analysis
- Design a **dimensional model (Star Schema)** in SQL Server
- Implement an end-to-end **Python ETL pipeline**
- Optimize ETL and query performance using indexing and incremental loads
- Build interactive **Power BI dashboards** for KPI reporting and insights

---


## 🏗️ System Architecture

**Flow:**

Operational Data Sources → Staging Layer → ETL Pipeline → Data Warehouse → BI Dashboards

### Key Components

* **Source Systems:** Sales, HR, Finance (CSV / SQL)
* ↓
* **Staging Layer:** Raw data validation and cleansing
* ↓
* **ETL Layer:** Incremental extraction, transformation, aggregation
* ↓
* **Data Warehouse:** Fact and Dimension tables
* ↓
* **BI Layer:** KPI dashboards and analytical reports

---

## 🧩 Data Warehouse Design (Star Schema)

### ⭐ Fact Table
**FactSales**
- Stores transactional measures like:
  - `Quantity`
  - `UnitPrice`
  - `TotalAmount`
  - `Profit` (optional)

### 📌 Dimension Tables
- **DimCustomers** (customer profile, purchase behavior)
- **DimProducts** (product category, description)
- **DimTime** (day, month, year, quarter)
- **DimRegion** (optional)

---

## 🔄 ETL Pipeline Workflow (Python)

### 1️⃣ Extract
- Read data from CSV / Excel / SQL sources
- Store raw data into **staging tables**

### 2️⃣ Transform
- Remove duplicates
- Handle missing values
- Standardize date/time formats
- Validate values (example: negative quantity checks)
- Generate surrogate keys (if required)

### 3️⃣ Load
- Load dimension tables first
- Load fact tables last (FK dependency)
- Maintain referential integrity

---

## ⚡ ETL Optimization Techniques
To make the project advanced-level, the following optimizations are applied:
- Incremental loading (timestamp/ID-based)
- Indexing on foreign keys in fact tables
- Pre-aggregation for common KPI reports
- Partitioning fact tables by date (optional)
- Removing redundant transformations

---

## 📊 BI Dashboard (Power BI)
Power BI reports include:
- Total Sales / Profit / Orders
- Monthly & yearly sales trends
- Top products and customers
- Region-wise performance
- Sales funnel / conversion insights (optional)

---

## 🛠️ Technology Stack

### Software Requirements
- Python 3.x (Pandas, SQLAlchemy, pyodbc)
- Microsoft SQL Server (Developer / Express)
- Power BI Desktop
- Git & GitHub

### Hardware Requirements
- CPU: x64 ≥ 2.0 GHz
- RAM: 8 GB recommended
- Storage: 100 GB SSD recommended

---


## 🛠️ Technology Stack

| Layer              | Tools                |
| ------------------ | -------------------- |
| Data Sources       | CSV, SQL             |
| ETL                | Python (Pandas), SQL |
| Data Warehouse     | PostgreSQL / MySQL   |
| BI & Visualization | Power BI / Tableau   |
| Version Control    | Git, GitHub          |

---

## 📁 Project Structure

```
data-warehouse-etl-bi/
│
├── README.md
│
├── data/
│ └── raw/
│ ├── 20100072.csv
│ ├── 20100072_MetaData.csv
│ └── warehouse.db # (Local test DB file - optional)
│
├── etl/
│ ├── extract.py # Extract data from source files
│ ├── transform.py # Data cleaning + transformations
│ ├── load_staging.py # Load cleaned data into staging tables
│ ├── load_warehouse.py # Load data into fact + dimension tables
│ ├── run_etl.py # Main pipeline runner (end-to-end)
│ │
│ └── pycache/ # Auto-generated (should be ignored in Git)
│ ├── extract.cpython-313.pyc
│ ├── transform.cpython-313.pyc
│ ├── load_staging.cpython-313.pyc
│ └── load_warehouse.cpython-313.pyc
│
├── sql/
│ ├── 01_create_database.sql # Create database + schema setup
│ ├── 02_create_staging_tables.sql # Create staging layer tables
│ ├── 03_create_dimensions.sql # Create dimension tables
│ ├── 04_create_fact_tables.sql # Create fact tables
│ ├── 05_indexes_partitions.sql # Performance tuning scripts
│ └── 06_views_for_powerbi.sql # Views for reporting / Power BI
│
├── evaluation/
│ ├── query_performance_results.csv # Query runtime benchmarking results
│ └── verify_warehouse.py # Script to validate warehouse outputs
│

```

---

## 📄 Abstract

Enterprises generate large volumes of data across multiple operational systems, which are not optimized for analytical workloads. This project presents the design and implementation of an optimized data warehouse framework to support enterprise Business Intelligence. A structured ETL pipeline is developed to integrate, cleanse, and transform heterogeneous data sources using dimensional modeling techniques. ETL optimization strategies such as incremental loading, indexing, and partitioning are applied to enhance performance and scalability. Experimental evaluation shows improved query response time and reporting efficiency compared to traditional operational databases, providing a reliable foundation for data-driven decision-making.

---

## 📈 Evaluation Metrics
The system is evaluated using:
- ETL execution time (before vs after optimization)
- Query response time (OLTP vs DWH)
- Data consistency and accuracy
- Reporting efficiency

---

## 📚 References
- Ralph Kimball & Margy Ross — *The Data Warehouse Toolkit*
- W.H. Inmon — *Building the Data Warehouse*
- Microsoft Documentation — SQL Server & Power BI
- IEEE Base Paper (Enterprise ETL + Data Warehousing)

---

## 👤 Author
**Venkateshwaran Mani**  
B.Tech – Artificial Intelligence & Data Science  


---

## ⭐ Note
This project demonstrates real-world skills in:
- Data Warehousing
- ETL Engineering
- SQL Server Analytics
- Power BI Reporting
- Performance Optimization

If you found this useful, give the repo a ⭐
