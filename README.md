# 🍔 Online Food Delivery Analysis

A complete end-to-end data analytics project that analyzes online food delivery orders to uncover customer behavior, operational performance, and business insights using **Python, SQL (MySQL), and Streamlit**.

---

## 📌 Project Overview

Online food delivery platforms generate large volumes of transactional data.  
This project focuses on analyzing such data to answer key business questions related to:

- Customer ordering behavior
- City and cuisine demand patterns
- Delivery performance and delays
- Peak-hour demand trends
- Payment preferences and order cancellations

The project follows a **real-world analytics workflow**, from raw data exploration to SQL-based analytics and an interactive dashboard.

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Data Analysis:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn, Plotly  
- **Database:** MySQL  
- **ORM / Connectivity:** SQLAlchemy, PyMySQL  
- **Dashboard:** Streamlit  
- **Environment:** Virtual Environment (venv)

---

## 📂 Project Structure

online-food-delivery-analysis/
│
├── data/
│ ├── raw/ # Original dataset
│ ├── processed/ # Cleaned & feature-engineered data
│
├── notebooks/
│ ├── 01_data_understanding.ipynb
│ ├── 02_data_cleaning.ipynb
│ ├── 03_exploratory_data_analysis.ipynb
│ ├── 04_feature_engineering.ipynb
│ ├── 05_sql_analysis.ipynb
│
├── dashboard/
│ └── app.py # Streamlit SQL-driven dashboard
│
├── requirements.txt
├── README.md


---

## 🔄 Project Workflow

### 1️⃣ Data Understanding
- Loaded raw CSV data
- Checked shape, column types, missing values, duplicates
- Identified business-relevant attributes

### 2️⃣ Data Cleaning
- Handled missing values logically (not blindly)
- Standardized column names
- Corrected data types
- Removed inconsistencies

### 3️⃣ Exploratory Data Analysis (EDA)
- Order value distribution
- Weekend vs weekday demand
- City-wise and cuisine-wise trends
- Delivery time and distance analysis

### 4️⃣ Feature Engineering
Created meaningful features such as:
- Day type (Weekday / Weekend)
- Peak hour flag
- Order hour
- Customer age groups
- Delivery performance categories
- Profit margin percentage

The processed dataset was saved for downstream use.

### 5️⃣ SQL Analysis (MySQL)
- Loaded processed data into MySQL
- Executed analytical SQL queries for:
  - KPIs
  - Demand patterns
  - Delivery performance
  - Payment preferences
  - Cancellation reasons

### 6️⃣ Dashboard (Streamlit)
- Built a **SQL-driven interactive dashboard**
- All insights are fetched using **live SQL queries**
- Different chart types used for different business questions

---

## 📊 Dashboard Insights

The Streamlit dashboard provides:

- Key business KPIs
- Weekend vs weekday demand comparison
- City-wise order volume
- Cuisine popularity
- Delivery performance breakdown
- Distance vs delivery time relationship
- Peak vs non-peak order analysis
- Payment mode preferences
- Cancellation reason analysis

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone <your-repo-link>
cd online-food-delivery-analysis

2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Ensure MySQL is running

Create database: food_delivery_db

Load the processed data using the SQL notebook

5️⃣ Run the dashboard
streamlit run dashboard/app.py

🔑 Key Learnings

End-to-end data analytics workflow

Practical data cleaning and feature engineering

Writing business-focused SQL queries

Connecting Python applications to MySQL

Building production-style Streamlit dashboards

Handling real-world issues like database connection errors

📈 Future Improvements

Add user-level filters in dashboard

Convert SQL queries into database views

Deploy dashboard to cloud

Integrate real-time data ingestion

📌 Conclusion

This project demonstrates how raw transactional data can be transformed into meaningful business insights using a structured analytics approach. It closely resembles how data analytics projects are executed in real-world industry environments.


---




