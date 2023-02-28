import pickle
from flask import Flask, request

app = Flask(__name__)

model_pickle=open('./classifier.pkl', "rb")
clf=pickle.load(model_pickle)

@app.route('/ping', methods=['GET'])
def ping():
    return {"message": "Pinging the model is successful!"}

@app.route('/predict', methods=['POST'])
def prediction():
    loan_req=request.get_json()

    if loan_req['Gender']=='Male':
        gender = 0
    else:
        gender = 1

    if loan_req['Married'] == 'Unmarried':
        marital_status = 0
    else:
        marital_status = 1

    applicant_income=loan_req['ApplicantIncome']
    loan_amt= loan_req['LoanAmount']/1000

    credit_history=loan_req['Credit_History']

# Input Expectation
    input_data=[[gender, marital_status, applicant_income, loan_amt, credit_history]]

#Generate Inference
    predictions= clf.predict(input_data)
    if predictions==0:
        pred="Rejection"
    else:
        pred='Approved'

    return {"Loan Approval Status": pred}



@app.route('/get_params', methods=['GET'])
def get_parameters():
   parameters= {"Gender": "Male",
                "Married": "Unmarried",
                "ApplicantIncome":500000,
                "LoanAmount": 200000,
                "Credit_History": 0.0
}
   return parameters