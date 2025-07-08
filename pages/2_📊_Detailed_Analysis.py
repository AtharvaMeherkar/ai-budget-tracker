import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from utils import load_data

st.set_page_config(page_title="Detailed Analysis", page_icon="📊")

# Initialize session state
if 'transactions' not in st.session_state:
    st.session_state.transactions = load_data()

st.sidebar.title("💰 AI Budget Tracker")
st.sidebar.markdown("---")
st.title("📊 Detailed Financial Analysis")

transactions_df = st.session_state.transactions

if transactions_df.empty:
    st.info("No data available. Please add transactions to see the analysis.")
else:
    st.subheader("Financial Flow (Sankey Diagram)")
    
    income_df = transactions_df[transactions_df['type'] == 'Income']
    expense_df = transactions_df[transactions_df['type'] == 'Expense']

    if not income_df.empty and not expense_df.empty:
        # Prepare data for Sankey chart
        income_sources = income_df['category'].unique()
        expense_categories = expense_df['category'].unique()
        
        all_nodes = list(income_sources) + ['Total Income'] + list(expense_categories)
        node_map = {node: i for i, node in enumerate(all_nodes)}

        sources = []
        targets = []
        values = []

        # Flow from income sources to 'Total Income' node
        for category in income_sources:
            amount = income_df[income_df['category'] == category]['amount'].sum()
            sources.append(node_map[category])
            targets.append(node_map['Total Income'])
            values.append(amount)

        # Flow from 'Total Income' node to expense categories
        for category in expense_categories:
            amount = expense_df[expense_df['category'] == category]['amount'].sum()
            sources.append(node_map['Total Income'])
            targets.append(node_map[category])
            values.append(amount)

        # Create Sankey Diagram
        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=25,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=all_nodes,
                color=px.colors.qualitative.Plotly
            ),
            link=dict(
                source=sources,
                target=targets,
                value=values
            ))])

        fig.update_layout(title_text="Income to Expense Flow", font_size=12)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Please add at least one income AND one expense to view the financial flow chart.")