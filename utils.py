import pandas as pd
import streamlit as st

def load_data():
    """Load transaction data from a CSV file."""
    try:
        df = pd.read_csv('transactions.csv', parse_dates=['date'])
    except FileNotFoundError:
        return pd.DataFrame(columns=['date', 'type', 'category', 'amount', 'description'])
    return df

def save_data():
    """Save the current session state DataFrame to the CSV file."""
    if 'transactions' in st.session_state:
        st.session_state.transactions.to_csv('transactions.csv', index=False)

def load_css(file_name):
    """Function to load local CSS file."""
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)