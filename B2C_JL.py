import streamlit as st

# Functions to calculate incentives
def calculate_cash_in_incentive(total_upfront_cash_in):
    conversion_rate = 88
    if 499 <= total_upfront_cash_in < 999:
        return 0
    elif 999 <= total_upfront_cash_in < 1499:
        return int(0.015 * total_upfront_cash_in * conversion_rate)
    elif 1499 <= total_upfront_cash_in < 1999:
        return int(0.025 * total_upfront_cash_in * conversion_rate)
    elif 1999 <= total_upfront_cash_in < 2499:
        return int(0.05 * total_upfront_cash_in * conversion_rate)
    elif 2499 <= total_upfront_cash_in < 2999:
        return int(0.075 * total_upfront_cash_in * conversion_rate)
    elif 2999 <= total_upfront_cash_in < 3499:
        return int(0.1 * total_upfront_cash_in * conversion_rate)
    elif 3499 <= total_upfront_cash_in < 3999:
        return int(0.125 * total_upfront_cash_in * conversion_rate)
    elif total_upfront_cash_in >= 3999:
        return int(0.15 * total_upfront_cash_in * conversion_rate)
    else:
        return 0

def calculate_price_control_incentive(full_payment_cash_in, mrp, deal_source):
    conversion_rate = 88
    if deal_source in ["PM-Search", "PM-Social", "Organic", "Others"]:
        if mrp == 649 and full_payment_cash_in >= 449:
            return int(0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in)
        elif mrp == 1199 and full_payment_cash_in >= 899:
            return int(0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in)
        elif mrp == 1999 and full_payment_cash_in >= 1549:
            return int(0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in)
        else:
            return 0
    elif deal_source in ["Referral", "Events", "Goldmine", "DP"]:
        if mrp == 649 and full_payment_cash_in >= 399:
            return int(0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in)
        elif mrp == 1199 and full_payment_cash_in >= 799:
            return int(0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in)
        elif mrp == 1999 and full_payment_cash_in >= 1429:
            return int(0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in)
        else:
            return 0
    else:
        return 0

# Streamlit App
st.title("Jan Incentive Calculator")

# Upfront Cash-in Incentive Section
st.subheader("Upfront Cash-in Incentive")
total_upfront_cash_in = st.number_input("Total Upfront Cash-in (€):", min_value=0, step=1)
upfront_incentive = calculate_cash_in_incentive(total_upfront_cash_in)
st.write(f"**Upfront Cash-in Incentive: INR {upfront_incentive:,}**")

# Manage dynamic full payment cases
st.subheader("Dynamic Full Payment Cases")

if "full_payment_cases" not in st.session_state:
    st.session_state.full_payment_cases = []

# Add a new full payment case
if st.button("Add Full Payment Case"):
    st.session_state.full_payment_cases.append({
        "full_payment_cash_in": 0,
        "mrp": 119,
        "deal_source": "PM-Search",
        "incentive": 0
    })

# Display all cases dynamically
total_price_control_incentive = 0
cases_to_remove = []

for i, case in enumerate(st.session_state.full_payment_cases):
    st.markdown(f"**Case {i + 1}**")
    cols = st.columns([2, 2, 2, 1])
    
    case["full_payment_cash_in"] = cols[0].number_input(
        f"Full Payment Cash-in (€) - Case {i + 1}", 
        min_value=0, 
        step=1, 
        value=case["full_payment_cash_in"], 
        key=f"full_payment_cash_in_{i}"
    )
    case["mrp"] = cols[1].selectbox(
        f"MRP (€) - Case {i + 1}", 
        options=[119, 349, 649, 1199, 1999], 
        index=[119, 349, 649, 1199, 1999].index(case["mrp"]), 
        key=f"mrp_{i}"
    )
    case["deal_source"] = cols[2].selectbox(
        f"Deal Source - Case {i + 1}", 
        options=["PM-Search", "PM-Social", "Organic", "Others", "Referral", "Events", "Goldmine", "DP"], 
        index=["PM-Search", "PM-Social", "Organic", "Others", "Referral", "Events", "Goldmine", "DP"].index(case["deal_source"]), 
        key=f"deal_source_{i}"
    )
    
    if cols[3].button(f"Delete Case {i + 1}", key=f"delete_case_{i}"):
        cases_to_remove.append(i)
    
    # Calculate incentive for this case
    case["incentive"] = calculate_price_control_incentive(
        case["full_payment_cash_in"], case["mrp"], case["deal_source"]
    )
    st.write(f"Price Control Incentive for Case {i + 1}: INR {case['incentive']:,}")
    total_price_control_incentive += case["incentive"]

# Remove deleted cases
for index in sorted(cases_to_remove, reverse=True):
    st.session_state.full_payment_cases.pop(index)

# Additional Incentives Section
st.subheader("Additional Incentives")
d0_cases = st.number_input("D0 Conversion Cases >= €400:", min_value=0, step=1)
within_window_cases = st.number_input("Converted within Window Cases:", min_value=0, step=1)
self_gen_cases = st.number_input("Self Gen Referral Cases:", min_value=0, step=1)
additional_incentive = (d0_cases * 300) + (within_window_cases * 4000) + (self_gen_cases * 3000)
st.write(f"**Additional Incentives: INR {additional_incentive:,}**")

# Final Incentive Calculation
st.subheader("Final Incentive")
total_incentive = upfront_incentive + total_price_control_incentive + additional_incentive
st.markdown(f"<h1 style='text-align: center; color: green;'>Overall Total Incentive: INR {total_incentive:,}</h1>", unsafe_allow_html=True)
