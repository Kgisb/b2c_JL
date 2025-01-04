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
st.markdown("<h1 style='text-align: center; color: darkblue;'>Jan Incentive Calculator</h1>", unsafe_allow_html=True)

# Upfront Cash-in Incentive Section
st.markdown("<h2 style='color: darkgreen;'>Upfront Cash-in Incentive</h2>", unsafe_allow_html=True)
total_upfront_cash_in = st.number_input("Total Upfront Cash-in (€):", min_value=0, step=1, format="%d")
upfront_incentive = calculate_cash_in_incentive(total_upfront_cash_in)
st.markdown(f"<p style='background-color: lightyellow; color: black; padding: 10px; border-radius: 5px;'>Upfront Cash-in Incentive: <strong>INR {upfront_incentive:,}</strong></p>", unsafe_allow_html=True)

# Manage dynamic full payment cases
st.markdown("<h2 style='color: darkorange;'>Dynamic Full Payment Cases</h2>", unsafe_allow_html=True)

if "full_payment_cases" not in st.session_state:
    st.session_state.full_payment_cases = []

# Add a new full payment case
if st.button("Add Full Payment Case", key="add_case"):
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
    st.markdown(f"<h4 style='color: darkblue;'>Case {i + 1}</h4>", unsafe_allow_html=True)
    cols = st.columns([2, 2, 2, 1])
    
    case["full_payment_cash_in"] = cols[0].number_input(
        f"Full Payment Cash-in (€) - Case {i + 1}", 
        min_value=0, 
        step=1, 
        value=case["full_payment_cash_in"], 
        format="%d", 
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
    st.markdown(f"<p style='color: darkgreen;'>Price Control Incentive for Case {i + 1}: <strong>INR {case['incentive']:,}</strong></p>", unsafe_allow_html=True)
    total_price_control_incentive += case["incentive"]

# Remove deleted cases
for index in sorted(cases_to_remove, reverse=True):
    st.session_state.full_payment_cases.pop(index)

# Additional Incentives Section
st.markdown("<h2 style='color: darkviolet;'>Additional Incentives</h2>", unsafe_allow_html=True)
d0_cases = st.number_input("D0 Conversion Cases >= €400:", min_value=0, step=1, format="%d")
within_window_cases = st.number_input("Converted within Window Cases: >=400 cash-in case", min_value=0, step=1, format="%d")
self_gen_cases = st.number_input("Self Gen Referral Cases: >=400 cash-in case", min_value=0, step=1, format="%d")
trial_scheduled_today = st.number_input("TS Today (Atleaset 50% is Done within 3 days, if > 4, INR 1000 per trial):", min_value=0, step=1, format="%d")
trial_done = st.number_input("TD Today (if > 4, INR 2000 per trial):", min_value=0, step=1, format="%d")

# Calculate additional incentives
additional_incentive = (
    (d0_cases * 3000) +
    (within_window_cases * 4000) +
    (self_gen_cases * 3000) +
    (max(0, trial_scheduled_today - 4) * 1000) +
    (max(0, trial_done - 4) * 2000)
)

st.markdown(f"<p style='background-color: lightblue; color: black; padding: 10px; border-radius: 5px;'>Additional Incentives: <strong>INR {additional_incentive:,}</strong></p>", unsafe_allow_html=True)

# Final Incentive Calculation
st.markdown("<h2 style='color: darkred;'>Final Incentive</h2>", unsafe_allow_html=True)

# Check if trial scheduled today is less than 2
if trial_scheduled_today < 2:
    total_incentive = 0
    st.markdown(
        "<p style='color: red; text-align: center; font-weight: bold;'>Final incentive is set to zero because trial scheduled today is less than 2.</p>",
        unsafe_allow_html=True
    )
else:
    total_incentive = upfront_incentive + total_price_control_incentive + additional_incentive

st.markdown(f"<h1 style='text-align: center; background-color: lightgreen; color: black; padding: 15px; border-radius: 10px;'>Overall Total Incentive: INR {total_incentive:,}</h1>", unsafe_allow_html=True)
