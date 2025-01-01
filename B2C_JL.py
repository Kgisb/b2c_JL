#!/usr/bin/env python
# coding: utf-8

# In[6]:


import ipywidgets as widgets
from IPython.display import display, clear_output

# Dropdown for selecting date
date_picker = widgets.DatePicker(
    description='Date:',
    disabled=False
)

# Dropdown for selecting academic counselor
counselor_dropdown = widgets.Dropdown(
    options=["Ali", "Kavish", "Fuzail", "Pranav", "Ashish", "Sreejit", "Bilal", 
             "Vimal", "Kamal", "Daksh", "Karan", "Ralph", "Salim", "Ankush"],
    description='Counselor:'
)

# Dropdown for deal source
deal_source_dropdown = widgets.Dropdown(
    options=["Referral", "PM-Search", "PM-Social", "Organic", "Others"],
    description='Deal Source:'
)

# Dropdown for subscription months
subscription_dropdown = widgets.Dropdown(
    options=[1, 3, 6, 12, 24],
    description='Subscription:'
)

# Input for upfront cash
upfront_cash_input = widgets.FloatText(
    value=0.0,
    description='Upfront Cash (€):',
)

# Output widget for displaying results
output = widgets.Output()

# Button for calculating incentive
calculate_button = widgets.Button(description="Calculate Incentive")

# Calculation logic
def calculate_incentive(button):
    with output:
        clear_output()
        
        # Get user inputs
        date = date_picker.value
        counselor = counselor_dropdown.value
        deal_source = deal_source_dropdown.value
        subscription_months = subscription_dropdown.value
        upfront_cash = upfront_cash_input.value
        
        # Check incentive conditions
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
        print(f"Date: {date}")
        print(f"Counselor: {counselor}")
        print(f"Deal Source: {deal_source}")
        print(f"Subscription Months: {subscription_months}")
        print(f"Upfront Cash (€): {upfront_cash}")
        print(f"Calculated Incentive (€): {incentive:.2f}")

# Link the button to the calculation function
calculate_button.on_click(calculate_incentive)

# Display widgets
display(date_picker, counselor_dropdown, deal_source_dropdown, subscription_dropdown, upfront_cash_input, calculate_button, output)


# In[ ]:




