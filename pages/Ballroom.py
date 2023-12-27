import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template, hide_streamlit_style
from langchain.llms import HuggingFaceHub




def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)



def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with the USA Dance Syllabus",
                       page_icon="pics/noun-ballroom-dance-4703910.png")
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state['conversation'] = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with the USA Dance Syllabus 🕺🏽💃🏿")

    #get vector store
    embedding_function = OpenAIEmbeddings(model="text-search-ada-doc-001")
    vectorstore = FAISS.load_local("FAISS",embedding_function)


    #get conversation chain(vectorstore)
    st.session_state.conversation = get_conversation_chain(vectorstore)

    user_question = st.text_input("Insert Question Below:")
    if user_question:
        handle_userinput(user_question)



if __name__ == '__main__':
    main()
