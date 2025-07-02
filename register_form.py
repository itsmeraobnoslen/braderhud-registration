import streamlit as st

st.title("PILOT OF THE YEAR")

name = st.text_input("PILOT NAME:")
email = st.text_input("EMAIL MO")
phone = st.text_input("NUMBER MO KUNG MERON KA")
gender = st.radio("Gender", ["Male", "Female", "Prefer not to say"])
education = st.selectbox("ANONG KASO MO", ["RAPE", "ADIK", "BABAERO", "HOLDAPER"])
address = st.text_area("HOME TOWN/REPPIN")
birthdate = st.date_input("KELAN KA INIRE")

if st.button("Submit"):
    st.success("Salamat sa pagsuko mo... este pag-register!")
    st.write("### 📋 DETALYENG IBINIGAY")
    st.write(f"**Pilot Name:** {name}")
    st.write(f"**Email Mo:** {email}")
    st.write(f"**Number Mo Kung Meron Ka:** {phone}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Kaso Mo:** {education}")
    st.write(f"**Reppin:** {address}")
    st.write(f"**Kailan Ka Inire:** {birthdate}")
