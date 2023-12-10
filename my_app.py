import streamlit as st
import pickle
import pandas as pd
from sklearn.linear_model import Lasso
from git import Object
import numpy as np



#title
st.title("Employee Churn Analysis")

# images



st.text("    ")

#pickles







#Departments = st.selectbox('Select Department name of the Employee', ['IT', 'sales', 'temp', 'engineering', 'support', 'finance', 'Procurement', 'Admin', 'management', 'marketing', 'product'])

choice = st.sidebar.selectbox('Department',
        ("Information Technology (IT)",
        "Research and Development (R & D)",
        "Accounting",
        "Human Resources",
        "Management",
        "Marketing",
        "Product Management",
        "Sales",
        "Support",
        "Technical"),
    )
if choice == "Information Technology (IT)":
        Departments = "IT"
elif choice == "Research and Development (R & D)":
        Departments = "RandD"
elif choice == "Accounting":
        Departments = "accounting"
elif choice == "Human Resources":
        Departments = "hr"
elif choice == "Management":
        Departments = "management"
elif choice == "Marketing":
        Departments = "marketing"
elif choice == "Product Management":
        Departments = "product_mng"
elif choice == "Sales":
        Departments = "sales"
elif choice == "Support":
        Departments = "support"
elif choice == "Technical":
        Departments = "technical" 

choice2 = st.sidebar.radio('Salary Level', ["Low", "Medium", "High"])
if choice2 == "Low":
 salary = "low"
elif choice2 == "Medium":
 salary = "medium"
elif choice2 == "High":
 salary = "high"

choice3 = st.sidebar.radio('promotion_last_5years', ["Yes", "No"])
if choice3 == "Yes":
        promotion_last_5years = 1
else:
        promotion_last_5years = 0

choice4 = st.sidebar.radio('Work_accident', ["Yes", "No"])
if choice4 == "Yes":
        Work_accident = 1
else:
        Work_accident = 0

satisfaction_level = st.sidebar.slider("What was the overall satisfaction level of the employee", 0.0, 1.0, 0.5)
        
average_montly_hours = st.sidebar.slider("Enter average monthly hours worked by the employee", 0, 240, 120)

last_evaluation = st.sidebar.slider("What was the score of the employee in the last evaluation?", 0.0, 1.0, 0.5)
number_project = st.sidebar.slider("Enter number of projects the employee is currently working on", 0, 20, 10)
#promotion_last_5years = st.radio("Has the employee been promoted recently?", (1, 0))


#salary = st.radio("Choose salary range of the employee", ("high", "medium", "low"))

time_spend_company = st.sidebar.slider("Enter employee tenure at the organization (in years)", 0, 30, 1)


    
#data
my_dict = {
	"satisfaction_level": satisfaction_level,	
    	"last_evaluation": last_evaluation,
    	"number_project": number_project,
    	"average_montly_hours": average_montly_hours,
	"time_spend_company": time_spend_company,
	"promotion_last_5years": promotion_last_5years,
    "Departments ": Departments,
    "salary" : salary,
    "Work_accident":Work_accident

}



columns = pickle.load(open("columns2", 'rb'))
model = pickle.load(open("KNN_Model","rb"))


#final_scale = pickle.load(open("cluster_features_scaled", 'rb'))

df = pd.DataFrame([my_dict])
#df = pd.get_dummies(df)
#df = df.reindex(columns=columns, fill_value=0)
#df = final_scale.transform(df)
st.markdown("""<h3 style='text-align:left; color:#000;'>Your Selected</h3>
""", unsafe_allow_html=True)
st.write(df)





#evaluation
if st.button("Predict", type="primary"):
    pred = model.predict(df)
    
    if pred==0:
     st.error("It looks like s/he is leaving. ")
     
     
    else:
     st.success("It looks like s/he Will Stay")

    
   

    
#pred = model.predict(df)
#pred_xgb = ['Left' if pred == 1 else 'Stayed']
    

    

    


    