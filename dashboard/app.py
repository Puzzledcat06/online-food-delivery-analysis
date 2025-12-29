import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import plotly.express as px
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

# -----------------------------------
# LOAD ENV VARIABLES
# -----------------------------------
load_dotenv()  # Load .env file automatically

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Online Food Delivery Analysis",
    layout="wide"
)

st.title("Online Food Delivery Analysis Dashboard")
st.markdown("SQL-driven analytics dashboard built using **MySQL + Streamlit**")

# -----------------------------------
# DATABASE CONNECTION
# -----------------------------------
engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# -----------------------------------
# HELPER FUNCTION FOR RUNNING QUERIES
# -----------------------------------
@st.cache_data
def run_query(query):
    with engine.connect() as conn:
        result = conn.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    return df

# -----------------------------------
# KPI SECTION
# -----------------------------------
st.subheader("Key Metrics Overview")

kpi_query = """
SELECT
    COUNT(*) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    ROUND(AVG(order_value), 2) AS avg_order_value,
    ROUND(AVG(delivery_time_min), 2) AS avg_delivery_time
FROM food_orders;
"""
kpi_df = run_query(kpi_query)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Orders", kpi_df.total_orders[0])
col2.metric("Total Customers", kpi_df.total_customers[0])
col3.metric("Avg Order Value", f"₹{kpi_df.avg_order_value[0]}")
col4.metric("Avg Delivery Time", f"{kpi_df.avg_delivery_time[0]} min")

st.divider()

# -----------------------------------
# WEEKEND vs WEEKDAY
# -----------------------------------
st.subheader("Weekend vs Weekday Demand")

day_df = run_query("""
SELECT day_type, COUNT(*) AS total_orders
FROM food_orders
GROUP BY day_type;
""")

st.plotly_chart(
    px.pie(day_df, names="day_type", values="total_orders", hole=0.4,
           title="Order Share: Weekend vs Weekday"),
    width='stretch'
)

# -----------------------------------
# CITY-WISE ANALYSIS
# -----------------------------------
st.subheader("City-wise Order Volume")

city_df = run_query("""
SELECT city, COUNT(*) AS total_orders
FROM food_orders
GROUP BY city
ORDER BY total_orders DESC;
""")

st.plotly_chart(
    px.bar(city_df, x="total_orders", y="city", orientation="h",
           title="Orders by City"),
    width='stretch'
)

# -----------------------------------
# CUISINE ANALYSIS
# -----------------------------------
st.subheader("Cuisine-wise Popularity")

cuisine_df = run_query("""
SELECT cuisine_type, COUNT(*) AS total_orders
FROM food_orders
GROUP BY cuisine_type
ORDER BY total_orders DESC;
""")

st.plotly_chart(
    px.bar(cuisine_df, x="cuisine_type", y="total_orders",
           title="Cuisine Popularity"),
    width='stretch'
)

# -----------------------------------
# DELIVERY PERFORMANCE
# -----------------------------------
st.subheader("Delivery Performance Breakdown")

delivery_df = run_query("""
SELECT delivery_performance, COUNT(*) AS total_orders
FROM food_orders
GROUP BY delivery_performance;
""")

st.plotly_chart(
    px.bar(delivery_df, x="delivery_performance", y="total_orders",
           color="delivery_performance", title="Delivery Performance Status"),
    width='stretch'
)

# -----------------------------------
# DISTANCE vs DELIVERY TIME
# -----------------------------------
st.subheader("Distance vs Delivery Time")

scatter_df = run_query("""
SELECT distance_km, delivery_time_min
FROM food_orders
WHERE distance_km IS NOT NULL
AND delivery_time_min IS NOT NULL
LIMIT 5000;
""")

st.plotly_chart(
    px.scatter(scatter_df, x="distance_km", y="delivery_time_min",
               opacity=0.5, title="Delivery Time vs Distance"),
    width='stretch'
)

# -----------------------------------
# PEAK vs NON-PEAK
# -----------------------------------
st.subheader("Peak vs Non-Peak Orders")

peak_df = run_query("""
SELECT day_type,
       CASE WHEN is_peak_hour = 1 THEN 'Peak' ELSE 'Non-Peak' END AS period,
       COUNT(*) AS total_orders
FROM food_orders
GROUP BY day_type, period;
""")

st.plotly_chart(
    px.bar(peak_df, x="day_type", y="total_orders", color="period",
           barmode="stack", title="Peak Hour Demand Comparison"),
    width='stretch'
)

# -----------------------------------
# PAYMENT MODE
# -----------------------------------
st.subheader("Payment Mode Preference")

payment_df = run_query("""
SELECT payment_mode, COUNT(*) AS total_orders
FROM food_orders
GROUP BY payment_mode;
""")

st.plotly_chart(
    px.pie(payment_df, names="payment_mode", values="total_orders",
           hole=0.4, title="Preferred Payment Methods"),
    width='stretch'
)

# -----------------------------------
# CANCELLATION ANALYSIS
# -----------------------------------
st.subheader("Cancellation Reasons")

cancel_df = run_query("""
SELECT cancellation_reason, COUNT(*) AS total_cancellations
FROM food_orders
WHERE order_status = 'Cancelled'
AND cancellation_reason IS NOT NULL
GROUP BY cancellation_reason
ORDER BY total_cancellations DESC;
""")

st.plotly_chart(
    px.bar(cancel_df, x="total_cancellations", y="cancellation_reason",
           orientation="h", title="Common Order Cancellation Reasons"),
    width='stretch'
)

# -----------------------------------
# FOOTER
# -----------------------------------
st.success("Dashboard loaded successfully using SQL!")
