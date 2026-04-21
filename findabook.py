import streamlit as st

st.set_page_config(page_title="Second Page", page_icon="📄")

st.sidebar.header("Filter Books")

#date filter
date_publish = st.sidebar.checkbox("Date Published:", value=False)
begin_date = st.sidebar.date_input("From:", key="begin_date", disabled=not date_publish)
end_date = st.sidebar.date_input("To:", key="end_date", disabled=not date_publish)

#genre filter
genre = st.sidebar.checkbox("Genre:", value=False)
genre_list = st.sidebar.multiselect(
    "Choose Genres:",
    options=["Contemporary", "Historical", "Paranormal", "Romantic Comedy", "Fantasy"],
    default=None, disabled=not genre
)


st.title("Find a Book 📄")
st.write("Either search for a book by title or author, or use the filters in the sidebar to find books by date or genre.")

st.text_input("Search for a book:", key="input_text", placeholder="Type the title or author of the book...")

#if page_mode == "Info":
#    st.info("This page can contain a different section of your Streamlit app.")
#else:
#    st.write("Replace this content with the second page of your romance tropes app.")
