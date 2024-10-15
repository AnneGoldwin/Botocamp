import streamlit as st
import pandas as pd
import random

# Load the exercises Excel data (from the same folder)
df = pd.read_excel('Bootcamp bestand.xlsx', sheet_name='Blad1')

# Function to randomly select exercises
def random_workout(muscle_group, num_exercises=3):
    exercises = df[muscle_group].dropna().tolist()
    if len(exercises) >= num_exercises:
        selected_exercises = random.sample(exercises, num_exercises)
    else:
        selected_exercises = exercises
    return selected_exercises

# Streamlit UI elements
st.title("Random Workout Generator")

# Muscle group selection
muscle_group = st.selectbox("Choose a muscle group", df.columns)

# Number of exercises
num_exercises = st.slider("Number of exercises", 1, 5, 3)

# Button to generate workout
if st.button("Generate Workout"):
    workout = random_workout(muscle_group, num_exercises)
    st.write(f"Here are your random {muscle_group} exercises:")
    for exercise in workout:
        st.write(f"- {exercise}")
