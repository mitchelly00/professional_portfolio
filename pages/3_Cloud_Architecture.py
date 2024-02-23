import streamlit as st
from htmlTemplates import css, hide_streamlit_style

def main():
    st.set_page_config(page_title="Cloud Architecture",
                       page_icon="pics/logo_cloud.png",
                       layout="wide")
    #st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.write(css, unsafe_allow_html=True)
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.image('pics/cloud.png')


    #overview
    st.header('Overview')
    st.image('pics/aws_diagram_1.png')
    text1 = '''
    Above is the general architecture of the current web application you are viewing. 
    \n 
    This application's general architecture is as follows:
    \n - **EC2** the instance connects to an Application Load Balancer
    \n - **Application Load Balancer** automatically redirects all HTTP traffic to HTTPS traffic.
    \n      - The load balancer has an HTTPS Certificate through AWS Certificate Manager. 
    \n - **Route 53** routes DNS traffic to the Application Load Balancer
    '''
    st.markdown(text1)

    # EC2 
    st.header('EC2 structure')
    st.image('pics/aws_diagram_2.png')
    text2 = '''
    This application has several important EC2 elements. 
    \n - **TMUX** ensures a consistant session. TMUX allows me to disconnect from a session without terminating running streamlit processes.
    \n - **NGINX** servers as a  reverse proxy to convert outward bound traffic from 8502 to port 80 (HTTP) to connect to the Application Load Balancer.
    \n - **OPENAI API** The application calls the OPENAI API to power the chatbot.
    '''
    st.markdown(text2)

if __name__ == '__main__':
    main()    