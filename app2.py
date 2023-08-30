import streamlit as st

# Function to calculate SOFA score
def calculate_sofa_score(resp_ratio, platelets, bilirubin, map, creatinine, gcs):
    sofa_score = 0
    
    # Respiratory
    if resp_ratio < 100: 
        sofa_score += 4
    elif resp_ratio < 200: 
        sofa_score += 3
    elif resp_ratio < 300: 
        sofa_score += 2
    elif resp_ratio < 400: 
        sofa_score += 1
    else:
        sofa_score += 0
    
    # Coagulation
    if platelets < 20: 
        sofa_score += 4
    elif platelets < 50: 
        sofa_score += 3
    elif platelets < 100: 
        sofa_score += 2
    elif platelets < 150: 
        sofa_score += 1
    else:
        sofa_score += 0
    
    # Liver
    if bilirubin >= 12: 
        sofa_score += 4
    elif bilirubin >= 6: 
        sofa_score += 3
    elif bilirubin >= 2: 
        sofa_score += 2
    elif bilirubin >= 1.2: 
        sofa_score += 1
    else:
        sofa_score += 0
    
    # Cardiovascular
    if map < 70: 
        sofa_score += 1
    else:
        sofa_score += 0
    
    # Renal
    if creatinine >= 5: 
        sofa_score += 4
    elif creatinine >= 3.5: 
        sofa_score += 3
    elif creatinine >= 2: 
        sofa_score += 2
    elif creatinine >= 1.2: 
        sofa_score += 1
    else:
        sofa_score += 0
    
    # Neurological
    if gcs < 6: 
        sofa_score += 4
    elif gcs < 10: 
        sofa_score += 3
    elif gcs < 13: 
        sofa_score += 2
    elif gcs < 15: 
        sofa_score += 1
    else:
        sofa_score += 0
    
    return sofa_score

# Streamlit app
st.title('Sepsis Assessment using qSOFA and SOFA')

# qSOFA criteria
st.subheader('Quick SOFA (qSOFA) Assessment')
resp_rate = st.number_input('Respiratory Rate (>=22 breaths/min)', 0, 50)
altered_mentation = st.checkbox('Altered mentation (GCS < 15)')
sysbp_qsofa = st.number_input('Systolic Blood Pressure (<=100 mmHg)', 0, 200)

qsofa_score = 0
if resp_rate >= 22: qsofa_score += 1
if altered_mentation: qsofa_score += 1
if sysbp_qsofa <= 100: qsofa_score += 1

st.write('qSOFA Score:', qsofa_score)

# Full SOFA Assessment if qSOFA is positive
if qsofa_score >= 2:
    st.subheader('Full SOFA Assessment')
    
    # Respiratory
    resp_ratio = st.number_input('PaO2/FiO2 ratio', 0, 500)
    
    # Coagulation
    platelets = st.number_input('Platelet count (x10^3/µL)', 0, 500)
    
    # Liver
    bilirubin = st.number_input('Total bilirubin (mg/dL)', 0.0, 20.0)
    
    # Cardiovascular
    map = st.number_input('Mean arterial pressure (mmHg)', 0, 200)
    
    # Renal
    creatinine = st.number_input('Serum creatinine (mg/dL)', 0.0, 20.0)
    
    # Neurological
    gcs = st.number_input('Glasgow Coma Scale', 3, 15)
    
    # Calculate full SOFA score
    sofa_score = calculate_sofa_score(resp_ratio, platelets, bilirubin, map, creatinine, gcs)
    st.write('Full SOFA Score:', sofa_score)
    
    if sofa_score >= 2:
        st.write('Sepsis confirmed based on full SOFA score.')
    else:
        st.write('Sepsis not confirmed based on full SOFA score.')
else:
    st.write('Sepsis not suspected based on qSOFA score.')
