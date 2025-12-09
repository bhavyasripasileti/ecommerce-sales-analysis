import streamlit as st
import pandas as pd

st.set_page_config(page_title="E-Commerce Sales Analysis", layout="wide")

st.title("🛒 E-Commerce Sales Dashboard")
st.write("Industry Internship Project | Bhavya Sri")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/customer_shopping_data.csv")
    return df

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"{(df['price'] * df['quantity']).sum():,.0f}")
col2.metric("Total Orders", df['invoice_no'].nunique())
col3.metric("Total Customers", df['customer_id'].nunique())

st.subheader("Sales by Category")
category_sales = df.groupby("category")["quantity"].sum()
st.bar_chart(category_sales)

st.subheader("Sales by Payment Method")
payment_sales = df["payment_method"].value_counts()
st.bar_chart(payment_sales)

st.info("For detailed visual analytics, view Tableau Dashboard (attached in GitHub).")
