import streamlit as st

#text/title
st.title("Streamlit Tutorial")
st.text("Hello Streamlit")

#header/subheader
st.header("This is a header")
st.subheader("This is a subheader")

#markdown
st.markdown("### This is a Markdown")
st.markdown("** This is also a markdown **")

#colorfull Text
st.success("Successfull")
st.info("This is an information")

#st.help(st.info)
st.warning("This is a warning")
st.error("This is an error")
st.help(range)

#writing text
st.write("Text with write func")

#images
from PIL import Image
im = Image.open("ali.jpg")
st.image(im, width=200, caption="GD")
#st.help(st.image)

#video&audio
vid_file = open("Pop_8D_2020.mp3", "rb")
st.video(vid_file)

#checkbox
if st.checkbox("Show/Hide"):
    st.text("I'm showing because you checked the box")
    
st.checkbox("Hide/Seek")

#radio buttons
status = st.radio("What is your status?", ("Active", "Inactive"))
#st.help(st.radio)
    
if status == "Active":
    st.success("You are active!")
else:
    st.warning("You are inactive")

#selectbox
dropdown = st.selectbox('Pick your status', ('active', 'inactive'))
st.write('You picked:', dropdown)
if dropdown == "active":
    st.success("wooo!")
else:
    st.warning("damn!")
    
occupation = st.selectbox('Select Your Occupation', ('Programmer', 'DS', "Developer"))
st.write('You picked:', occupation)

#multiselect
location = st.multiselect("where do you work?", ("London", "Istanbul", "Moscow", "Berlin"))
st.write("You selected: ", len(location), "locations")

#slider
level = st.slider("What is your level", 0,40, 10, step=5)
st.write("You selected", level)

#button
st.button("Simple Button")

if st.button("About"):
    st.text("Streamlit is Cool")
else:
    st.text("Hasta Pronto")
    
#text input
firstname = st.text_input("Enter Your Firstname")  # tek satirlik veri icin
if st.button("Submit"):
    st.success(firstname.title())

#text area
message = st.text_area("Enter Your Text", "Type Here...")
if st.button("submit"):
    result = message.title()
    st.success(result)
    
#date input
import datetime
today = st.date_input("Today is", datetime.datetime.now())

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

#time input
the_time = st.time_input("The time is", datetime.time(8,45))

#Raw_Data
st.text("Display Text")

#single line code
st.code("import numpy as np")

#multiple line codes
with st.echo():
    import numpy as np
    import pandas as pd
    
#progress bar
import time
my_bar = st.progress(0)
for p in range(50):
    my_bar.progress(p+1)
    #time.sleep(0.1)
    
#spinner
#import time
#with st.spinner("Waiting......"):
    #time.sleep(3)
#st.success("Finished")
#st.balloons()

if st.button('Baloons'):
    st.balloons()

st.title("Churn Probability of a Single Customer")
st.sidebar.title("Churn Probability of a Single Customer")

#st.markdown(html_temp, unsafe_allow_html=True)
st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                width: 1000px;
            }}
        </style>
    ''',
    unsafe_allow_html=True)


import pickle
import pandas as pd

df = pickle.load(open("df_saved.pkl", "rb"))

st.write(df.head())