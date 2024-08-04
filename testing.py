import streamlit as st
import pandas as pd
import os
from datetime import datetime
import pytz

# Custom CSS to style the buttons with images
st.markdown("""
    <style>
    .button-container {
        display: flex;
        justify-content: space-around;
    }
    .button img {
        width: 50px;
        height: 50px;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

# HTML and JavaScript for buttons with images
button_html = """
<div class="button-container">
    <div id="btn1">
        <img src="btn_prev.png" alt="Load Data">
    </div>
    <div id="btn2">
        <img src="btn_next.png" alt="Save Data">
    </div>
</div>
<script>
    document.getElementById('btn_prev.png').onclick = function() {
        window.parent.postMessage('btn1', '*');
    }
    document.getElementById('btn2_next.png').onclick = function() {
        window.parent.postMessage('btn2', '*');
    }
</script>
"""

# Display the HTML
st.markdown(button_html, unsafe_allow_html=True)

# Placeholder for button actions
action = st.empty()

# Function to handle button click messages from JavaScript
def process_js_data(data):
    if data == 'btn1':
        st.session_state.button_clicked = 'Load Data'
    elif data == 'btn2':
        st.session_state.button_clicked = 'Save Data'

# JS callback to handle messages from the buttons
st.markdown("""
    <script>
        window.addEventListener('message', function(event) {
            window.parent.streamlitRerun({
                button_clicked: event.data
            });
        });
    </script>
    """, unsafe_allow_html=True)

# Display messages based on button clicks
if 'button_clicked' in st.session_state:
    if st.session_state.button_clicked == 'Load Data':
        action.write('Load Data button clicked')
    elif st.session_state.button_clicked == 'Save Data':
        action.write('Save Data button clicked')
