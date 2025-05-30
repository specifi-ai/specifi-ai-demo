
import streamlit as st

st.title("Specifi AI Demo")
st.write("This is a prototype AI assistant for Specifi software.")
st.write("Use it to help generate reports, analyze foundations, and check compliance.")

question = st.text_input("Ask the AI something about your site:")
if question:
    st.write("AI response would go here based on your query.")
