import streamlit as st
from htmlTemplates import css, bot_template, user_template, hide_streamlit_style

def main():
    st.set_page_config(page_title="Cloud Architecture",
                       page_icon=":cloud:")
    
    st.title(":cloud: Cloud Architecture")


if __name__ == '__main__':
    main()

