import streamlit as st
from PIL import Image
import streamlit.components as stc
import streamlit.components.v1 as components
import pandas as pd
import base64 #use to convert to plain text
import webbrowser

st.set_page_config(page_title="HeartBeats_App",page_icon="❤️",layout="centered")
img = Image.open("ImageLogoBmi.jpg")
st.image(img,use_column_width=True)

##===========================================================

state = st.session_state
if 'WEIGHT' not in state:
    state.WEIGHT = 1.0
if 'HEIGHT' not in state:
    state.HEIGHT = 1.00

def _set_values_cb():
    state.WEIGHT = state['weight']
    state.HEIGHT = state['height']

##=============================================================

#--Header
Intro_text ='<p style="font-family:Bellota;color:black;font-size:18px;"> .......the health beats of your heart💛. BMI is not a diagnostic tool. But in a certain way, it reflects your lifestyle. Excess body fat accumulates may puts you at risk of health problems such as diabetes, high blood pressure and even heart diseases. Lets get started by finding out your BMI." </p>'
st.markdown(Intro_text,unsafe_allow_html=True)

#--Image for Header
img = Image.open("ImageBMIs.jpg")
st.image(img,use_column_width=True)

#--Input Name---------------------------------------------------

st.subheader("Please provide your name and your mood today.")
with st.form(key="FormInfo"):
    col1,col2=st.columns([2,3])
    with col1:
        fname = st.text_input("Enter your Name",max_chars=15)
    with col2:
        mood = st.radio("It is said that mental health affects physical health. How are you feeling today😁-🤠-😤-😢?",
            ("Please select one👇🏻:","Just another common day","Angry, Sad, Lousy","Happy, Excited, Peaceful"))
    submit_info=st.form_submit_button(label="Click To START")

    if submit_info:
        if fname=="":
            st.warning("Dear stranger, please input your name.")
        else:
            if mood == "Just another common day":
                st.markdown(f"Dear {fname}. Your mood is just -a common day-. We have a quote for you today.")
                img = Image.open("QuoteNormal.jpg")
                st.image(img,use_column_width=True)
            elif mood == "Angry, Sad, Lousy":
                st.markdown(f"Dear {fname}, your mood is not so good-. We have a quote for you today.")
                img = Image.open("QuoteBad.jpg")
                st.image(img,use_column_width=True)
            elif mood == "Happy, Excited, Peaceful":
                st.markdown(f"Dear {fname}, your mood is good-. We have a quote for you today.")
                img = Image.open("QuoteHappy.jpg")
                st.image(img,use_column_width=True)
            else:
                st.warning(f"Dear {fname}, you have not select your mood yet. Please select one and [click to START]")
st.text("")
st.text("")

#--Calculate BMI-------------------------------------------------------

st.subheader("BMI Calculator - Please input your weight and height.")
c1,c2,c3=st.columns([4,0.5,2])
with c1:
    img = Image.open("ImageBody.jpg")
    st.image(img,use_column_width=True)
with c2:
    st.text("")
with c3:
    state.WEIGHT = st.number_input("Enter Weight (kg)",min_value=1.0, max_value=150.0, value=state.WEIGHT, step=0.5, on_change=_set_values_cb, key='weight')
    state.HEIGHT = st.number_input('Enter height (m)', min_value=0.8, max_value=2.5, value=state.HEIGHT, step=0.1, on_change=_set_values_cb, key='height')
    if st.button("Calculate"):
        if fname =="":
            st.warning(f"Dear Stranger,☝️please input your name and [click to START] button")
            pass
        else:
            BMI = round(state.WEIGHT/(state.HEIGHT**2), 1)
            st.success(f"Your BMI is {BMI}")    
            df=pd.DataFrame({"fullname":fname,"fmood":mood,"weightkg":state.WEIGHT,"heightm":state.HEIGHT,"BMIc":BMI}, index=[0])

#--BMI Classification------------------------------------------------

BMI = round(state.WEIGHT/(state.HEIGHT**2), 1)
index_bmi = [18.5, 23, 27.5]
index_label = ['underweight','normalweight','overweight','obesity']
index_result = {"underweight":"can be better", "normalweight":"is excellent","overweight":"is not too good","obesity":"is poor"}
index_action = {"underweight":"You risk weakened immune system, fragile bones and feeling tired.", "normalweight":"Cool. You are healthy looking","overweight":"You risk high blood pressure, diabetes, heart disease, certain cancers, bone & joint disorders","obesity":"You risk high blood pressure, diabetes, heart disease, certain cancers, bone & joint disorders"}
index_img = {'underweight':'ImageUnder.jpg','normalweight':'ImageNormal.jpg','overweight':'ImageOver.jpg','obesity':'ImageObesity.jpg'}

if BMI <= index_bmi[0]:
    level = index_label[0]
elif BMI <= index_bmi[1]:
    level = index_label[1]
elif BMI <= index_bmi[2]:
    level = index_label[2]
else:
    level = index_label[3]
    
for r in index_result:
    if level == r:  
        result = index_result[level]
for a in index_action:
    if level == a:  
        action = index_action[level]
for i in index_img:
    if level == i:  
        bmi_img = index_img[level]

#--Report----------------------------------------------------------------------

if state.HEIGHT > 1:
    #Greeting
    if fname == "":
        fname = "Stranger"
        pass
    else:
        fname = fname

    if BMI == 1:
        BMI = " ...☝️click calculate button "
    else:
        BMI = BMI

    st.markdown("")
    st.info("##### BMI Report") 
    st.markdown(f"#### Dear {fname},")

    Rpt_text ='<p style="font-family:Arial;color:black;font-size:18px;"> Thank you for using HeartBeats App. BMI measures the relationship between your weight and height to calculate the amount of body fat you have. The higher your BMI, the higher the estimate fat in your body." </p>'
    st.markdown(Rpt_text,unsafe_allow_html=True)

    #Result
    col1,col2=st.columns([3,3])
    with col1:
        img = Image.open(bmi_img)
        st.image(img,use_column_width=True) 
    with col2:
        st.info(f"##### Your BMI is {BMI}")

        Rpt_result =f'<p style="font-family:Arial;color:black;font-size:18px;"> Generally you are categorized as {level}. Looks like your health management {result}. {action}." </p>'
        st.markdown(Rpt_result,unsafe_allow_html=True)

    #General Information
    img = Image.open("ImageGeneral.jpg")
    st.image(img,use_column_width=True)

    
    #--Feedback------------------------------------------------

    st.subheader("Feedback and Wish List")
    st.info(f"""Dear {fname}, We hope you have an enjoyable experience with this simple apps. You are welcome to provide feedback for future improvement. We welcome any idea on health related apps that you think is useful, helpful or entertaining. We look forward to create better and more apps in the near future. 

        Stay happy. Stay healthy.

        """) 

    st.markdown('<a href="mailto:alice.python21@gmail.com">Sent feedback to this email !</a>', unsafe_allow_html=True)

    st.markdown("")
    img = Image.open("signature.jpg")
    st.image(img,use_column_width=True)
    
else:
    pass

