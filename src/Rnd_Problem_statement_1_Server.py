import streamlit as st 
import pickle

print('Successfully executed ')

model = pickle.load(open('Rnd_Problem_statement_1.pkl', 'rb'))

def predict(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    prediction=model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    return prediction
    
def main():
    st.title("Heart Disease Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Heart Disease Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("Age","Type Here")
    sex = st.text_input("Sex","Type Here")
    cp = st.text_input("CP","Type Here")
    trestbps = st.text_input("Tres BP","Type Here")
    chol = st.text_input("Cholestrol","Type Here")
    fbs=st.text_input("FBS","Type Here")
    restecg = st.text_input("Rest Ecg","Type Here")
    thalach=st.text_input("Thalach","Type Here")
    exang=st.text_input("Exang","Type Here")
    oldpeak=st.text_input("Old Peak","Type Here")
    slope =st.text_input("Slope","Type Here")
    ca=st.text_input("Ca","Type Here")
    thal=st.text_input("Thal","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

main()
