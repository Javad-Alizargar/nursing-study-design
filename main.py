
import streamlit as st
import os

st.set_page_config(page_title="StatWhy Study Design", layout="wide")
st.title("🎓 Nursing Study Design Simulator")

# Navigation for Weeks
day_choice = st.sidebar.selectbox("Select Week", ["Week 1: Foundations", "Week 2", "Week 3", "Week 4", "Week 5"])

if day_choice == "Week 1: Foundations":
    from modules import week1
    week1.run()
else:
    st.write("Coming soon...")
