import streamlit as st
from htmlTemplates import css,data_ucwdc,data_immigration, hide_streamlit_style
from streamlit_card import card
import base64
def main():
    st.set_page_config(page_title="MJ Schonhoeft",
                       page_icon="pics/logo_home.png",
                       layout="wide"
                       #initial_sidebar_state="collapsed"
                       )
    
    #collpasing the side navebar
    
    #st.markdown( """ <style> [data-testid="collapsedControl"] { display: none } </style> """, unsafe_allow_html=True, )
    #adding custom markdown for navigation bar
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

#     st.markdown("""
# <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
#   <a class="navbar-brand" target="_blank">Data Scientist</a>
#   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
#     <span class="navbar-toggler-icon"></span>
#   </button>
#   <div class="collapse navbar-collapse" id="navbarNav">
#     <ul class="navbar-nav">
#       <li class="nav-item active">
#         <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">YouTube</a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Twitter</a>
#       </li>
#     </ul>
#   </div>
# </nav>
# """, unsafe_allow_html=True)

    
    st.image("pics/home_background.png")
    
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.write(css, unsafe_allow_html=True)


    #st.markdown(streamlit_style, unsafe_allow_html=True)
    st.header("About me")
    text = '''I am a Data Science Analyst at Deloitte and am passionate about creating AI applications that best serve the needs of end users.
    '''
    st.markdown(text)
    st.header("Projects")
    text2 = ''' Click on any link below to see each project:
    '''
    st.markdown(text2, unsafe_allow_html=True)


#UCWDC content card
    # with st.container():
    #     card1 = card(
    #         title="Country Dance Chatbot",
    #         text="an LLM application that answers your questions from the UCWDC country dance rules",
    #         image= data_ucwdc,
    #         url="/Country_Dance_Chatbot",
    #         styles={
    #                 "card": {
    #                     "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
    #                     "height": "300px", # <- if you want to set the card height to 300px
    #                     "border-radius": "10px"
    #                 }})
    #     card2 = card(
    #         title="US Deportations by Political Party",
    #         text="statistical test between immigration and pesidential administrations' political party",
    #         image= data_immigration,
    #         url="/US_Deportations_by_Political_Party",
    #         styles={
    #                 "card": {
    #                     "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
    #                     "height": "300px", # <- if you want to set the card height to 300px
    #                     "border-radius": "10px"
    #                 }})
        
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

    with tab1:
        card3 = card(
            title="Country Dance Chatbot",
            text="an LLM application that answers your questions from the UCWDC country dance rules",
            image= data_ucwdc,
            url="/Country_Dance_Chatbot",
            styles={
                    "card": {
                        "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
                        "height": "300px", # <- if you want to set the card height to 300px
                        "border-radius": "10px"
                    }})

    with tab2:
        card4 = card(
            title="US Deportations by Political Party",
            text="statistical test between immigration and pesidential administrations' political party",
            image= data_immigration,
            url="/US_Deportations_by_Political_Party",
            styles={
                    "card": {
                        "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
                        "height": "300px", # <- if you want to set the card height to 300px
                        "border-radius": "10px"
                    }})
    

    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    
#Immigration Content card
    # with st.container():
    #     card3 = card(
    #         title="US Deportations by Political Party",
    #         text="statistical test between immigration and pesidential administrations' political party",
    #         image= data_immigration,
    #         url="/US_Deportations_by_Political_Party",
    #         styles={
    #                 "card": {
    #                     "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
    #                     "height": "300px", # <- if you want to set the card height to 300px
    #                     "border-radius": "10px"
    #                 }})
    


if __name__ == '__main__':
    main()
