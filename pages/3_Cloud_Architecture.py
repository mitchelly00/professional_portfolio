import streamlit as st
from htmlTemplates import css, hide_streamlit_style

def main():
    st.set_page_config(page_title="Cloud Architecture",
                       page_icon="pics/logo_cloud.png",
                       layout="wide")
    #st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.write(css, unsafe_allow_html=True)
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.header('Overview')
    st.image('pics/cloud.png')

    st.header('EC2 structure')

    st.image('pics/aws_diagram_1.png')
    st.image('pics/aws_diagram_2.png')


if __name__ == '__main__':
    main()    