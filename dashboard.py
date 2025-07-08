import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, load_css

st.set_page_config(page_title="Dashboard", page_icon="💰", layout="wide")

# Initialize session state
if 'transactions' not in st.session_state:
    st.session_state.transactions = load_data()

# Load CSS and get data from session state
load_css("style.css")
transactions_df = st.session_state.transactions

# --- Sidebar ---
st.sidebar.title("💰 AI Budget Tracker")
st.sidebar.markdown("---")

# --- Main Page Content ---
st.title("Financial Dashboard")
st.write("An overview of your income and expenses.")

if transactions_df.empty:
    st.info("No transactions yet. Add your first transaction from the 'Add Transaction' page.")
else:
    # --- Dashboard Metrics ---
    st.header("📊 Key Metrics")
    total_income = transactions_df[transactions_df['type'] == 'Income']['amount'].sum()
    total_expense = transactions_df[transactions_df['type'] == 'Expense']['amount'].sum()
    net_balance = total_income - total_expense

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"${total_income:,.2f}")
    col2.metric("Total Expenses", f"${total_expense:,.2f}")
    col3.metric("Current Balance", f"${net_balance:,.2f}")

    st.markdown("---")

    # --- Charts ---
    st.header("Visualizations")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Spending by Category")
        expense_df = transactions_df[transactions_df['type'] == 'Expense']
        if not expense_df.empty:
            category_spending = expense_df.groupby('category')['amount'].sum().sort_values(ascending=False)
            fig_pie = px.pie(category_spending, values='amount', names=category_spending.index, hole=.4)
            fig_pie.update_traces(textposition='inside', textinfo='percent+label', showlegend=False)
            st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.info("No expense data for pie chart.")

    with col2:
        st.subheader("Income vs. Expense Trend")
        monthly_summary = transactions_df.copy()
        monthly_summary['month'] = monthly_summary['date'].dt.to_period('M').astype(str)
        monthly_summary = monthly_summary.groupby(['month', 'type'])['amount'].sum().unstack().fillna(0)
        
        if not monthly_summary.empty:
            fig_area = px.area(monthly_summary, x=monthly_summary.index, y=['Income', 'Expense'],
                               labels={"value": "Amount ($)", "date": "Month", "variable": "Transaction Type"},
                               color_discrete_map={"Income": "rgba(0, 163, 108, 0.6)", "Expense": "rgba(210, 43, 43, 0.6)"})
            st.plotly_chart(fig_area, use_container_width=True)
        else:
            st.info("Not enough data for trend chart.")