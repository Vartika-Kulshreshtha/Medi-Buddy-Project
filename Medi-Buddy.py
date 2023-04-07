# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:22:17 2023

@author: nandi
"""



import sklearn
import pickle
import streamlit as st
from streamlit_option_menu import option_menu



# loading the saved models

diabetes_model = pickle.load(open('diabetes_model (3).sav','rb'))

heart_disease_model = pickle.load(open('heart_disease_model (1).sav','rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Medi-Buddy',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['activity','heart'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies (0-17)')
        
    with col2:
        Glucose = st.number_input('Glucose Level (0-199)')
    
    with col3:
        BloodPressure = st.number_input('Blood Pressure value (0-122 mm Hg)')
    
    with col1:
        SkinThickness = st.number_input('Skin Thickness value (0-99 mm)')
    
    with col2:
        Insulin = st.number_input('Insulin Level (0-846 U/mL)')
    
    with col3:
        BMI = st.number_input('BMI value (0-67.1)')
    
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value (0.08-2.42)')
    
    with col2:
        Age = st.number_input('Age of the Person (21-81)')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'THE PERSON IS DIABETIC'
          st.success(diab_diagnosis)
          
          st.button('Precautions:')
          st.button('Keep your blood pressure and cholesterol under control')
          st.button('Make a commitment to managing your diabetes')
          st.button('Dont smoke')
          
          
          
          
          
        else:
          diab_diagnosis = 'THE PERSON IS NOT DIABETIC'
          st.success(diab_diagnosis)

        
    



# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age =st.number_input('Age (29-77)')
        
    with col2:
        sex =st.number_input('Sex (1-Male,0-Female)')
        
    with col3:
        cp =st.number_input('Chest Pain types (0-3)')
        
    with col1:
        trestbps =st.number_input('Resting Blood Pressure (94-200 mm Hg)')
        
    with col2:
        chol =st.number_input('Serum Cholestoral in mg/dl (126-564 mg/dL)')
        
    with col3:
        fbs =st.number_input('Fasting Blood Sugar (0-False,1-True)')
        
    with col1:
        restecg =st.number_input('Resting Electrocardiographic results (0-2)')
        
    with col2:
        thalach =st.number_input('Maximum Heart Rate achieved (71-202)')
        
    with col3:
        exang =st.number_input('Exercise Induced Angina (1-Yes,0-No)')
        
    with col1:
        oldpeak =st.number_input('ST depression induced by exercise (0-6.2)')
        
    with col2:
        slope =st.number_input('Slope of the peak exercise ST segment (0-2)')
        
    with col3:
        ca =st.number_input('Major vessels colored by flourosopy (0-3)')
        
    with col1:
        thal =st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        


        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
          st.success(heart_diagnosis)
          
          st.button('Precautions:')
          st.button('Eat a heart-healthy diet')
          st.button('Maintain a healthy weight')
          st.button('Give up smoking and alcohol')
          st.button('Keep your blood pressure under control')
          
         
         
                             
                             
        else:
          heart_diagnosis = 'The person does not have any heart disease'
          st.success(heart_diagnosis)
         
        
    
        

