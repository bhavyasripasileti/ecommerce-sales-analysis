import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="E-Commerce Sales Analysis Dashboard",
    page_icon="🛒",
    layout="wide"
)

# ------------------ STYLE ------------------
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
}
h1, h2, h3 {
    color: #EAEAEA;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------ LOAD DATA ------------------
@st.cache_data
def load_data():
    df = pd.read_csv("customer_shopping_data.csv")
    df["invoice_date"] = pd.to_datetime(df["invoice_date"], dayfirst=True)
    df["Month"] = df["invoice_date"].dt.to_period("M").astype(str)
    df["Total_Amount"] = df["quantity"] * df["price"]

    bins = [10, 20, 30, 40, 50, 60, 70, 80]
    labels = ["10–19", "20–29", "30–39", "40–49", "50–59", "60–69", "70–79"]
    df["Age_Group"] = pd.cut(df["age"], bins=bins, labels=labels, right=False)

    return df

df = load_data()

# ------------------ HEADER ------------------
st.title("🛒 E-Commerce Sales Analysis Dashboard")
st.caption("Analyze revenue trends, customer behavior, and business insights")

# ------------------ SIDEBAR ------------------
st.sidebar.header("🔎 Filters")

selected_gender = st.sidebar.multiselect(
    "Gender",
    df["gender"].unique(),
    default=df["gender"].unique()
)

selected_category = st.sidebar.multiselect(
    "Category",
    df["category"].unique(),
    default=df["category"].unique()
)

selected_mall = st.sidebar.multiselect(
    "Shopping Mall",
    df["shopping_mall"].unique(),
    default=df["shopping_mall"].unique()
)

filtered_df = df[
    (df["gender"].isin(selected_gender)) &
    (df["category"].isin(selected_category)) &
    (df["shopping_mall"].isin(selected_mall))
]

# ------------------ KPI CARDS ------------------
st.markdown("## 📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"### 💰 Revenue\n<h2 style='color:#00FF9C'>₹ {filtered_df['Total_Amount'].sum():,.0f}</h2>", unsafe_allow_html=True)

col2.markdown(f"### 👥 Customers\n<h2 style='color:#00C4FF'>{filtered_df['customer_id'].nunique()}</h2>", unsafe_allow_html=True)

col3.markdown(f"### 🧾 Orders\n<h2 style='color:#FFA500'>{filtered_df['invoice_no'].nunique()}</h2>", unsafe_allow_html=True)

col4.markdown(f"### 📦 Avg Order Value\n<h2 style='color:#FF4B4B'>₹ {filtered_df['Total_Amount'].mean():,.0f}</h2>", unsafe_allow_html=True)

st.markdown("---")

# ------------------ CHARTS ROW 1 ------------------
col5, col6 = st.columns(2)

sales_by_category = filtered_df.groupby("category")["Total_Amount"].sum().reset_index()
fig_cat = px.bar(
    sales_by_category,
    x="category",
    y="Total_Amount",
    color="category",
    text_auto=True
)
fig_cat.update_layout(template="plotly_dark")

col5.plotly_chart(fig_cat, use_container_width=True)

sales_by_gender = filtered_df.groupby("gender")["Total_Amount"].sum().reset_index()
fig_gender = px.pie(
    sales_by_gender,
    names="gender",
    values="Total_Amount",
    hole=0.5
)
fig_gender.update_layout(template="plotly_dark")

col6.plotly_chart(fig_gender, use_container_width=True)

st.info("📌 Insight: Category contribution and gender distribution highlight key revenue drivers.")

st.markdown("---")

# ------------------ CHARTS ROW 2 ------------------
col7, col8 = st.columns(2)

monthly_sales = filtered_df.groupby("Month")["Total_Amount"].sum().reset_index()
fig_month = px.line(
    monthly_sales,
    x="Month",
    y="Total_Amount",
    markers=True
)
fig_month.update_layout(template="plotly_dark")

col7.plotly_chart(fig_month, use_container_width=True)

age_group_df = (
    filtered_df.groupby("Age_Group")["customer_id"]
    .nunique()
    .reset_index(name="Customers")
    .dropna()
)

fig_age = px.bar(
    age_group_df,
    x="Age_Group",
    y="Customers",
    text="Customers"
)
fig_age.update_layout(template="plotly_dark")

col8.plotly_chart(fig_age, use_container_width=True)

st.info("📌 Insight: Younger age groups and seasonal trends impact revenue significantly.")

st.markdown("---")

# ------------------ TOP MALLS ------------------
st.markdown("## 🏬 Top Performing Shopping Malls")

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
    color="shopping_mall",
    text_auto=True
)
fig_mall.update_layout(template="plotly_dark")

st.plotly_chart(fig_mall, use_container_width=True)

st.markdown("---")

# ------------------ DOWNLOAD + DATA ------------------
st.markdown("## 📥 Data Export")

st.download_button(
    "Download Filtered Data",
    filtered_df.to_csv(index=False),
    file_name="filtered_data.csv"
)

st.markdown("## 🔍 Data Preview")
st.dataframe(filtered_df.head(50), use_container_width=True)
