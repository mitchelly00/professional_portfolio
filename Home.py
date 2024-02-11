import streamlit as st
from htmlTemplates import css, bot_template, user_template, hide_streamlit_style

def main():
    st.set_page_config(page_title="MJ Schonhoeft",
                       page_icon="pics/Logo small With background 2.png")
    
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.write(css, unsafe_allow_html=True)

    colT1,colT2,colT3,colT4 = st.columns(4)
    with colT2:
        st.image('pics/croped.png',width=150)

    with colT3:
        st.title('MJ Schonhoeft')
        

    #st.markdown(streamlit_style, unsafe_allow_html=True)
    st.header("About me:")
    text = '''I am a Data Science Analyst at Deloitte and am passionate about creating AI applications that best serve the needs of end users.
    '''
    st.markdown(text)
    st.header("Projects:")
    text2 = '''Country Dance ChatBot 🤠
    \n - This is an LLM application that answers your questions from the UCWDC country dance rules.
    \n US Deportations Visualized :earth_americas:
    \n - This data project shows the correlation between immigration and pesidential administrations' political party
    '''
    st.markdown(text2)


if __name__ == '__main__':
    main()
