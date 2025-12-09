import streamlit as st
import pandas as pd
import numpy as np

# ---------------------- PAGE CONFIG ---------------------- #
st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)

# ---------------------- DATA LOADING --------------------- #
@st.cache_data
def load_data():
    # CSV is in the same folder as app.py
    df = pd.read_csv("customer_shopping_data.csv")

    # Basic cleaning / feature engineering
    df["invoice_date"] = pd.to_datetime(df["invoice_date"], dayfirst=True, errors="coerce")
    df["Total_Amount"] = df["quantity"] * df["price"]
    df["Month"] = df["invoice_date"].dt.to_period("M").astype(str)
    df["Year"] = df["invoice_date"].dt.year
    df["Day"] = df["invoice_date"].dt.date

    return df.dropna(subset=["invoice_date"])

df = load_data()

# ---------------------- SIDEBAR -------------------------- #
st.sidebar.title("🔧 Filters")

# Date range filter
min_date = df["invoice_date"].min()
max_date = df["invoice_date"].max()
date_range = st.sidebar.date_input(
    "Invoice Date Range",
    value=(min_date.date(), max_date.date()),
    min_value=min_date.date(),
    max_value=max_date.date()
)

# Gender filter
genders = df["gender"].dropna().unique().tolist()
selected_genders = st.sidebar.multiselect(
    "Gender",
    options=genders,
    default=genders
)

# Category filter
categories = df["category"].dropna().unique().tolist()
selected_categories = st.sidebar.multiselect(
    "Product Category",
    options=categories,
    default=categories
)

# Shopping mall filter
malls = df["shopping_mall"].dropna().unique().tolist()
selected_malls = st.sidebar.multiselect(
    "Shopping Mall",
    options=malls,
    default=malls
)

# Payment method filter
payments = df["payment_method"].dropna().unique().tolist()
selected_payments = st.sidebar.multiselect(
    "Payment Method",
    options=payments,
    default=payments
)

# Apply filters
start_date, end_date = date_range
mask = (
    (df["invoice_date"].dt.date >= start_date) &
    (df["invoice_date"].dt.date <= end_date) &
    (df["gender"].isin(selected_genders)) &
    (df["category"].isin(selected_categories)) &
    (df["shopping_mall"].isin(selected_malls)) &
    (df["payment_method"].isin(selected_payments))
)

filtered_df = df[mask].copy()

# ---------------------- HEADER --------------------------- #
st.title("🛒 E-Commerce Sales Dashboard")
st.subheader("Customer Shopping Data Analysis – Bhavya Sri")

st.markdown(
    """
This dashboard provides an overview of **sales performance**, **customer behaviour**,  
and **shopping trends** based on the E-commerce sales dataset.
"""
)

# ---------------------- KPI CARDS ------------------------ #
total_revenue = filtered_df["Total_Amount"].sum()
total_orders = filtered_df["invoice_no"].nunique()
total_customers = filtered_df["customer_id"].nunique()
avg_order_value = total_revenue / total_orders if total_orders > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Unique Customers", f"{total_customers:,}")
col4.metric("Avg. Order Value", f"${avg_order_value:,.2f}")

st.markdown("---")

# ---------------------- ROW 1: TIME & CATEGORY ----------- #
left_col, right_col = st.columns(2)

with left_col:
    st.markdown("### 📈 Monthly Revenue Trend")
    monthly_sales = (
        filtered_df.groupby("Month")["Total_Amount"]
        .sum()
        .sort_index()
    )
    if not monthly_sales.empty:
        st.line_chart(monthly_sales)
    else:
        st.info("No data available for the selected filters.")

with right_col:
    st.markdown("### 🧺 Revenue by Category")
    category_sales = (
        filtered_df.groupby("category")["Total_Amount"]
        .sum()
        .sort_values(ascending=False)
    )
    if not category_sales.empty:
        st.bar_chart(category_sales)
    else:
        st.info("No data available for the selected filters.")

st.markdown("---")

# ---------------------- ROW 2: MALL & PAYMENT ------------ #
left_col2, right_col2 = st.columns(2)

with left_col2:
    st.markdown("### 🏬 Revenue by Shopping Mall")
    mall_sales = (
        filtered_df.groupby("shopping_mall")["Total_Amount"]
        .sum()
        .sort_values(ascending=False)
    )
    if not mall_sales.empty:
        st.bar_chart(mall_sales)
    else:
        st.info("No data available for the selected filters.")

with right_col2:
    st.markdown("### 💳 Orders by Payment Method")
    payment_counts = (
        filtered_df["payment_method"]
        .value_counts()
        .sort_values(ascending=False)
    )
    if not payment_counts.empty:
        st.bar_chart(payment_counts)
    else:
        st.info("No data available for the selected filters.")

st.markdown("---")

# ---------------------- ROW 3: CUSTOMER & AGE ------------ #
c1, c2 = st.columns(2)

with c1:
    st.markdown("### 👤 Top 10 Customers by Revenue")
    top_customers = (
        filtered_df.groupby("customer_id")["Total_Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    if not top_customers.empty:
        st.bar_chart(top_customers)
    else:
        st.info("No data available for the selected filters.")

with c2:
    st.markdown("### 👥 Age Distribution of Customers")
    if not filtered_df.empty:
        st.histogram(filtered_df, x="age", use_container_width=True)
    else:
        st.info("No data available for the selected filters.")

st.markdown("---")

# ---------------------- DATA TABLE ----------------------- #
st.markdown("### 📄 Filtered Transaction Details")
st.dataframe(
    filtered_df[
        [
            "invoice_no",
            "invoice_date",
            "customer_id",
            "gender",
            "age",
            "category",
            "quantity",
            "price",
            "Total_Amount",
            "payment_method",
            "shopping_mall",
        ]
    ].sort_values(by="invoice_date", ascending=False),
    use_container_width=True,
    hide_index=True
)

st.caption("Dashboard built with Streamlit & Python – E-Commerce Sales Analysis.")
