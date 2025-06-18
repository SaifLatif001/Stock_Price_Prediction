import streamlit as st
import pandas as pd

# Define stocks and dates
stocks = ['RELIANCE', 'HDFCBANK', 'ICICIBANK', 'INFY', 'TCS']
future_dates = pd.date_range(start='2025-06-13', periods=22, freq='B').strftime('%Y-%m-%d').tolist()

# Load precomputed predictions (manually input from Jupyter output)
predictions = {
    'RELIANCE': [1438.690434, 1447.046401, 1436.264765, 1437.149944, 1438.160256, 1438.877766, 1444.614008, 1437.406409, 1431.554951, 1440.219828, 1438.448668, 1446.167533, 1436.500326, 1434.692084, 1438.854986, 1438.995828, 1445.057514, 1437.285285, 1432.789711, 1439.868615, 1438.392568, 1445.942226],
    'HDFCBANK': [1946.625004, 1954.019765, 1942.101563, 1947.857501, 1944.981739, 1943.894790, 1950.622123, 1944.729626, 1947.179219, 1944.204244, 1945.236812, 1952.292215, 1943.437816, 1947.512625, 1944.586417, 1944.577148, 1951.471291, 1944.072798, 1947.348741, 1944.398562, 1944.901402, 1951.874812],
    'ICICIBANK': [1429.361114, 1424.800606, 1427.351535, 1427.940558, 1428.644573, 1431.576050, 1422.649018, 1426.910693, 1428.317835, 1426.905951, 1430.458077, 1423.735016, 1427.133205, 1428.127407, 1427.783508, 1431.022366, 1423.186866, 1427.020894, 1428.223524, 1427.340567, 1430.737545, 1423.463541],
    'INFY': [1615.041577, 1611.288854, 1607.057506, 1612.987025, 1607.288748, 1615.808006, 1607.197337, 1608.308787, 1615.077027, 1607.948093, 1615.422618, 1609.254700, 1607.679597, 1614.026098, 1607.616550, 1615.616405, 1608.220183, 1607.995977, 1614.554543, 1607.783262, 1615.518962, 1608.740376],
    'TCS': [3432.757760, 3442.638501, 3420.512619, 3437.855403, 3433.341205, 3436.502533, 3439.150586, 3426.492284, 3438.226871, 3433.746202, 3434.742168, 3440.789895, 3423.682364, 3438.052452, 3433.555838, 3435.569354, 3440.019606, 3425.002683, 3438.134401, 3433.645288, 3435.180679, 3440.381546]
}

# Title of the app
st.title("Stock Price Prediction for Nifty 50 Stocks (June 13 - July 12, 2025)")

# Sidebar for user input
st.sidebar.header("Select Options")
selected_stock = st.sidebar.selectbox("Choose a Stock", stocks)
selected_date = st.sidebar.selectbox("Choose a Date", future_dates)

# Get the predicted price
date_index = future_dates.index(selected_date)
predicted_price = predictions[selected_stock][date_index]

# Display the result
st.write(f"## Predicted Price for {selected_stock} on {selected_date}")
st.write(f"**Predicted Price:** {predicted_price:.2f} INR")

# Debug: Verify predictions
st.write("### Debug: Full Predictions")
for stock in stocks:
    st.write(f"{stock}: {predictions[stock]}")

# Optional: Display full table for reference
prediction_df = pd.DataFrame(index=stocks, columns=future_dates)
for stock in stocks:
    prediction_df.loc[stock] = predictions[stock]
st.write("\n## Full Prediction Table (June 13 - July 12, 2025)")
st.table(prediction_df.round(2))

# Add a summary
st.write("\n## Summary of Predictions")
for stock in stocks:
    st.write(f"{stock}: {predictions[stock][:5]}... (22 total)")

# Final Report
st.write("\n## Final Report")
st.write("""
- **Selected Model**: SARIMAX with Exogenous Variables
- **Prediction Horizon**: June 13 - July 12, 2025 (22 business days)
- **Training Data**: Historical data up to June 12, 2025
- **Observations**: SARIMAX with open, high, low, volume covariates produces stable predictions close to last prices.
- **Limitations**: Simplified parameters may miss complex trends; accuracy to be validated post-July 2025.
- **Recommendations**: Use for short-term forecasting; consider AutoML for longer horizons if needed.
""")