import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import langchain_helper

st.markdown("""
    <style>
    .main {
        background-color: #f0f0f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Analyze your employees data")
btn = st.button("Start")
if btn:
    langchain_helper.createdb()

sample_question = [
    "Provide me the joining date for the employee with employee name William Wang",
    "Provide me all the details for the employee with employee name John Doe?"
]

selected_example = st.selectbox("Choose a sample question:", [""] + sample_question)
if selected_example:
    question = selected_example
else:
    question = st.text_input("Question: ", placeholder="Enter your question here...")


if question:
    chain = langchain_helper.create_qachain()
    response = chain.invoke(question)
    #print(response)
    st.header("Answer")
    st.write(response)

#print(chain.invoke("Provide me the joining date for the employee with employee name William Wang?"))




