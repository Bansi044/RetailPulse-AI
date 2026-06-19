import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="RetailPulse AI Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------------
# Title
# -------------------------
st.title("📊 RetailPulse AI Dashboard")
st.write("Retail Analytics & Demand Forecasting Dashboard")

# -------------------------
# Sidebar
# -------------------------
st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Select Module",
    [
        "Home",
        "Sales Analysis",
        "Customer Segmentation",
        "Forecasting",
        "Business Insights"
    ]
)

# -------------------------
# Home Page
# -------------------------
if page == "Home":

    st.header("Dashboard Overview")

    rfm = pd.read_csv("customer_rfm.csv")
    sales = pd.read_csv("cleaned_online_retail.csv")

    total_revenue = sales["Revenue"].sum()
    total_customers = rfm["Customer ID"].nunique()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"£{total_revenue:,.0f}")
    col2.metric("Customers", f"{total_customers:,}")
    col3.metric("Prophet MAPE", "39.40%")

    st.success("RetailPulse AI Dashboard Loaded Successfully!")

# -------------------------
# Sales Analysis
# -------------------------
elif page == "Sales Analysis":

    st.header("Sales Analysis")

    try:
        df = pd.read_csv("cleaned_online_retail.csv")
        st.write(df.head())
        revenue = df["Revenue"].head(20)
        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(revenue)
        ax.set_title("Sample Revenue Trend")
        st.pyplot(fig)
    except:
        st.warning("cleaned_online_retail.csv not found.")

# -------------------------
# Customer Segmentation
# -------------------------
elif page == "Customer Segmentation":

    st.header("Customer Segmentation")

    rfm = pd.read_csv("customer_rfm.csv")
    seg_counts = rfm["Segment"].value_counts().reset_index()
    seg_counts.columns = ["Segment", "Customers"]

    st.dataframe(seg_counts)

    fig, ax = plt.subplots()
    ax.bar(seg_counts["Segment"], seg_counts["Customers"])
    ax.set_title("Customer Segments")
    plt.xticks(rotation=15)
    st.pyplot(fig)

# -------------------------
# Forecasting
# -------------------------
elif page == "Forecasting":

    st.header("Demand Forecast")

    try:
        forecast = pd.read_csv("prophet_forecast_results.csv")
        st.write(forecast.head())
        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(forecast["yhat"])
        ax.set_title("Forecasted Sales")
        st.pyplot(fig)
    except:
        st.warning("prophet_forecast_results.csv not found.")

# -------------------------
# Business Insights
# -------------------------
elif page == "Business Insights":

    st.header("Business Insights")

    st.markdown("""
- Revenue trends help monitor business growth.

- Customer segmentation supports targeted marketing.

- Forecasting improves inventory planning.

- KPIs support strategic decision-making.

- RetailPulse AI enables data-driven business intelligence.
""")
