# import streamlit as st
# import requests
# import pandas as pd
# import plotly.express as px

# API_URL = ""https://expense-tracker-backend-ni52.onrender.com"

# st.set_page_config(page_title="💸 Expense Tracker", layout="wide")

# # Session states
# if "expense_added" not in st.session_state:
#     st.session_state.expense_added = False
# if "expense_deleted" not in st.session_state:
#     st.session_state.expense_deleted = False

# st.title("💸 Expense Tracker")

# # Add New Expense
# with st.sidebar:
#     st.header("➕ Add New Expense")
#     with st.form("expense_form", clear_on_submit=True):
#         date = st.date_input("Date")
#         category = st.selectbox("Category", ["Food", "Transport", "Utilities", "Entertainment", "Other"])
#         amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
#         note = st.text_input("Note")
#         submit = st.form_submit_button("Add Expense")
#         if submit:
#             data = {
#                 "date": date.strftime("%Y-%m-%d"),
#                 "category": category,
#                 "amount": amount,
#                 "note": note,
#             }
#             res = requests.post(f"{API_URL}/add", json=data)
#             if res.status_code == 201:
#                 st.session_state.expense_added = True
#                 st.rerun()
#             else:
#                 st.error("❌ Failed to add expense")

# if st.session_state.expense_added:
#     st.success("✅ Expense added successfully!")
#     st.session_state.expense_added = False

# if st.session_state.expense_deleted:
#     st.success("🗑️ Expense deleted successfully!")
#     st.session_state.expense_deleted = False

# # Load Expenses
# @st.cache_data(ttl=5)
# def load_expenses():
#     try:
#         res = requests.get(f"{API_URL}/expenses")
#         if res.ok:
#             return pd.DataFrame(res.json())
#         else:
#             st.error("❌ Failed to fetch data")
#             return pd.DataFrame()
#     except Exception as e:
#         st.error(f"❌ Error loading data: {e}")
#         return pd.DataFrame()

# df = load_expenses()

# # Filter Options
# st.subheader("🔍 Filter Expenses")
# col1, col2 = st.columns(2)

# with col1:
#     if not df.empty and "category" in df.columns:
#         selected_category = st.selectbox("Filter by Category", ["All"] + sorted(df["category"].dropna().unique().tolist()))
#     else:
#         selected_category = "All"
#         st.warning("No categories to filter.")

# with col2:
#     search_text = st.text_input("Search in Notes")

# # Filter logic
# filtered_df = df.copy()
# if not filtered_df.empty:
#     if "category" in filtered_df.columns and selected_category != "All":
#         filtered_df = filtered_df[filtered_df["category"] == selected_category]
#     if "note" in filtered_df.columns and search_text:
#         filtered_df = filtered_df[filtered_df["note"].str.contains(search_text, case=False)]

# # Display Table
# st.subheader("📋 All Expenses")
# if not filtered_df.empty:
#     filtered_df.index.name = "Index"
#     if "amount" in filtered_df.columns:
#         filtered_df["Amount (₹)"] = filtered_df["amount"].apply(lambda x: f"₹{x:.2f}")
#     display_df = filtered_df[["date", "category", "Amount (₹)", "note"]]
#     st.dataframe(display_df, use_container_width=True)

#     st.markdown("### 🧹 Delete an Expense")
#     selected_index = st.number_input("Enter Index to Delete", min_value=0, max_value=len(df)-1, step=1)
#     if st.button("Delete Selected Expense"):
#         del_res = requests.delete(f"{API_URL}/delete/{selected_index}")
#         if del_res.ok:
#             st.session_state.expense_deleted = True
#             st.rerun()
#         else:
#             st.error("❌ Failed to delete expense")
# else:
#     st.info("No expenses to show based on your filters.")

# # Summary Section
# st.subheader("📊 Summary")
# if not df.empty and "amount" in df.columns and "date" in df.columns:
#     total_spent = df["amount"].sum()
#     st.markdown(f"### 💰 Total Spent: ₹ {total_spent:.2f}")

#     # Pie Chart: Spending by Category
#     if "category" in df.columns:
#         category_summary = df.groupby("category")["amount"].sum().reset_index()
#         fig = px.pie(category_summary, names="category", values="amount", title="Spending by Category", hole=0.4)
#         st.plotly_chart(fig, use_container_width=True)

#     # Monthly Expenses
#     df["month"] = pd.to_datetime(df["date"], errors="coerce").dt.to_period("M").astype(str)
#     monthly_summary = df.groupby("month")["amount"].sum().reset_index()
#     bar_fig = px.bar(monthly_summary, x="month", y="amount", title="Monthly Expenses", text_auto=True)
#     st.plotly_chart(bar_fig, use_container_width=True)

#     # CSV Download
#     csv = df.to_csv(index=False).encode("utf-8")
#     st.download_button("⬇️ Download Expenses as CSV", csv, file_name="expenses.csv", mime="text/csv")
# else:
#     st.warning("Please add some valid expenses to see summaries.")

