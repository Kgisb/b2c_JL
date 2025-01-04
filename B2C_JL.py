import streamlit as st

def calculate_cash_in_incentive(total_upfront_cash_in):
    conversion_rate = 88  # Conversion value from Euro to INR
    if 499 <= total_upfront_cash_in < 999:
        return 0
    elif 999 <= total_upfront_cash_in < 1499:
        return 0.015 * total_upfront_cash_in * conversion_rate
    elif 1499 <= total_upfront_cash_in < 1999:
        return 0.025 * total_upfront_cash_in * conversion_rate
    elif 1999 <= total_upfront_cash_in < 2499:
        return 0.05 * total_upfront_cash_in * conversion_rate
    elif 2499 <= total_upfront_cash_in < 2999:
        return 0.075 * total_upfront_cash_in * conversion_rate
    elif 2999 <= total_upfront_cash_in < 3499:
        return 0.1 * total_upfront_cash_in * conversion_rate
    elif 3499 <= total_upfront_cash_in < 3999:
        return 0.125 * total_upfront_cash_in * conversion_rate
    elif total_upfront_cash_in >= 3999:
        return 0.15 * total_upfront_cash_in * conversion_rate
    else:
        return 0

def calculate_price_control_incentive(full_payment_cash_in, mrp, deal_source):
    conversion_rate = 88  # Conversion value from Euro to INR
    if deal_source in ["PM-Search", "PM-Social", "Organic", "Others"]:
        if mrp == 649 and full_payment_cash_in >= 449:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        elif mrp == 1199 and full_payment_cash_in >= 899:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        elif mrp == 1999 and full_payment_cash_in >= 1549:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        else:
            return 0
    elif deal_source in ["Referral", "Events", "Goldmine", "DP"]:
        if mrp == 649 and full_payment_cash_in >= 399:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        elif mrp == 1199 and full_payment_cash_in >= 799:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        elif mrp == 1999 and full_payment_cash_in >= 1429:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        else:
            return 0
    else:
        return 0

# Streamlit Interface
st.title("Incentive Calculator")

# Upfront Cash-in Section
st.subheader("Upfront Cash-in Incentive Calculation")
total_upfront_cash_in = st.number_input("Total Upfront Cash-in (€):", min_value=0.0, step=0.01, value=0.0)
if st.button("Calculate Upfront Incentive"):
    upfront_incentive = calculate_cash_in_incentive(total_upfront_cash_in)
    st.success(f"Upfront Cash-in Incentive: INR {upfront_incentive:,.2f}")

# Dynamic Full Payment Cases
st.subheader("Price Control Incentive Calculation")
st.write("Add and calculate incentives for multiple Full Payment Cases.")

if "full_payment_cases" not in st.session_state:
    st.session_state.full_payment_cases = []

# Function to add a new case
def add_case():
    st.session_state.full_payment_cases.append({
        "full_payment_cash_in": 0.0,
        "mrp": 119,
        "deal_source": "PM-Search"
    })

# Function to delete a case
def delete_case(index):
    st.session_state.full_payment_cases.pop(index)

# Add new case button
if st.button("Add Another Full Payment Case"):
    add_case()

# Display all cases
total_price_control_incentive = 0
for i, case in enumerate(st.session_state.full_payment_cases):
    st.write(f"Case {i+1}")
    case["full_payment_cash_in"] = st.number_input(
        f"Full Payment Cash-in (€) - Case {i+1}:", 
        min_value=0.0, 
        step=0.01, 
        value=case["full_payment_cash_in"], 
        key=f"cash_in_{i}"
    )
    case["mrp"] = st.selectbox(
        f"MRP (€) - Case {i+1}:", 
        options=[119, 349, 649, 1199, 1999], 
        index=[119, 349, 649, 1199, 1999].index(case["mrp"]), 
        key=f"mrp_{i}"
    )
    case["deal_source"] = st.selectbox(
        f"Deal Source - Case {i+1}:", 
        options=["PM-Search", "PM-Social", "Organic", "Others", "Referral", "Events", "Goldmine", "DP"], 
        index=["PM-Search", "PM-Social", "Organic", "Others", "Referral", "Events", "Goldmine", "DP"].index(case["deal_source"]), 
        key=f"deal_source_{i}"
    )
    if st.button(f"Delete Case {i+1}", key=f"delete_{i}"):
        delete_case(i)
        st.experimental_rerun()
    
    # Calculate incentive for this case
    incentive = calculate_price_control_incentive(
        case["full_payment_cash_in"], case["mrp"], case["deal_source"]
    )
    st.write(f"Price Control Incentive for Case {i+1}: INR {incentive:,.2f}")
    total_price_control_incentive += incentive

# Display total price control incentive
st.write(f"**Total Price Control Incentive: INR {total_price_control_incentive:,.2f}**")

# Additional Incentives Section
st.subheader("Additional Incentives Calculation")
d0_cases = st.number_input("D0 Conversion Cases >= €400:", min_value=0, step=1, value=0)
within_window_cases = st.number_input("Converted within Window Cases:", min_value=0, step=1, value=0)
self_gen_cases = st.number_input("Self Gen Referral Cases:", min_value=0, step=1, value=0)
if st.button("Calculate Additional Incentives"):
    additional_incentive = (d0_cases * 300) + (within_window_cases * 4000) + (self_gen_cases * 3000)
    st.success(f"Additional Incentives: INR {additional_incentive:,.2f}")

# Final Incentive Calculation
st.subheader("Final Incentive")
if st.button("Calculate Total Incentive"):
    upfront_incentive = calculate_cash_in_incentive(total_upfront_cash_in)
    total_additional_incentive = (d0_cases * 300) + (within_window_cases * 4000) + (self_gen_cases * 3000)
    total_incentive = upfront_incentive + total_price_control_incentive + total_additional_incentive
    st.success(f"Overall Total Incentive: INR {total_incentive:,.2f}")
