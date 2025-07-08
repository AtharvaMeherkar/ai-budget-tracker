import streamlit as st
import pandas as pd
from utils import load_data

st.set_page_config(page_title="AI Advisor", page_icon="🤖")

# Initialize session state from the CSV file if it's not already loaded
if 'transactions' not in st.session_state:
    st.session_state.transactions = load_data()

st.sidebar.title("💰 AI Budget Tracker")
st.sidebar.markdown("---")
st.title("🤖 AI Financial Advisor")
st.write("Get personalized insights and tips based on your spending habits.")

transactions_df = st.session_state.transactions

# Check for a minimum number of expenses to start analysis
if transactions_df.empty or len(transactions_df[transactions_df['type'] == 'Expense']) < 2:
    st.info("Not enough data for analysis. Please add at least a few expense transactions first.")
else:
    st.subheader("Spending Analysis & Tips")
    
    expense_df = transactions_df[transactions_df['type'] == 'Expense'].copy()
    
    # --- 1. Highest Spending Category Insight ---
    top_category = expense_df.groupby('category')['amount'].sum().idxmax()
    top_category_amount = expense_df.groupby('category')['amount'].sum().max()
    st.warning(f"**Top Spending Category:** You've spent the most on **{top_category}** (${top_category_amount:,.2f}). Consider reviewing this category for potential savings.")

    # --- 2. Anomaly Detection Insight ---
    anomalies_found = False
    for category in expense_df['category'].unique():
        category_df = expense_df[expense_df['category'] == category]
        if len(category_df) > 2:
            mean = category_df['amount'].mean()
            std = category_df['amount'].std()
            if std > 0: # Avoid division by zero if all amounts are the same
                anomaly_threshold = mean + 2 * std
                anomalies = category_df[category_df['amount'] > anomaly_threshold]
                if not anomalies.empty:
                    anomalies_found = True
                    for index, row in anomalies.iterrows():
                        st.error(f"**Unusual Spending Alert:** A purchase of **${row['amount']:,.2f}** in **{row['category']}** on {row['date'].strftime('%Y-%m-%d')} is significantly higher than your average for this category.")
    if not anomalies_found:
        st.info("💡 **Tip:** Add at least 3 expenses with varying amounts in the same category to unlock **Unusual Spending Alerts**.")

    # --- 3. Monthly Spending Comparison Insight ---
    expense_df['month'] = expense_df['date'].dt.to_period('M')
    this_month = pd.to_datetime('today').to_period('M')
    last_month = this_month - 1
    
    spending_this_month = expense_df[expense_df['month'] == this_month]['amount'].sum()
    spending_last_month = expense_df[expense_df['month'] == last_month]['amount'].sum()

    monthly_insight_generated = False
    if spending_last_month > 0 and spending_this_month > 0:
        monthly_insight_generated = True
        percent_change = ((spending_this_month - spending_last_month) / spending_last_month) * 100
        if percent_change > 10:
             st.info(f"**Monthly Trend:** Your spending this month (${spending_this_month:,.2f}) is **{abs(percent_change):.0f}% higher** than last month (${spending_last_month:,.2f}).")
        elif percent_change < -10:
             st.success(f"**Great Job!** Your spending this month (${spending_this_month:,.2f}) is **{abs(percent_change):.0f}% lower** than last month (${spending_last_month:,.2f}). Keep it up!")
        else:
            monthly_insight_generated = False # Re-arm the tip if change is not significant
    
    if not monthly_insight_generated:
        st.info("💡 **Tip:** Add expenses from this month and last month to unlock your **Monthly Spending Trend**.")