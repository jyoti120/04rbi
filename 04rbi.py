import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="RBI Dashboard")

# Title
st.title("RBI Monetary Policy & Financial Market Dashboard")
st.write("Graph-based dashboard project (No research, only visuals)")

# Data
data = {
    "Year": ["2019", "2020", "2021", "2022", "2023", "2024"],
    "Repo Rate (%)": [6.25, 4.00, 4.00, 6.50, 6.50, 6.50],
    "G-Sec Yield (%)": [7.4, 6.0, 6.2, 7.3, 7.2, 7.1],
    "Equity Index": [36000, 38000, 52000, 61000, 65000, 72000]
}

df = pd.DataFrame(data)
df = df.set_index("Year")

# Show data
st.subheader("Data Overview")
st.dataframe(df)

# Repo Rate Chart
st.subheader("Repo Rate Trend")
st.line_chart(df["Repo Rate (%)"])
st.write("Repo rate reflects RBI monetary policy stance.")

# G-Sec Yield Chart
st.subheader("Government Bond Yield Trend")
st.line_chart(df["G-Sec Yield (%)"])
st.write("Bond yields react quickly to RBI policy signals.")

# Equity Market Chart
st.subheader("Equity Market Movement")
st.line_chart(df["Equity Index"])
st.write("Equity markets respond to liquidity and interest rate expectations.")

# Key Insights
st.subheader("Key Insights")
st.write("• Repo rate directly impacts bond yields")
st.write("• Debt market reacts faster than equity market")
st.write("• Stable policy improves investor confidence")

# Footer
st.caption("Dashboard Project | RBI Summer Internship | MMS (GFM)")
