import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Trading Dashboard", layout="wide")

# 1. Load the data exported from Colab
df = pd.read_csv('master_df.csv')
profiles = pd.read_csv('trader_profiles.csv')

st.title("📊 Market Sentiment & Trader Performance")

# 2. Sidebar Filters
sentiment = st.sidebar.multiselect("Select Market Sentiment", options=df['regime'].unique(), default='Fear')
filtered_df = df[df['regime'].isin(sentiment)]

# 3. Simple Predictive Logic
st.subheader("🔮 Next-Day Risk Predictor")
score = st.slider("Current Fear/Greed Score", 0, 100, 50)
# Simple rule of thumb based on your analysis: Fear increases risk
predicted_risk = (100 - score) * 250 
st.write(f"Estimated Next-Day Risk (Volatility): **{predicted_risk:,.0f}**")

# 4. Clustering Chart
st.subheader("👥 Trader Behavioral Archetypes")
fig = px.scatter(profiles, x="trade_count", y="daily_pnl", color="Archetype", size="win_rate",
                 title="Activity vs. Profitability by Group")
st.plotly_chart(fig, use_container_width=True)

# 5. Performance Chart
st.subheader("📈 Profit Distribution")
fig2 = px.box(filtered_df, x="regime", y="daily_pnl", color="regime")
st.plotly_chart(fig2, use_container_width=True)