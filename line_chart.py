
# Important libraries
import streamlit as st
import pandas as pd
import numpy as np

# Header text
st.header('Line chart')

# Creating data frame with random values
chart_data = pd.DataFrame(
     np.random.randn(10, 4),
     columns=['a', 'b', 'c','d'])

# Creating line chart using data frame data
st.line_chart(chart_data)