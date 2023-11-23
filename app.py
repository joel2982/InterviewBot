import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from chatui import css,user_template,bot_template

OPENAI_API_KEY=st.secrets['OPENAI_API_KEY']

def new_session_state():
    if 'conversation' not in st.session_state:
        st.session_state.conversation = None
        st.session_state.chat_history = None

def chat_output(user_question):
    response = st.session_state.conversation(user_question)
    st.session_state.chat_history = response['chat_history']
    for i,chat in enumerate(st.session_state.chat_history):
        if i%2 == 0:
            st.write(user_template.replace("{{MSG}}",chat.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}",chat.content), unsafe_allow_html=True)

def conversation_chain():
    prompt = ChatPromptTemplate(
                messages=[
                    SystemMessagePromptTemplate.from_template(
                        ''' You are an interviewer, interviewing the user for a junior level job role. Your Name is Sam Altman.
                        You should start the interview by introducing yourself, asking the user their name and the specific job role they have applied for, if they haven't mentioned.
                        Always Address the user by the name they specify.  
                        If the user hasn't mentioned the job role, ask for the job role untill it hasn't been given by the user.
                        You should ask one question at a time. The questions should start from an easy level and then can range from easy to haed depending on the answers of the user.
                        The questions that you ask regarding the job role should comprise of both behavioural questions and job specific questions.
                        You should stop the interview after 5 questions asked by AI/you.
                        Your should let the user know that their interview is over and thank the user for their time and tell them that you will let them know the results of the soon via mail.

                        Give the user a feedback of the interview only if the user asks and it should be at the end of the interview.
                        '''
                        ),
                    MessagesPlaceholder(variable_name="chat_history"),
                    HumanMessagePromptTemplate.from_template("{question}"),
                    ]
                )
                        # You should ask the user with a total of not more than 5 questions, regarding the job role that the user mentions.
    llm = ChatOpenAI(model_name='gpt-3.5-turbo')
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = LLMChain(
        llm = llm,
        memory = memory,
        prompt = prompt,
        verbose = True
    )
    st.session_state.conversation = conversation_chain

def main():
    load_dotenv()
    st.set_page_config(page_title='Interview Bot',page_icon=':clipboard:')
    st.write(css, unsafe_allow_html=True)
    new_session_state()
    col1,col2 = st.columns([0.9,0.1])
    with col1:
        st.subheader('Interview Bot :clipboard:')
    with col2:
        new_chat = st.button('New')
    user_question = st.chat_input('Type')
    if user_question:
        if not st.session_state.conversation:
            conversation_chain()
        chat_output(user_question)
    if new_chat:
        st.session_state.clear()
        st.empty()

if __name__ == '__main__':
    main()
