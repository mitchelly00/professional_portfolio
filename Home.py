import streamlit as st
from htmlTemplates import css, bot_template, user_template, hide_streamlit_style

def main():
    st.set_page_config(page_title="MJ Schonhoeft",
                       page_icon="pics/logo_home.png")
    
    #adding custom markdown for navigation bar
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    st.markdown("""
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Features</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Pricing</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#">Disabled</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

    
    st.image("pics/home_background.png")
    
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.write(css, unsafe_allow_html=True)

    # colT1,colT2,colT3,colT4 = st.columns(4)
    # with colT2:
    #     st.image('pics/croped.png',width=150)

    # with colT3:
    #     st.title('MJ Schonhoeft')
        

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
