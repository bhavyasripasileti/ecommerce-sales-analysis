import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("customer_shopping_data.csv")
    df["invoice_date"] = pd.to_datetime(df["invoice_date"], dayfirst=True)
    df["Month"] = df["invoice_date"].dt.to_period("M").astype(str)
    df["Total_Amount"] = df["quantity"] * df["price"]
    return df

df = load_data()

st.title("🛒 E-Commerce Sales Dashboard")
st.markdown("Industry Internship Project | Bhavya Sri")

st.sidebar.header("Filters")

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    df["gender"].unique(),
    default=df["gender"].unique()
)

selected_category = st.sidebar.multiselect(
    "Select Category",
    df["category"].unique(),
    default=df["category"].unique()
)

selected_mall = st.sidebar.multiselect(
    "Select Shopping Mall",
    df["shopping_mall"].unique(),
    default=df["shopping_mall"].unique()
)

filtered_df = df[
    (df["gender"].isin(selected_gender)) &
    (df["category"].isin(selected_category)) &
    (df["shopping_mall"].isin(selected_mall))
]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"₹ {filtered_df['Total_Amount'].sum():,.0f}")
col2.metric("Total Customers", filtered_df["customer_id"].nunique())
col3.metric("Total Orders", filtered_df["invoice_no"].nunique())
col4.metric("Avg Order Value", f"₹ {filtered_df['Total_Amount'].mean():,.0f}")

st.divider()

col5, col6 = st.columns(2)

sales_by_category = filtered_df.groupby("category")["Total_Amount"].sum().reset_index()
fig_cat = px.bar(
    sales_by_category,
    x="category",
    y="Total_Amount",
    title="Revenue by Category",
    color="category"
)
col5.plotly_chart(fig_cat, use_container_width=True)

sales_by_gender = filtered_df.groupby("gender")["Total_Amount"].sum().reset_index()
fig_gender = px.pie(
    sales_by_gender,
    names="gender",
    values="Total_Amount",
    title="Revenue Share by Gender"
)
col6.plotly_chart(fig_gender, use_container_width=True)

st.divider()

col7, col8 = st.columns(2)

monthly_sales = filtered_df.groupby("Month")["Total_Amount"].sum().reset_index()
fig_month = px.line(
    monthly_sales,
    x="Month",
    y="Total_Amount",
    title="Monthly Sales Trend",
    markers=True
)
col7.plotly_chart(fig_month, use_container_width=True)

fig_age = px.plotly_chart(
    filtered_df,
    x="age",
    nbins=20,
    title="Customer Age Distribution"
)
col8.plotly_chart(fig_age, use_container_width=True)

st.divider()

top_malls = (
    filtered_df.groupby("shopping_mall")["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_mall = px.bar(
    top_malls,
    x="shopping_mall",
    y="Total_Amount",
    title="Top Shopping Malls by Revenue",
    color="shopping_mall"
)

st.plotly_chart(fig_mall, use_container_width=True)

st.divider()

st.subheader("Filtered Dataset Preview")
st.dataframe(filtered_df.head(50), use_container_width=True)
