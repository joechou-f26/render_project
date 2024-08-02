import streamlit as st
import pandas as pd
import os
from datetime import datetime
import pytz


# Initialize session state
if 'data' not in st.session_state:
    st.session_state['data'] = []

def load_review_data():
    gmt8 = pytz.timezone('Asia/Taipei')
    current_datetime_gmt8 = datetime.now(gmt8)
    st.write("Current date and time in GMT+8:", current_datetime_gmt8)
    
    try:                  
        df = pd.read_csv('/mount/src/peer_review/review_data.csv')
        st.table(df)
        return df
    except FileNotFoundError:
        st.error("File not found. Please check the file path.")
    except PermissionError:
        st.error("Permission denied. Please check the file permissions.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
    
# Function to add data
def add_data():
    st.session_state['data'].append(st.session_state.input_data)

# Function to save data to CSV
def save_data():
    df = pd.DataFrame(st.session_state['data'], columns=['Data'])
    file_path = os.path.join(os.getcwd(), 'data.csv')
    df.to_csv(file_path, index=False)
    st.session_state['file_path'] = file_path
    st.success(f"Data saved to {file_path}")

# Function to provide download link
def download_link():
    if 'file_path' in st.session_state and os.path.exists(st.session_state['file_path']):
        with open(st.session_state['file_path'], 'rb') as f:
            st.download_button(
                label="Download Raw Data",
                data=f,
                file_name='data.csv',
                mime='text/csv'
            )
    else:
        st.warning("No file to download. Please save data first.")

# Display current working directory
st.write(f"Current working directory: {os.getcwd()}")

# Display input field and buttons
st.text_input("Enter filename", key="input_data")
if st.button("Add Data"):
    add_data()
if st.button("Save Data"):
    save_data()
if st.button("Load review_data.csv"):
    load_review_data()
    
    
# Display stored data
st.write("Stored data:", st.session_state['data'])

# Provide download link
download_link()
