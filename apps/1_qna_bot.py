from dotenv import load_dotenv
load_dotenv()

from langchain_ollama import ChatOllama
import streamlit as st

llm = ChatOllama(
    model="ministral-3:latest",
    temperature=0.7
)

st.title("🤖 AskBuddy - AI QnA Bot")
st.markdown("My QnA Bot with LangChain and Ollama")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask anything")
if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({"role":"ai","content":res.content})
    
    
# while True:
#     query = input("User: ")
    
#     if query.lower() in ["quit","exit","bye"]:
#         print("GoodByee 👋")
#         break
    
#     res = llm.invoke(query)
#     print("AI: ",res.content)