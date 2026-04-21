import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from recommender2 import predict_tropes, load_and_train_model

st.set_page_config(page_title="Fourth Page", page_icon="🧩")

#st.sidebar.header("Fourth page settings")
#page_mode = st.sidebar.radio("Page mode:", ["Overview", "Action"])

st.title("🧩 Fourth page", text_alignment="center")
st.write("This is the fourth page of the app. Use the top menu to switch between pages.")

title = st.text_input("Title:", key="input_text", placeholder="Type the title of the book...")
author = st.text_input("Author:", key="input_text2", placeholder="Type the author of the book...")
description = st.text_area("Description:", key="input_text3", placeholder="Type a brief description of the book...")

predict_button = st.button("Predict Tropes", disabled=not (title and author and description))
if predict_button:
    if title and author and description:
        progress_bar = st.progress(0)
        status_text = st.empty()

        status_text.text("Loading model...")
        progress_bar.progress(5)
        
        model, clf, trope_columns = load_and_train_model()

        status_text.text("Preparing text input...")
        progress_bar.progress(10)

        status_text.text("Encoding input into X...")
        progress_bar.progress(40)

        status_text.text("Running trope prediction...")
        result = predict_tropes(title, author, description, model, clf, trope_columns)
        progress_bar.progress(80)

        status_text.text("Finalizing results...")
        progress_bar.progress(100)

        status_text.empty()
        st.success("Prediction complete.")
        st.write("Predicted Tropes:")
        for trope, score in result:
            st.write(f"{trope}: {round(score, 3)}")

        progress_bar.empty()
    else:
        st.error("Please fill in all fields.")

#if page_mode == "Overview":
#    st.info("Use this page for yet another section of your romance tropes app.")
#else:
#    st.write("Replace this content with the fourth page of your romance tropes app.")
