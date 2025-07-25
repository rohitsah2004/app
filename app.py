import streamlit as st
import math

st.set_page_config(page_title="Medical Drug Calculator", layout="centered")
st.title("💊 Medical Drug Calculator")
st.subheader("Professional Dosing Calculator for Tepezza, Remicade, and Benlysta")
st.markdown("---")

tab = st.radio("Select Drug", ["Tepezza", "Remicade", "Benlysta"])

def validate_input(weight, dose):
    if weight <= 0 or dose <= 0:
        st.error("⚠️ Weight and dose must be greater than 0.")
        return False
    if weight > 500:
        st.warning("Weight seems unusually high. Please verify.")
    return True

def calculate_tepezza(weight, dose_per_kg):
    total_dose = round(weight * dose_per_kg, 1)
    volume_required = round(total_dose / 47.6, 1)
    vials_needed = math.ceil(total_dose / 500)
    iv_bag_size = "100 mL" if total_dose <= 1800 else "250 mL"
    ns_bag_volume = 100 if total_dose <= 1800 else 250
    remaining_ns = round(ns_bag_volume - volume_required, 1)

    infusion_time = "90 mins (1–2 infusions), then 60 mins (3–8 infusions)"
    infusion_rate = "66 mL/hr" if ns_bag_volume == 100 else "166 mL/hr"
    infusion_rate_60 = "100 mL/hr" if ns_bag_volume == 100 else "250 mL/hr"

    return f"""
📊 **PATIENT INFORMATION**  
• Weight: {weight:.1f} kg  
• Prescribed Dose: {dose_per_kg:.1f} mg/kg  

💊 **DOSAGE CALCULATIONS**  
• Total Dose: {total_dose} mg  
• Volume Required: {volume_required} mL  
• Vials Needed: {vials_needed}  
• IV Bag Size: {iv_bag_size}  

🧪 **PREPARATION STEPS**  
1. Use a {iv_bag_size} 0.9% Sodium Chloride bag  
2. Withdraw {volume_required} mL from the bag  
3. Inject 10 mL of SWFI into each of the {vials_needed} vial(s)  
4. Return {volume_required} mL to the remaining {remaining_ns} mL in the NS bag  

⚠️ **INFUSION INSTRUCTIONS**  
• First 1–2 infusions: Infuse over 90 minutes at {infusion_rate}  
• Infusions 3–8: Infuse over 60 minutes at {infusion_rate_60}  

⚠️ **NOTES**  
• Concentration: 47.6 mg/mL  
• Stability: Use within 24 hours or refrigerate  
"""

# Remicade and Benlysta remain unchanged
# ... (rest of the code continues without change)
