import streamlit as st

st.title("Obi's Hearts Risk Prediction")
st.header("Demo Day Presentation")

st.write("To be filled by a Physician")
st.text_input("What is your name")
st.number_input("Enter your age?")
race = st.radio("Whats your sex?", 
                ["Male","Female"])
st.number_input("SBP")
st.selectbox("Choose one?", 
            ["black","white","Red","Blue"])
st.select_slider("Your class",
                 ["1","2","3","4"])


## st.slider("Pick one",
##          ["A","B","C","BDlue"])

st.button("Predict")

