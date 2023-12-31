import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path


#testing wasnt working very well. To trouble shoot
#next steps are having the program return the top three responses most similar.
#this could also market as a smart search feature.

# def get_pdf_text(pdf_docs):
#     text = ""
#     for pdf in pdf_docs:
#         pdf_reader = PdfReader(pdf)
#         for page in pdf_reader.pages:
#             text += page.extract_text()
#     return text


# def get_text_chunks(text):
#     text_splitter = CharacterTextSplitter(
#         separator="\n",
#         chunk_size=1000,
#         chunk_overlap=200,
#         length_function=len
#     )
#     chunks = text_splitter.split_text(text)
#     return chunks


# def get_vectorstore(text_chunks):
#     embeddings = OpenAIEmbeddings()
#     # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
#     vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
#     return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(openai_api_key=st.session_state.openai_api_key)
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
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
    
    st.set_page_config(page_title="Chat with the UCWDC Rules",
                       page_icon="🤠")
    #st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.write(css, unsafe_allow_html=True)

    # if "conversation" not in st.session_state:
    #     st.session_state.conversation = None
    # if "chat_history" not in st.session_state:
    #     st.session_state.chat_history = None

    st.header("Chat with the UCWDC rules :scroll:")

    text3 = '''     Disclaimer: This tool is not affliated with the UCWDC. The answers are non binding. Please consult the rules [here.](https://ucwdc.org/rules/)
    '''

    colT1,colT2 = st.columns([1,8])
    with colT2:
        st.markdown(text3)


    

    load_dotenv(Path("/home/ec2-user/.env"))
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if openai_api_key:
        st.session_state.openai_api_key = openai_api_key
        #get vector store
        embedding_function = OpenAIEmbeddings(openai_api_key=st.session_state.openai_api_key,model="text-search-ada-doc-001")
        vectorstore = FAISS.load_local("FAISS_Country",embedding_function)

        #get_conversation_chain(vectorstore)
        st.session_state.conversation = get_conversation_chain(vectorstore)
        user_question = st.text_input("Ask a question about the UCWDC Rules:")
        if user_question:
            handle_userinput(user_question)

    # with st.sidebar:
    #     st.subheader("Your documents")
    #     pdf_docs = st.file_uploader(
    #         "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
    #     if st.button("Process"):
    #         with st.spinner("Processing"):
    #             # get pdf text
    #             raw_text = get_pdf_text(pdf_docs)

    #             # get the text chunks
    #             text_chunks = get_text_chunks(raw_text)

    #             # create vector store
    #             vectorstore = get_vectorstore(text_chunks)

    #             # create conversation chain
    #             st.session_state.conversation = get_conversation_chain(
    #                 vectorstore)


if __name__ == '__main__':
    main()
