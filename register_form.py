import streamlit as st

st.title("Braderhud Registration Form")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
gender = st.radio("Gender", ["Male", "Female", "Prefer not to say"])
education = st.selectbox("Education Level", ["High School", "College", "Graduate", "Other"])
address = st.text_area("Address")
birthdate = st.date_input("Birthdate")

if st.button("Submit"):
    st.success("Registration Submitted Successfully!")
    st.write("### 📋 Your Info:")
    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Education:** {education}")
    st.write(f"**Address:** {address}")
    st.write(f"**Birthdate:** {birthdate}")
