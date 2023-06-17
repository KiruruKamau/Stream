import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Set the page title and layout
st.set_page_config(page_title='Data Visualization Tool', layout='wide')

# Add a title and description
st.title('Data Visualization Tool')
st.write('Upload your dataset and explore it with interactive visualizations.')

# Add file uploader for dataset
uploaded_file = st.file_uploader('Upload a dataset', type=['csv', 'xlsx'])

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the dataset into a pandas DataFrame
    df = pd.read_csv(uploaded_file)  # Use pd.read_excel() for Excel files

    # Display the dataset
    st.subheader('Dataset')
    st.write(df)

    # Allow users to select columns for visualization
    selected_columns = st.multiselect('Select columns for visualization', df.columns)

    # Generate visualizations based on user selection
    if len(selected_columns) > 0:
        st.subheader('Visualizations')

        # Reshape the data to long-form
        long_df = pd.melt(df, id_vars=[selected_columns[0]], value_vars=selected_columns[1:], var_name='Category', value_name='Value')

        # Example: Bar chart
        st.subheader('Bar Chart')
        fig_bar = px.bar(long_df, x=selected_columns[0], y='Value', color='Category')
        st.plotly_chart(fig_bar)

        # Example: Line chart
        st.subheader('Line Chart')
        fig_line = px.line(long_df, x=selected_columns[0], y='Value', color='Category')
        st.plotly_chart(fig_line)

        # Example: Scatter plot
        st.subheader('Scatter Plot')
        fig_scatter = px.scatter(long_df, x=selected_columns[0], y='Value', color='Category')
        st.plotly_chart(fig_scatter)