# # Styles
# st.markdown("""
# <style>
# div.stButton > button {
#     background-color: #4CAF50;
#     color: white;
#     font-weight: 600;
#     border-radius: 8px;
#     padding: 10px 16px;
# }
# div.stButton > button:hover {
#     background-color: #388E3C;
# }
# </style>
# """, unsafe_allow_html=True)


import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "https://expense-tracker-backend-ni52.onrender.com"  # ✅ Fixed

st.set_page_config(page_title="💸 Expense Tracker", layout="wide")

# Session states
if "expense_added" not in st.session_state:
    st.session_state.expense_added = False
if "expense_deleted" not in st.session_state:
    st.session_state.expense_deleted = False

st.title("💸 Expense Tracker")

# Add New Expense
with st.sidebar:
    st.header("➕ Add New Expense")
    with st.form("expense_form", clear_on_submit=True):
        date = st.date_input("Date")
        category = st.selectbox("Category", ["Food", "Transport", "Utilities", "Entertainment", "Other"])
        amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
        note = st.text_input("Note")
        submit = st.form_submit_button("Add Expense")
        if submit:
            data = {
                "date": date.strftime("%Y-%m-%d"),
                "category": category,
                "amount": amount,
                "note": note,
            }
            try:
                res = requests.post(f"{API_URL}/add", json=data)
                if res.status_code == 201:
                    st.session_state.expense_added = True
                    st.rerun()
                else:
                    st.error("❌ Failed to add expense")
            except Exception as e:
                st.error(f"❌ Connection error: {e}")

if st.session_state.expense_added:
    st.success("✅ Expense added successfully!")
    st.session_state.expense_added = False

if st.session_state.expense_deleted:
    st.success("🗑️ Expense deleted successfully!")
    st.session_state.expense_deleted = False

# Load Expenses
@st.cache_data(ttl=5)
def load_expenses():
    try:
        res = requests.get(f"{API_URL}/expenses")
        if res.ok:
            return pd.DataFrame(res.json())
        else:
            st.error("❌ Failed to fetch data")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"❌ Error loading data: {e}")
        return pd.DataFrame()

df = load_expenses()

# Filter Options
st.subheader("🔍 Filter Expenses")
col1, col2 = st.columns(2)

with col1:
    if not df.empty and "category" in df.columns:
        selected_category = st.selectbox("Filter by Category", ["All"] + sorted(df["category"].dropna().unique().tolist()))
    else:
        selected_category = "All"
        st.warning("No categories to filter.")

with col2:
    search_text = st.text_input("Search in Notes")

# Filter logic
filtered_df = df.copy()
if not filtered_df.empty:
    if "category" in filtered_df.columns and selected_category != "All":
        filtered_df = filtered_df[filtered_df["category"] == selected_category]
    if "note" in filtered_df.columns and search_text:
        filtered_df = filtered_df[filtered_df["note"].str.contains(search_text, case=False)]

# Display Table
st.subheader("📋 All Expenses")
if not filtered_df.empty:
    filtered_df.index.name = "Index"
    if "amount" in filtered_df.columns:
        filtered_df["Amount (₹)"] = filtered_df["amount"].apply(lambda x: f"₹{x:.2f}")
    display_df = filtered_df[["date", "category", "Amount (₹)", "note"]]
    st.dataframe(display_df, use_container_width=True)

    st.markdown("### 🧹 Delete an Expense")
    selected_index = st.number_input("Enter Index to Delete", min_value=0, max_value=len(df)-1, step=1)
    if st.button("Delete Selected Expense"):
        try:
            del_res = requests.delete(f"{API_URL}/delete/{selected_index}")
            if del_res.ok:
                st.session_state.expense_deleted = True
                st.rerun()
            else:
                st.error("❌ Failed to delete expense")
        except Exception as e:
            st.error(f"❌ Connection error: {e}")
else:
    st.info("No expenses to show based on your filters.")

# Summary Section
st.subheader("📊 Summary")
if not df.empty and "amount" in df.columns and "date" in df.columns:
    total_spent = df["amount"].sum()
    st.markdown(f"### 💰 Total Spent: ₹ {total_spent:.2f}")

    # Pie Chart: Spending by Category
    if "category" in df.columns:
        category_summary = df.groupby("category")["amount"].sum().reset_index()
        fig = px.pie(category_summary, names="category", values="amount", title="Spending by Category", hole=0.4)
        st.plotly_chart(fig, use_container_width=True)

    # Monthly Expenses
    df["month"] = pd.to_datetime(df["date"], errors="coerce").dt.to_period("M").astype(str)
    monthly_summary = df.groupby("month")["amount"].sum().reset_index()
    bar_fig = px.bar(monthly_summary, x="month", y="amount", title="Monthly Expenses", text_auto=True)
    st.plotly_chart(bar_fig, use_container_width=True)

    # CSV Download
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download Expenses as CSV", csv, file_name="expenses.csv", mime="text/csv")
else:
    st.warning("Please add some valid expenses to see summaries.")

# Styles
st.markdown("""
<style>
div.stButton > button {
    background-color: #4CAF50;
    color: white;
    font-weight: 600;
    border-radius: 8px;
    padding: 10px 16px;
}
div.stButton > button:hover {
    background-color: #388E3C;
}
</style>
""", unsafe_allow_html=True)
