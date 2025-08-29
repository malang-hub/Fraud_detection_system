# 🚨 Fraud Detection System  

A Machine Learning-powered **Fraud Detection App** built with **Streamlit**.  
This project helps in identifying potentially fraudulent financial transactions by analyzing transaction details.  

---

## 📌 Features  
- User-friendly **Streamlit web app**  
- Input transaction details (type, amount, balances, etc.)  
- Real-time **fraud prediction** using a trained ML model  
- Provides instant feedback:
  - ✅ Safe Transaction  
  - ❌ Potential Fraud  

---

## 📂 Project Structure  

├── faud.ipynb # Jupyter Notebook for training & experimentation
├── Fraud_dection.py # Streamlit app for fraud detection
├── fraud_detection_pipline.pkl # Trained ML model pipeline
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/fraud-detection.git
   cd fraud-detection
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
(Make sure fraud_detection_pipline.pkl is in the project folder.)

▶️ Usage
Run the Streamlit app:

bash
Copy code
streamlit run Fraud_dection.py
Open the browser at http://localhost:8501/ to access the app.

📊 Input Fields
Transaction Type: PAYMENT, TRANSFER, or CASHOUT

Amount: Transaction amount

Old Balance (Sender)

New Balance (Sender)

Old Balance (Receiver)

New Balance (Receiver)

🧠 Model
The model is stored in fraud_detection_pipline.pkl

Trained using supervised machine learning techniques

Capable of classifying transactions as:

0 → Not Fraud

1 → Fraud

📌 Example Prediction
If the transaction looks suspicious:

makefile
Copy code
Prediction: 1
This Transaction can be Fraud 🚨
If the transaction is safe:

vbnet
Copy code
Prediction: 0
This Transaction looks like it is not a Fraud ✅
