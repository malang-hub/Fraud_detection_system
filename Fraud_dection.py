import streamlit as st
import  pandas as pd 
import joblib

model=joblib.load("fraud_detection_pipline.pkl")

st.title("Fraud Dection App")
st.markdown("Please enter the Transaction detail and use the predict button")
st.divider()

transaction_type=st.selectbox("transaction type",["PAYMENT","TRANSFER","CASHOUT",])
amount=st.number_input("Amount",min_values=0.0,value=10000)
oldbalanceorg=st.number_input("Old Balance(Sender)",min_value=0.0,value=10000)
newbalanceorig=st.number_input("New Balance(sender)",min_value=0.0,value=9000)
oldbalanceDest=st.number_input("Old Balance(Receiver)",min_value=0.0,value=0.0)
newbalanceDest=st.number_input("New Balance(Receiver)",min_value=0.0,value=0.0)

if st.button("Predict"):
    input_data=pd.DataFrame([{
        "type":transaction_type,
        "amount":amount,
        "oldbalanceorg":oldbalanceorg,
        "newbalanceorig":newbalanceorig,
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest":newbalanceDest
    }])
    
    prediction=model.predict(input_data)[0]
    st.subheader(f"Prediction: '{int(prediction)}'")
    if  prediction==1:
        st.error("This Transaction can be Fraud")
    else:
        st.success("This Transaction look like it is not a Fraud")
        