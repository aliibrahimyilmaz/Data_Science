import streamlit as st
import pickle
import pandas as pd

st.title('Employee Churn Analysis Prediction')

html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML App </h2>
</div>"""

st.markdown(html_temp, unsafe_allow_html=True)

model = pickle.load(open("rf_model", "rb"))
#age = st.selectbox("What is the satisfaction level of the employee?", (1,2,3))
satisfaction = st.slider("What is the satisfaction level of the employee?", 0.0, 1.0, step = 0.1)
evaluation = st.slider("What is the the last evaluation of the employee?", 0.0, 1.0, step = 0.1)
pro_num = st.slider("What is the number of project that the employee involved?", 0, 15, step=1)
ave_hour = st.slider("What is the average montly hours that the employee worked?", 0, 250, step=1)
time_spend=st.selectbox("How many years has the employee so far spent?", (1,2,3,4,5,6,7,8,9,10))

my_dict={'satisfaction_level':satisfaction,
        'last_evaluation':evaluation,
        'number_project':pro_num,
        'average_montly_hours':ave_hour,
        'time_spend_company':time_spend}

df = pd.DataFrame.from_dict([my_dict])

columns = ['satisfaction_level',
           'last_evaluation',
           'number_project',
           'average_montly_hours',
           'time_spend_company',
           'Work_accident',
           'promotion_last_5years',
           'Departments',
           'salary']

df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)

#st.table(df)

prediction = model.predict(df)

if int(prediction[0]) == 0:
    st.success("The employee will NOT CHURN.")
else:
    st.success("The employee will CHURN.")


# büyük dosyalari kullanirken st.cache kullanilabilir