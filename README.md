# Market-Sentiment-Trader-Performance
Predictive analysis and interactive dashboard for trader performance based on market sentiment.
## Project Goals
* **Analyze:** Relationship between market "mood" and daily PnL.
* **Cluster:** Segment traders into behavioral archetypes (Scalpers, Retail, Whales).
* **Predict:** Forecast next-day PnL volatility using sentiment scores.
* **Visualize:** Build an interactive Streamlit dashboard for data exploration.

## Methodology & Clustering
I used **K-Means Clustering** to segment the trading community into three distinct groups:
1. **High-Volume Scalpers:** High trade counts, consistent but smaller individual profits.
2. **Casual/Retail:** Low frequency, high sensitivity to market "Fear."
3. **Consistent Pros:** High win rates and steady performance regardless of market regime.

## How to Run
1. **Install Dependencies:**
   ```bash
   pip install streamlit pandas plotly scikit-learn
