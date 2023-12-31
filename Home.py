import streamlit as st
from htmlTemplates import css, bot_template, user_template, hide_streamlit_style

def main():
    st.set_page_config(page_title="MJ Lopez-Schonhoeft",
                       page_icon="pics/Logo small With background 2.png")
    
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.write(css, unsafe_allow_html=True)

    colT1,colT2 = st.columns([1,2])
    with colT2:
        st.title('MJ Schonhoeft')
        st.image('pics/croped.png',width=300)

    #st.markdown(streamlit_style, unsafe_allow_html=True)
    st.header("About me:")
    text = '''I am a Data Science Analyst at Deloitte.  
  
    I am passionate about creating AI applications that best serve the needs of end users.
    '''
    st.markdown(text)
    st.header("Projects:")
    # st.subheader(" - UN Buget Forcasting")    
    st.subheader(" - Country Dance Chatbot")
    st.text("This is an LLM application that tells you information based on the UCWDC dance rules")




if __name__ == '__main__':
    main()
