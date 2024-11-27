import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Load the dataset
data = pd.read_csv('data/Urinalysis_Cleaned.csv')

# Ensure consistent column naming
data.columns = data.columns.str.strip().str.replace(' ', '_')

# Select features and target
features = [
    'Age', 
    'Gender_Num',
    'Color_Num', 
    'Transparency_Num', 
    'Glucose_Num', 
    'Protein_Num', 
    'pH', 
    'Specific_Gravity', 
    'Epithelial_Cells_Num', 
    'Mucous_Threads_Num', 
    'Amorphous_Urates',  # Use the categorical feature
    'Bacteria_Num'
]
target = 'Diagnosis_Num'

# Prepare the data
X = data[features]
y = data[target]

# Encode categorical feature 'Amorphous_Urates' into numeric values for the model
X = pd.get_dummies(X, columns=['Amorphous_Urates'], drop_first=True)

# Train a RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Streamlit App
st.title('UTI Prediction App')

# User inputs
age = st.text_input('Age', value='25')
try:
    age = float(age)
except ValueError:
    st.error('Please enter a valid age.')
    st.stop()

gender = st.selectbox('Gender', options=['MALE', 'FEMALE'])
gender_num = 1 if gender == 'MALE' else 0

color = st.selectbox('Urine Color', options=list(data['Color'].unique()))
color_num = data.loc[data['Color'] == color, 'Color_Num'].values[0]

transparency = st.selectbox('Urine Transparency', options=list(data['Transparency'].unique()))
transparency_num = data.loc[data['Transparency'] == transparency, 'Transparency_Num'].values[0]

glucose = st.selectbox('Glucose in Urine', options=list(data['Glucose'].unique()))
glucose_num = data.loc[data['Glucose'] == glucose, 'Glucose_Num'].values[0]

protein = st.selectbox('Protein in Urine', options=list(data['Protein'].unique()))
protein_num = data.loc[data['Protein'] == protein, 'Protein_Num'].values[0]

pH = st.text_input('pH Level', value='6.0')
try:
    pH = float(pH)
except ValueError:
    st.error('Please enter a valid pH level.')
    st.stop()

specific_gravity = st.text_input('Specific Gravity', value='1.020')
try:
    specific_gravity = float(specific_gravity)
except ValueError:
    st.error('Please enter a valid specific gravity.')
    st.stop()

epithelial_cells = st.selectbox('Epithelial Cells', options=list(data['Epithelial_Cells'].unique()))
epithelial_cells_num = data.loc[data['Epithelial_Cells'] == epithelial_cells, 'Epithelial_Cells_Num'].values[0]

mucous_threads = st.selectbox('Mucous Threads', options=list(data['Mucous_Threads'].unique()))
mucous_threads_num = data.loc[data['Mucous_Threads'] == mucous_threads, 'Mucous_Threads_Num'].values[0]

# Use the categorical feature 'Amorphous_Urates'
amorphous_urates = st.selectbox('Amorphous Urates', options=list(data['Amorphous_Urates'].unique()))

bacteria = st.selectbox('Bacteria in Urine', options=list(data['Bacteria'].unique()))
bacteria_num = data.loc[data['Bacteria'] == bacteria, 'Bacteria_Num'].values[0]

# Prediction button
if st.button('Predict'):
    # Prepare the input data for prediction, matching the structure of the training data
    input_data = pd.DataFrame(
        {
            'Age': [age], 
            'Gender_Num': [gender_num], 
            'Color_Num': [color_num], 
            'Transparency_Num': [transparency_num], 
            'Glucose_Num': [glucose_num], 
            'Protein_Num': [protein_num], 
            'pH': [pH], 
            'Specific_Gravity': [specific_gravity], 
            'Epithelial_Cells_Num': [epithelial_cells_num], 
            'Mucous_Threads_Num': [mucous_threads_num], 
            'Bacteria_Num': [bacteria_num]
        }
    )
    
    # Handle categorical encoding for 'Amorphous_Urates'
    for category in X.columns:
        if 'Amorphous_Urates_' in category:
            input_data[category] = 1 if category == f'Amorphous_Urates_{amorphous_urates}' else 0

    # Align the input data to the model's training data format
    input_data = input_data.reindex(columns=X.columns, fill_value=0)
    
    # Prediction
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.markdown("<h3 style='color: red;'>UTI POSITIVE</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color: green;'>UTI NEGATIVE</h3>", unsafe_allow_html=True)
