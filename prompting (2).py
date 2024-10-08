import streamlit as st
import pandas as pd
# Title of the app
st.title('Interactive Sales Data Visualization App')

# Pre-loaded dataset for sales information
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'Sales (Thousands USD)': [150, 200, 300, 400, 250],
    'Quantity Sold': [30, 45, 55, 65, 50]
}
df = pd.DataFrame(data)

# Display the dataset
st.write("Sales Data:")
st.write(df)

# Let the user select columns for the chart
columns = df.columns.tolist()

# Dropdowns for X and Y axes selection
x_axis = st.selectbox('Select column for X-axis', columns)
y_axis = st.selectbox('Select column for Y-axis', columns)

# Choose chart type: Bar Chart or Line Chart
chart_type = st.selectbox('Select chart type', ['Bar Chart', 'Line Chart'])

# Display chart based on user selections
if chart_type == 'Bar Chart':
    st.bar_chart(df[[x_axis, y_axis]].set_index(x_axis))
elif chart_type == 'Line Chart':
    st.line_chart(df[[x_axis, y_axis]].set_index(x_axis))

