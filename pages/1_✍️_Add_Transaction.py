import streamlit as st
import pandas as pd
from datetime import datetime
from utils import load_data, save_data

st.set_page_config(page_title="Add Transaction", page_icon="✍️")

# Initialize session state
if 'transactions' not in st.session_state:
    st.session_state.transactions = load_data()

def reset_data():
    st.session_state.transactions = pd.DataFrame(columns=['date', 'type', 'category', 'amount', 'description'])
    save_data()
    st.success("All transactions have been reset!")

st.sidebar.title("💰 AI Budget Tracker")
st.sidebar.markdown("---")
st.title("✍️ Add New Transaction")

with st.form("transaction_form"):
    st.subheader("Enter Transaction Details")
    col1, col2 = st.columns(2)
    with col1:
        transaction_date = st.date_input("Date", datetime.now())
        transaction_type = st.selectbox("Type", ["Expense", "Income"], key="transaction_type")
        transaction_amount = st.number_input("Amount", min_value=0.01, format="%.2f")
    with col2:
        if st.session_state.get('transaction_type', 'Expense') == "Expense":
            categories = ["Food", "Transport", "Bills", "Shopping", "Entertainment", "Health", "Other"]
        else:
            categories = ["Salary", "Bonus", "Gifts", "Other Income"]
        transaction_category = st.selectbox("Category", categories)
        transaction_description = st.text_input("Description (Optional)")

    if st.form_submit_button("Add Transaction", type="primary"):
        if transaction_amount > 0:
            new_transaction = pd.DataFrame([{"date": pd.to_datetime(transaction_date), "type": transaction_type, "category": transaction_category, "amount": transaction_amount, "description": transaction_description}])
            st.session_state.transactions = pd.concat([st.session_state.transactions, new_transaction], ignore_index=True)
            save_data()
            st.success("Transaction added successfully!")
        else:
            st.error("Amount must be greater than zero.")

st.markdown("---")
st.subheader("Current Transactions")
st.dataframe(st.session_state.transactions.sort_values(by="date", ascending=False), use_container_width=True, hide_index=True)

st.markdown("---")
st.subheader("Settings")

if 'confirm_reset' not in st.session_state:
    st.session_state.confirm_reset = False
if st.button("🚨 Reset All Transactions"):
    st.session_state.confirm_reset = True
if st.session_state.confirm_reset:
    st.warning("Are you sure? This will delete all transactions permanently.")
    c1, c2 = st.columns(2)
    if c1.button("✅ Yes, I'm sure", type="primary"):
        reset_data()
        st.session_state.confirm_reset = False
        st.rerun()
    if c2.button("Cancel"):
        st.session_state.confirm_reset = False
        st.rerun()