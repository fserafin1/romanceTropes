import streamlit as st

st.set_page_config(page_title="Romance Tropes", page_icon="💕", layout="centered")

st.subheader("Welcome to", text_alignment="center", )
st.title("💕Romance Tropes! 💕", text_alignment="center"
         )
info = st.selectbox(
    "Select to Learn More about the App:", 
    ["Description", "About", "Mission"],
    key="main_menu",
    width=210

)

if info == "Description":
    st.write("Romance Tropes is an app designed to help readers find tropes within romance novels. It uses machine learning to analyze book descriptions and predict which tropes are present, making it easier for readers to discover books that match their interests.")
elif info == "About":
    st.write("While the main feature of the app is the trope prediction, it also includes additional pages finding a book using filters and a user library page where you can add or remove books from.")
elif info == "Mission":
    st.write("Our mission is to enhance the reading experience for romance novel enthusiasts by providing insights into the tropes present in their favorite books, helping them discover new reads that align with their preferences. This app is made with Streamlit and is a project for learning purposes, so expect some quirks along the way!")




