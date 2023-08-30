import streamlit as st

# Define the criteria for SIRS, Sepsis, and Septic Shock
def assess_condition(temp, heart_rate, resp_rate, wbc, infection, sysbp, lactate):
    sirs_criteria = 0
    sepsis = False
    septic_shock = False
    
    if temp < 36 or temp > 38:
        sirs_criteria += 1
    if heart_rate > 90:
        sirs_criteria += 1
    if resp_rate > 20 or paco2 < 32:
        sirs_criteria += 1
    if wbc < 4 or wbc > 12:
        sirs_criteria += 1
    
    if sirs_criteria >= 2 and infection:
        sepsis = True
    
    if sepsis and (sysbp < 90 or lactate > 4):
        septic_shock = True
    
    return sirs_criteria, sepsis, septic_shock

# Create the Streamlit app
st.title('SIRS, Sepsis, and Septic Shock Assessment')

# Input patient data
temp = st.number_input('Temperature (°C)')
heart_rate = st.number_input('Heart rate (bpm)')
resp_rate = st.number_input('Respiratory rate (breaths/min)')
wbc = st.number_input('White blood cell count (x10^9/L)')
infection = st.checkbox('Confirmed infection?')
sysbp = st.number_input('Systolic blood pressure (mmHg)')
lactate = st.number_input('Serum lactate (mmol/L)')

# Assess condition based on input
sirs_criteria, sepsis, septic_shock = assess_condition(temp, heart_rate, resp_rate, wbc, infection, sysbp, lactate)

# Display results
st.write('SIRS Criteria Met:', sirs_criteria)
st.write('Sepsis:', sepsis)
st.write('Septic Shock:', septic_shock)
