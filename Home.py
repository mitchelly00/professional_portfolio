import streamlit as st
from htmlTemplates import css, bot_template, user_template, hide_streamlit_style

def main():
    st.set_page_config(page_title="MJ Schonhoeft",
                       page_icon="pics\Logo small With background 2.png")
    
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.write(css, unsafe_allow_html=True)

    colT1,colT2 = st.columns([1,2])
    with colT2:
        st.title('MJ Schonhoeft')
        st.image('pics\croped.png',width=300)

    #st.markdown(streamlit_style, unsafe_allow_html=True)
    st.header("About me:")
    st.text('I am a Data Science Analyst at Deloitte.')
    st.text('I am passionate about ensuring I create AI applications that best serve the end\nusers.')
    st.write('---')
    st.header("Projects:")
    st.subheader(" - UN Buget Forcasting")    
    st.subheader(" - BallroomBot")
    st.text("This is an LLM application that tells you information based on the American Dance Sylabus")




if __name__ == '__main__':
    main()
