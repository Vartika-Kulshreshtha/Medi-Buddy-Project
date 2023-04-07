# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:22:20 2023

@author: nandi
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/nandi/OneDrive/Desktop/MEDI-BUDDY/trained_model_heart.sav','rb')) 


#creating a function
def heart_disease_prediction(input_data):
    

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
      return'The Person does not have a Heart Disease'
    else:
      return'The Person has Heart Disease'



def main():
    
    #giving a title
    st.title('Heart Disease Prediction Web App')
    
    
    #getting the input data from the user
    
    age = st.text_input('Age')
    sex=st.text_input('Sex')
    cp=st.text_input('Cp')
    trestbps=st.text_input('Trestbps')
    chol=st.text_input('Cholestrol')
    fbs =st.text_input('Fasting Blood Sugar')
    restecg =st.text_input('Resting Electrocardiographic results')
    thalach =st.text_input('Maximum Heart Rate achieved')
    exang =st.text_input('Exercise Induced Angina')
    oldpeak =st.text_input('ST depression induced by exercise')
    slope =st.text_input('Slope of the peak exercise ST segmen')
    ca =st.text_input('Major vessels colored by flourosopy ')
    thal =st.text_input('thal defect')
    
    #code for Prediction
    diagnosis=''
    
    #creating a buttton for prediction
    if st.button('Heart Disease Test Result'):
        diagnosis = heart_disease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
    st.success(diagnosis)
    
    
    
    
if __name__=='__main__':
    main()

    