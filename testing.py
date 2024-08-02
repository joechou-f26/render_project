import streamlit as st
import pandas as pd

# Initialize session state
if 'data' not in st.session_state:
    st.session_state['data'] = []

# Function to add data
def add_data():
    st.session_state['data'].append(st.session_state.input_data)

# Function to save data to CSV
def save_data():
    df = pd.DataFrame(st.session_state['data'], columns=['Data'])
    df.to_csv('data.csv', index=False)
    st.success("Data saved to data.csv")
 
# Display input field and buttons
st.text_input("Enter data", key="input_data")
if st.button("Add Data"):
    add_data()
if st.button("Save Data"):
    save_data()

# Display stored data
st.write("Stored data:", st.session_state['data'])

df = pd.read_csv("data.csv")

@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)
st.download_button(
   "Press to Download",
   csv,
   "data.csv",
   "text/csv",
   key='download-csv'
)


