import streamlit as st
import pandas as pd

# Custom CSS for a subtle and beautiful design
st.markdown(
    """
    <style>
    .main {
        background-color: #f9f9f9;
        padding: 30px;
        text-align: center;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #2c3e50;
        font-family: 'Arial', sans-serif;
        font-size: 32px;
        margin-bottom: 20px;
    }
    .stSelectbox {
        width: 300px;
        margin: 10px auto;
        text-align: center;
        background-color: #ffffff;
        border-radius: 5px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }
    .stText {
        color: #27ae60;
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define stocks and dates
stocks = ['RELIANCE', 'HDFCBANK', 'ICICIBANK', 'INFY', 'TCS']
future_dates = pd.date_range(start='2025-06-13', periods=22, freq='B').strftime('%Y-%m-%d').tolist()

# Load precomputed predictions
predictions = {
    'RELIANCE': [1438.690434, 1447.046401, 1436.264765, 1437.149944, 1438.160256, 1438.877766, 1444.614008, 1437.406409, 1431.554951, 1440.219828, 1438.448668, 1446.167533, 1436.500326, 1434.692084, 1438.854986, 1438.995828, 1445.057514, 1437.285285, 1432.789711, 1439.868615, 1438.392568, 1445.942226],
    'HDFCBANK': [1946.625004, 1954.019765, 1942.101563, 1947.857501, 1944.981739, 1943.894790, 1950.622123, 1944.729626, 1947.179219, 1944.204244, 1945.236812, 1952.292215, 1943.437816, 1947.512625, 1944.586417, 1944.577148, 1951.471291, 1944.072798, 1947.348741, 1944.398562, 1944.901402, 1951.874812],
    'ICICIBANK': [1429.361114, 1424.800606, 1427.351535, 1427.940558, 1428.644573, 1431.576050, 1422.649018, 1426.910693, 1428.317835, 1426.905951, 1430.458077, 1423.735016, 1427.133205, 1428.127407, 1427.783508, 1431.022366, 1423.186866, 1427.020894, 1428.223524, 1427.340567, 1430.737545, 1423.463541],
    'INFY': [1615.041577, 1611.288854, 1607.057506, 1612.987025, 1607.288748, 1615.808006, 1607.197337, 1608.308787, 1615.077027, 1607.948093, 1615.422618, 1609.254700, 1607.679597, 1614.026098, 1607.616550, 1615.616405, 1608.220183, 1607.995977, 1614.554543, 1607.783262, 1615.518962, 1608.740376],
    'TCS': [3432.757760, 3442.638501, 3420.512619, 3437.855403, 3433.341205, 3436.502533, 3439.150586, 3426.492284, 3438.226871, 3433.746202, 3434.742168, 3440.789895, 3423.682364, 3438.052452, 3433.555838, 3435.569354, 3440.019606, 3425.002683, 3438.134401, 3433.645288, 3435.180679, 3440.381546]
}

# Header
st.markdown("<h1>Nifty 50 Stocks Price Prediction by SAIF LATIF</h1>", unsafe_allow_html=True)

# Dropdowns for user input
selected_stock = st.selectbox("Select a Stock", stocks)
selected_date = st.selectbox("Select a Date", future_dates)

# Get the predicted price
if selected_stock and selected_date:
    date_index = future_dates.index(selected_date)
    predicted_price = predictions[selected_stock][date_index]
    st.markdown(f"<p class='stText'>Predicted Price: {predicted_price:.2f} INR</p>", unsafe_allow_html=True)