import streamlit as st
import json
import datetime

st.set_page_config(page_title="Bridge Talent - LatAm/Eastern Europe Dev Recruiting", page_icon="🌉")

st.title("🌉 Bridge Talent")
st.markdown("**Connecting US tech companies with elite remote engineers from Latin America & Eastern Europe.** Save 30-50% vs. domestic hires. 0-3 hour timezone overlap.")

tab1, tab2 = st.tabs(["🏢 I'm Hiring", "👨‍💻 I'm a Developer"])

with tab1:
    st.subheader("Submit an Open Role")
    with st.form("client_form"):
        company = st.text_input("Company Name")
        role = st.text_input("Role Title (e.g., Senior Python Engineer)")
        stack = st.text_input("Required Stack (e.g., Python, AWS, React)")
        budget = st.number_input("Monthly Budget (USD)", min_value=1000, value=6000, step=500)
        contact = st.text_input("Your Email")
        submitted = st.form_submit_button("Submit Role")
        if submitted:
            st.success(f"✅ Role submitted! We'll source candidates within 72 hours and contact you at {contact}.")

with tab2:
    st.subheader("Join Our Talent Pool")
    with st.form("candidate_form"):
        name = st.text_input("Full Name")
        country = st.text_input("Country")
        stack = st.text_input("Primary Stack")
        english = st.selectbox("English Level", ["Basic", "Intermediate", "Advanced", "Native"])
        github = st.text_input("GitHub Profile URL")
        candidate_submitted = st.form_submit_button("Apply")
        if candidate_submitted:
            st.success("✅ Application received! We'll review your profile and reach out within 48 hours.")

st.divider()
st.caption("Bridge Talent | Contingency Recruiting | 18-22% placement fee | 90-day guarantee")
