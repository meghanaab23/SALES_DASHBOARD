import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Data Dashboard")

df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

st.sidebar.header("Filter Data")

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[df["Category"].isin(category)]

total_sales = filtered_df["Sales"].sum()
avg_sales = filtered_df["Sales"].mean()

col1, col2 = st.columns(2)
col1.metric("💰 Total Sales", total_sales)
col2.metric("📊 Average Sales", round(avg_sales, 2))

st.subheader("📈 Sales Over Time")

sales_by_date = filtered_df.groupby("Date")["Sales"].sum()

fig1, ax1 = plt.subplots()
ax1.plot(sales_by_date.index, sales_by_date.values, marker='o')
ax1.set_xlabel("Date")
ax1.set_ylabel("Sales")
ax1.set_title("Sales Trend")

st.pyplot(fig1)

st.subheader("📊 Sales by Category")

sales_by_category = filtered_df.groupby("Category")["Sales"].sum()

fig2, ax2 = plt.subplots()
ax2.bar(sales_by_category.index, sales_by_category.values)
ax2.set_xlabel("Category")
ax2.set_ylabel("Sales")
ax2.set_title("Category-wise Sales")

st.pyplot(fig2)

st.subheader("📄 Raw Data")
st.dataframe(filtered_df)
