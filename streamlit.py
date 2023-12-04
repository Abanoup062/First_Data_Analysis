import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="First Project", layout="wide")

# Loading data
st.title('Macrodata')
data = pd.read_csv('macrodata.csv')
st.write(data.head())

def plot_chart(selected_chart):
    fig, ax = plt.subplots(figsize=(8, 6))
    if selected_chart == 'Line Chart':
        ax.plot(data['year'], data['cpi'])
        ax.set_xlabel('year')
        ax.set_ylabel('cpi')
        ax.set_title('Line Chart')

    elif selected_chart == 'Bar Chart':
        ax.bar(data['year'], data['cpi'])
        ax.set_xlabel('year')
        ax.set_ylabel('cpi')
        ax.set_title('Bar Chart')

    elif selected_chart == 'Scatter Plot':
        ax.scatter(data['year'], data['cpi'])
        ax.set_xlabel('year')
        ax.set_ylabel('cpi')
        ax.set_title('Scatter Plot')

    elif selected_chart == 'Histogram':
        ax.hist(data['year'], bins=100)
        ax.set_xlabel('cpi')
        ax.set_ylabel('Frequency')
        ax.set_title('Histogram')

    st.pyplot(fig)

def main():
    # Dropdown to select chart type
    selected_chart = st.selectbox('Select Chart Type:', ['Line Chart', 'Bar Chart', 'Scatter Plot', 'Histogram'])

    # Button to plot chart
    if st.button('Plot Chart'):
        plot_chart(selected_chart)

    st.sidebar.header('Filter Data Based on Year and Quarter')

    # Filter data function
    def filter_data(year, quarter):
        filtered_data = data[(data['year'] == year) & (data['quarter'] == quarter)]
        return filtered_data

    # Slider to select values for filtering
    selected_year = st.sidebar.slider('Select value for Year:', 1959, 2009)
    selected_quarter = st.sidebar.slider('Select value for Quarter:', 1, 4)

    # Button to trigger filtering
    if st.sidebar.button('Filter Data'):
        filtered_result = filter_data(selected_year, selected_quarter)
        st.write("Filtered Result:")
        st.write(filtered_result)

if __name__ == '__main__':
    main()
