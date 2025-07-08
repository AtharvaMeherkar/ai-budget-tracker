<div align="center">

<img src="https://raw.githubusercontent.com/streamlit/streamlit/develop/components/extras/images/logo.png" alt="Streamlit Logo" width="150"/>

# 💰 AI-Powered Financial Dashboard

### A sophisticated, multi-page budget tracking application with personalized AI-driven insights.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.x-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-F89939?style=for-the-badge&logo=scikit-learn&logoColor=white)

</div>

> This project is more than just a budget tracker; it's an intelligent financial dashboard designed to provide a clear and comprehensive overview of your spending habits. Built entirely in Python, it leverages Streamlit for a beautiful, interactive user interface and Pandas for robust data analysis to deliver actionable, AI-generated advice.

---

## 🚀 Live Demo

**Interact with the live application here:**

### **[https://ai-budget-tracker.streamlit.app/](https://ai-budget-tracker.streamlit.app/)**
  
*A quick demonstration of the app's features in action.*

## 📋 Table of Contents
- [✨ Key Features](#-key-features)
- [🏗️ Architecture & Tech Stack](#️-architecture--tech-stack)
- [🔧 The AI Advisor Workflow](#-the-ai-advisor-workflow)
- [⚙️ Getting Started](#️-getting-started)
  - [Prerequisites](#1-prerequisites)
  - [Installation & Setup](#2-installation--setup)
  - [Running the App](#3-run-the-application)
- [📞 Contact](#-contact)

---

## ✨ Key Features

-   **Professionally Structured UI:** A multi-page application design that cleanly separates the Dashboard, Transaction Entry, Detailed Analysis, and AI Advisor sections.
-   **Interactive Dashboard:** Features at-a-glance metrics for income, expenses, and balance, alongside an interactive pie chart for category-wise spending and a modern area chart for financial trends over time.
-   **Advanced Financial Flow Visualization:** A dedicated "Detailed Analysis" page featuring a sophisticated **Sankey Diagram** to beautifully illustrate the flow of money from income sources to expense categories.
-   **Personalized AI Financial Advisor:** The core intelligent feature that analyzes your data to provide actionable tips:
    -   Identifies your **highest spending category**.
    -   Detects **spending anomalies** (unusually high purchases) within categories.
    -   Compares your spending trends **month-over-month**.
-   **Custom Theming & Animations:** A polished user experience with a built-in toggle for Light/Dark modes (via the settings menu) and subtle fade-in animations.
-   **Full Data Control:** Users can add, view, and completely reset their transaction data with a safe, two-step confirmation process.

---

## 🏗️ Architecture & Tech Stack

This project uses a modern, Python-based stack to deliver a seamless experience from data processing to user interaction.

| Technology | Role |
| :--- | :--- |
| **Python** | The core programming language for all application logic. |
| **Streamlit** | The framework used to build and serve the entire interactive web application and UI components. |
| **Pandas** | The backbone for all data operations: loading the CSV, data manipulation, aggregation, and analysis. |
| **Plotly** | The engine for creating beautiful, interactive, and data-rich visualizations like the pie, area, and Sankey charts. |
| **Scikit-learn** | Used for prototyping the underlying machine learning models for anomaly detection and other insights. |

---

## 🔧 The AI Advisor Workflow

The AI Advisor provides insights not from a single complex model, but through a series of targeted data analysis steps, mimicking how a financial analyst would work.

**`[transactions.csv]` ➔ `[Data Ingest]` ➔ `[Filtering & Grouping]` ➔ `[Statistical Analysis]` ➔ `[Conditional Logic]` ➔ `[Personalized Tip]`**

1.  **Data Ingest:** The advisor loads the current, up-to-date transaction data from the shared session state.
2.  **Filtering & Grouping:** It separates expenses from income and groups transactions by category and by month.
3.  **Statistical Analysis:** For each spending category, it calculates key statistics like the mean (average) and standard deviation of transaction amounts. It also calculates total spending for the current and previous months.
4.  **Conditional Logic:** The advisor checks for specific conditions:
    -   *Is one category's total spending significantly higher than others?*
    -   *Is any single transaction more than 2 standard deviations above the average for its category?*
    -   *Is this month's spending more than 10% higher or lower than last month's?*
5.  **Personalized Tip Generation:** Based on which conditions are met, it generates a formatted, easy-to-understand string with a `st.warning`, `st.error`, or `st.success` message, providing the user with actionable advice.

---

## ⚙️ Getting Started

To get this project running on your local machine, follow these steps.

### **1. Prerequisites**
-   Python 3.8+
-   An understanding of how to use the command line/terminal.

### **2. Installation & Setup**

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/AtharvaMeherkar/ai-budget-tracker.git](https://github.com/AtharvaMeherkar/ai-budget-tracker.git)
    cd ai-budget-tracker
    ```
    *(Replace `your-username` with your actual GitHub username)*

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    ```bash
    # On Windows:
    .\venv\Scripts\activate
    
    # On macOS/Linux:
    source venv/bin/activate
    ```

4.  **Create a `requirements.txt` file:**
    Create a new file named `requirements.txt` and paste the following lines into it:
    ```text
    streamlit
    pandas
    plotly
    scikit-learn
    ```

5.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### **3. Run the Application**

Launch the Streamlit web server with this command:
```bash
streamlit run dashboard.py
```
The application will automatically open in a new tab in your web browser!

---

## 📞 Contact

Your Name - `atharvameherkar123@gmail.com`

Project Link: [https://github.com/AtharvaMeherkar/ai-budget-tracker](https://github.com/AtharvaMeherkar/ai-budget-tracker)
