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

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Revenue",
        "£1.2M"
    )

    col2.metric(
        "Customers",
        "4300"
    )

    col3.metric(
        "Forecast Accuracy",
        "92%"
    )

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

    data = {

        "Segment":[
            "VIP",
            "Regular",
            "At Risk",
            "Lost"
        ],

        "Customers":[
            520,
            1800,
            900,
            450
        ]

    }

    seg = pd.DataFrame(data)

    st.dataframe(seg)

    fig, ax = plt.subplots()

    ax.bar(
        seg["Segment"],
        seg["Customers"]
    )

    ax.set_title("Customer Segments")

    st.pyplot(fig)

# -------------------------
# Forecasting
# -------------------------
elif page == "Forecasting":

    st.header("Demand Forecast")

    try:

        forecast = pd.read_csv(
            "prophet_forecast_results.csv"
        )

        st.write(
            forecast.head()
        )

        fig, ax = plt.subplots(
            figsize=(10,5)
        )

        ax.plot(
            forecast["yhat"]
        )

        ax.set_title(
            "Forecasted Sales"
        )

        st.pyplot(fig)

    except:

        st.warning(
            "prophet_forecast_results.csv not found."
        )

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