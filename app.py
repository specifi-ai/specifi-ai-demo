
import streamlit as st

st.set_page_config(page_title="Specifi AI Demo", layout="centered")

st.title("🤖 Specifi AI Assistant")
st.write("This is a demo of how AI can be integrated into Specifi to assist with engineering tasks.")

query = st.text_input("Ask a question about residential engineering or NZ code:")

if query:
    st.success("AI Response:")
    st.write("This is a simulated AI response based on your question. In a real integration, this would connect to engineering databases or code references.")
