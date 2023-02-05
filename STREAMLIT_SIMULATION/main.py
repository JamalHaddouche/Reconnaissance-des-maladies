import streamlit as st
import pickle
from PIL import Image

model=pickle.load(open("text_classifier", "rb"))
vectorizer=pickle.load(open("tf_idf", "rb"))

st.markdown("<h1 style='text-align: center; color:#1278a9 ;'>Reconnaissance des maladies</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>realisé par Jamal Haddouche</p>", unsafe_allow_html=True)
image1 = Image.open('img.jpg')
st.image(image1, use_column_width=True)
text = st.text_input(' how are you felling Right now?', ' ')
symp = [text]
transform_vect =vectorizer.transform(symp).toarray()
maladie = model.predict(transform_vect)[0]
def predictDisease(maladie):
    if maladie == 0:
        return "Emotional pain"
    elif maladie == 1:
        return "Hair falling out"
    elif maladie == 2:
        return "Heart hurts"
    elif maladie == 3:
        return"Infected wound"
    elif maladie == 4:
        return "Foot achne"
    elif maladie == 5:
        return "Shoulder pain"
    elif maladie == 6:
        return "Injury from sports"
    elif maladie == 7:
        return "Skin issue"
    elif maladie == 8:
        return "Stomach ache"
    elif maladie == 9:
        return "Knee pain"
    elif maladie == 10:
        return "Joint pain"
    elif maladie == 11:
        return "Hard to breath"
    elif maladie == 12:
        return "Head ache"
    elif maladie == 13:
        return "Body feels weak"
    elif maladie == 14:
        return "Feeling Dizzy"
    elif maladie == 15:
        return "Back pain"
    elif maladie == 16:
        return "Open wound"
    elif maladie == 17:
        return "Internal pain"
    elif maladie == 18:
        return "Blurry vision"
    elif maladie == 19:
        return "Acne"
    elif maladie == 20:
        return "Muscle pain"
    elif maladie == 21:
        return "Neck pain"
    elif maladie == 22:
        return "Cough"
    elif maladie == 23:
        return "Ear ache"

    else:
        return "Feeling cold"
st.write(predictDisease(maladie))
