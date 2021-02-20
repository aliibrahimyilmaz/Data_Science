import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import joblib

st.title('Employee Churn Analysis')
html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML App </h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)

model = pickle.load(open("churn_pred_model", "rb"))

satisfaction_level = st.slider("What is the satisfaction level of the employee?", 0.0, 1.0, step = 0.01)
last_evaluation = st.slider("What is the last evaluation of the employee?", 0.0, 1.0, step = 0.01)
number_project = st.slider("How many of projects assigned to the employee?", 0, 10, step = 1)
average_montly_hours = st.slider("How many hours in average the employee worked in a month?", 50, 350, step = 1)
time_spend_company = st.slider("How many years spent by the employee in the company?"
                               , 0, 15, step = 1)
Work_accident = st.selectbox("Is the employee has had a work accident?", ('Yes', 'No'))
promotion_last_5years = st.selectbox("Is the employee has had a promotion in the last 5 years?", ('Yes', 'No'))
departments = st.selectbox("Select the employee's working department/division.", ("sales", "technical", "support", "IT", "product_mng", "marketing", "RandD", "accounting", "hr", "management"))
salary = st.selectbox("Select salary level of the employee.", ("low", "medium", "high"))


my_dict = {
    "satisfaction_level": satisfaction_level,
    "last_evaluation": last_evaluation,
    "number_project": number_project,
    "average_montly_hours": average_montly_hours,
    "time_spend_company": time_spend_company,
    "Work_accident": Work_accident,
    "promotion_last_5years": promotion_last_5years,
    "departments": departments,
    "salary" : salary
}

df = pd.DataFrame.from_dict([my_dict])


df['salary'] = df['salary'].apply(lambda x: ['low', 'medium', 'high'].index(x))
df['Work_accident'] = df['Work_accident'].apply(lambda x: ['No', 'Yes'].index(x))
df['promotion_last_5years'] = df['promotion_last_5years'].apply(lambda x: ['No', 'Yes'].index(x))
st.table(df.head())

scalerfile = 'scaler.sav'
scaler = pickle.load(open(scalerfile, 'rb'))

num_cols = df.columns[df.dtypes.apply(lambda c: np.issubdtype(c, np.number))]
df[num_cols] = scaler.transform(df[num_cols])
st.table(df.head())

columns = ['satisfaction_level', 'last_evaluation', 'number_project',
       'average_montly_hours', 'time_spend_company', 'Work_accident',
       'promotion_last_5years', 'salary', 'departments_IT',
       'departments_RandD', 'departments_accounting', 'departments_hr',
       'departments_management', 'departments_marketing',
       'departments_product_mng', 'departments_sales', 'departments_support',
       'departments_technical']

df2 = pd.get_dummies(df).reindex(columns=columns, fill_value=0)
st.table(df2)
pred = model.predict(df2)

#st.warning(pred)

if pred[0] == 1.0:
    st.warning("Bad news! This employee is churn one.")
else:
    st.success("Good news! This employee is loyal one")

