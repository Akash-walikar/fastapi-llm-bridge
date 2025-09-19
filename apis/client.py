import requests
import streamlit as st


def get_openai_response(input_text):
    response=requests.post("https://localhost:8000/essay/invoke",
                    json={"topic":{input_text}})
    return response.json()['output']

st.title("Langchain with OpenAI API")
input_text=st.text_input("write a essay on ")
input_text1=st.input_text("write a poem on ")
if input_text:
    st.write(get_openai_response(input_text))
if  input_text1:
    st.write(get_openai_response(input_text1))


#to run thin we streamlit run  client.py