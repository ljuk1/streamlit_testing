import streamlit as st


def emission_calculation(distance, fuel_type):
    if fuel_type == "Diesel":
        return distance * 0.5
    elif fuel_type == "Gasoline":
        return distance * 0.3
    elif fuel_type == "Electric":
        return distance * 0.1
    elif fuel_type == "Cardboard Boxes":
        return distance * 99999999
    else:
        return "Did you try running on cow poop? That's not supported!!!!"