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

# Add a gap before the logic explanation
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

# Incentive Formulas Section
st.markdown("<h2 style='color: darkblue;'>Incentive Calculation Logic</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 14px;'>
<strong>Upfront Cash-in Incentive:</strong> Percentage-based on total upfront cash-in tiers (e.g., 1.5% for €999-€1499, 2.5% for €1499-€1999); 
<strong>Price Control Incentive:</strong> 7.5% of full payment cash-in based on MRP and source thresholds; 
<strong>D0 Conversion Cases:</strong> INR 3000 per case (cash-in >= €400); 
<strong>Converted within Window Cases:</strong> INR 4000 per case (completed within time window); 
<strong>Self-Generated Referral Cases:</strong> INR 3000 per case (cash-in >= €400); 
<strong>Trial Scheduled Today:</strong> INR 1000 per trial beyond 4 (50% completion within 3 days); 
<strong>Trial Done Today:</strong> INR 2000 per trial beyond 4; 
<strong>Final Incentive:</strong> Zero if trials scheduled today are less than 2.
</p>
""", unsafe_allow_html=True)
