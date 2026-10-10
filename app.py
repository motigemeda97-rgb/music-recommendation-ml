
import streamlit as st
import joblib
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="AI Music Predictor",
    page_icon="🎵",
    layout="centered"
)

# Load the trained AI model
model = joblib.load("music-recommender.joblib")

# Page heading
st.title("🎵 AI Music Genre Predictor")
st.markdown(
    "### Discover your predicted music genre"
)
st.write(
    "Enter your details below and let our machine-learning "
    "model make a prediction."
)

st.divider()

# User inputs
st.subheader("👤 Your details")

age = st.number_input(
    "Your age",
    min_value=1,
    max_value=100,
    value=21,
    help="Enter your age in years."
)


gender_option = st.selectbox(
    "Select your gender",
    options=["Male", "Female"],
    help="Choose your gender."
)

gender = 1 if gender_option == "Male" else 0


st.caption("Your inputs are used to generate a model prediction.")

# Prediction
if st.button("🎶 Predict my music genre", use_container_width=True):
    input_data = pd.DataFrame(
        [[age, gender]],
        columns=["age", "gender"]
    )

    prediction = model.predict(input_data)

    st.divider()
    st.subheader("✨ Your prediction")
    st.success(f"Your predicted genre is **{prediction[0]}**")

st.divider()
st.caption("Built with Python, Streamlit, and machine learning.")
