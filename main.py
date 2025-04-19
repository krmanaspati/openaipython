import streamlit as st
from langchain_helper import generate_restaurant_name_and_items

st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick an option", ("indian", "American"))

if cuisine:
    response = generate_restaurant_name_and_items(cuisine)
    if isinstance(response, dict):
        # Clean and display the restaurant name
        restaurant_name = response['restaurant_name'].strip().strip('"')
        st.header(restaurant_name)

        # Clean and display the menu items
        menu_items = response['menu_items'].strip().split("\n")
        st.write("****Menu Items****")
        for item in menu_items:
            st.write("-", item.strip())
    else:
        st.error("Unexpected response format. Please check the backend.")