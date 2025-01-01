import streamlit as st

# Title of the app
st.title("Academic Counselor Incentive Calculator")

# Input fields
date = st.date_input("Select Date")
counselor = st.selectbox(
    "Select Academic Counselor:",
    ["Ali", "Kavish", "Fuzail", "Pranav", "Ashish", "Sreejit", "Bilal", 
     "Vimal", "Kamal", "Daksh", "Karan", "Ralph", "Salim", "Ankush"]
)
deal_source = st.selectbox(
    "Select Deal Source:",
    ["Referral", "PM-Search", "PM-Social", "Organic", "Others"]
)
subscription_months = st.selectbox(
    "Select Subscription Months:",
    [1, 3, 6, 12, 24]
)
upfront_cash = st.number_input(
    "Enter Upfront Cash (€):",
    min_value=0.0,
    step=1.0
)

# Logic for calculating incentive
if st.button("Calculate Incentive"):
    incentive = 0
    if subscription_months == 1 and upfront_cash >= 100:
        incentive = 0
    elif subscription_months == 3 and upfront_cash >= 299:
        if deal_source == "Referral":
            incentive = upfront_cash * 88 * 0.015
        else:
            incentive = upfront_cash * 88 * 0.01
    elif subscription_months == 6 and upfront_cash >= 499:
        if deal_source == "Referral":
            incentive = upfront_cash * 88 * 0.025
        else:
            incentive = upfront_cash * 88 * 0.02
    elif subscription_months == 12 and upfront_cash >= 899:
        if deal_source == "Referral":
            incentive = upfront_cash * 88 * 0.05
        else:
            incentive = upfront_cash * 88 * 0.03

    # Display results
    st.write(f"### Date: {date}")
    st.write(f"### Counselor: {counselor}")
    st.write(f"### Deal Source: {deal_source}")
    st.write(f"### Subscription Months: {subscription_months}")
    st.write(f"### Upfront Cash (€): {upfront_cash:.2f}")
    st.write(f"### Calculated Incentive (€): {incentive:.2f}")
