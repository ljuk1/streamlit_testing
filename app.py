import streamlit as st


st.title("Emissions Calculating Application - by Lukasz 'Mamacita Seducer' Janicki")


st.write("This dashboard will perform valuable calculations for my mamacita.")


love = st.slider("How much do you love me mamcita?", 0, 100, 50)  # min=0, max=100, default=50


st.write(f"You love me mamcita {love}%. That's {'MUCH BUENO MI AMOR' if love >= 99 else 'SAD FACE'}!")