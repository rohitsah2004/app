import streamlit as st
import math

st.set_page_config(page_title="Medical Drug Calculator", layout="centered")

st.title("💊 Medical Drug Calculator")
st.subheader("Professional Dosing Calculator for Tepezza and Remicade")
st.markdown("---")

# Tab selection
tab = st.radio("Select Drug", ["Tepezza", "Remicade"])

def validate_input(weight, dose):
    if weight <= 0 or dose <= 0:
        st.error("⚠️ Weight and dose must be greater than 0.")
        return False
    if weight > 500:
        st.warning("Weight seems unusually high. Please verify.")
    return True

def calculate_tepezza(weight, dose_per_kg):
    total_dose = weight * dose_per_kg
    volume_required = total_dose / 47.6
    vials_needed = math.ceil(total_dose / 500)
    iv_bag_size = "100 mL" if total_dose <= 1800 else "250 mL"
    ns_bag_volume = 100 if total_dose <= 1800 else 250
    remaining_ns = ns_bag_volume - volume_required

    return f"""
📊 **PATIENT INFORMATION**  
• Weight: {weight:.1f} kg  
• Prescribed Dose: {dose_per_kg:.1f} mg/kg  

💊 **DOSAGE CALCULATIONS**  
• Total Dose: {total_dose:.1f} mg  
• Volume Required: {volume_required:.1f} mL  
• Vials Needed: {vials_needed}  
• IV Bag Size: {iv_bag_size}  

🧪 **PREPARATION STEPS**  
1. Use a {iv_bag_size} 0.9% Sodium Chloride bag  
2. Withdraw {volume_required:.1f} mL from the bag  
3. Inject 10 mL of SWFI into each of the {vials_needed} vial(s)  
4. Return {volume_required:.1f} mL to the remaining {remaining_ns:.1f} mL in the NS bag  

⚠️ **NOTES**  
• Concentration: 47.6 mg/mL  
• Stability: Use within 24 hours or refrigerate  
• Administer over 90 mins (1–2 infusions), then 60 mins (3–8 infusions)  
"""

def calculate_remicade(weight, dose_per_kg):
    total_dose = weight * dose_per_kg
    volume_required = total_dose / 10
    vials_needed = math.ceil(total_dose / 100)

    if total_dose > 2000:
        iv_bag_size = "two 500 mL bags"
        bag_volume = 1000
    elif total_dose > 1000:
        iv_bag_size = "500 mL"
        bag_volume = 500
    else:
        iv_bag_size = "250 mL"
        bag_volume = 250

    remaining_volume = bag_volume - volume_required

    return f"""
📊 **PATIENT INFORMATION**  
• Weight: {weight:.1f} kg  
• Prescribed Dose: {dose_per_kg:.1f} mg/kg  

💉 **DOSAGE CALCULATIONS**  
• Total Dose: {total_dose:.1f} mg  
• Volume Required: {volume_required:.1f} mL  
• Vials Needed: {vials_needed}  
• IV Bag Size: {iv_bag_size}  

🧪 **PREPARATION STEPS**  
1. Use a {iv_bag_size} 0.9% Sodium Chloride bag  
2. Withdraw {volume_required:.1f} mL using 21g needle  
3. Inject 10 mL of NS into each of the {vials_needed} vial(s)  
4. Return {volume_required:.1f} mL to the remaining {remaining_volume:.1f} mL in the NS bag  
5. Attach 0.2-micron filtered tubing  

⚠️ **NOTES**  
• Concentration: 10 mg/mL  
• Final infusion concentration: 0.4–4.0 mg/mL  
• Use immediately or refrigerate (good for 24 hrs)  
• Administer IV over 2+ hours  
"""

# --- INPUT FORM ---
with st.form("dose_form"):
    weight = st.number_input("Patient Weight (kg)", min_value=0.0, format="%.1f")
    dose = st.number_input("Prescribed Dose (mg/kg)", min_value=0.0, format="%.1f")
    submitted = st.form_submit_button("🧮 Calculate")

# --- RESULTS ---
if submitted:
    if validate_input(weight, dose):
        st.markdown("---")
        if tab == "Tepezza":
            result = calculate_tepezza(weight, dose)
        else:
            result = calculate_remicade(weight, dose)
        st.markdown(result)

st.markdown("---")
st.caption("For healthcare use only. Always verify clinical decisions independently.")
