import streamlit as st
from calculation_methods import * 
 

##### background CSS 

background_css = """
<style>
html, body, [class*="css"]  {
    background-image: url('https://www.jocooks.com/wp-content/uploads/2022/04/tacos-al-pastor-feature-1.jpg');
    background-size: cover !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
}
.stApp {
    background: transparent !important;
}

"""

st.markdown(background_css, unsafe_allow_html=True)

##########   BACKGROUND CSS 




st.title("Emissions Calculating Application - by Lukasz Janicki")


st.write("This dashboard will perform valuable calculations for my mamacita.")


st.header("Emissions Calculation Section")

distance = st.number_input("Miles the truck travelled:", min_value=0.0, value=10.0)

fuel_type = st.selectbox("Type of fuel used:", ["Diesel", "Gasoline", "Electric", "Cardboard Boxes"]) 


###############

if st.button("Calculate Your Emissions SandyES!!!!!!"):
    
    result = emission_calculation(distance, fuel_type)
    
    st.write(f"Total crap emitted: {result} kg")



############

love = st.slider("How much do you love me mamcita?", 0, 100, 50)  # min=0, max=100, default=50


st.write(f"You love me mamcita {love}%. That's {'MUCH BUENO MI AMOR' if love >= 99 else 'SAD FACE'}!")
