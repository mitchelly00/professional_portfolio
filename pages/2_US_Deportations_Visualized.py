import streamlit as st
from htmlTemplates import css, bot_template, user_template, hide_streamlit_style
import pandas as pd
import matplotlib as plt
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from scipy.stats import f_oneway

# adding data
df_visual = pd.read_csv("df_visual.csv")
df_visual_recent = df_visual[df_visual['Year']>1940]

#######################################################################################
# fig showing the political parties
fig = px.bar(df_visual_recent, x='Year', y='Total Deportations',color='Political Party',
             title='Deportations in the US from Government Fiscal Year 1940-2022', color_discrete_sequence=['blue','indianred'])

#####################################################################################
# fig showing the total deportations by political party


fig2 = px.bar(df_visual_recent, x='Political Party', y='Total Deportations',
              color='Political Party',title='Total deportations by political parties in the US from Government Fiscal Year 1940-2022',
              color_discrete_sequence=['blue','indianred'])

###################################################################
#Hypothesis testing

#dem distributions
df_dem = df_visual_recent[df_visual_recent['Political Party']=='Democrat']


fig3 = px.histogram(df_dem, x="Total Deportations",nbins=10,title="Distribution of the number of deportations a year per Democrat presidential administration")

fig3.update_layout(bargap=0.2)

#republican distribtuion 

df_rep = df_visual_recent[df_visual_recent['Political Party']=='Republican']

fig4 = px.histogram(df_rep, x="Total Deportations",nbins=10,
                    title="Distribution of the number of deportations a year per Republican presidential administration",
                    color_discrete_sequence=['indianred'])

fig4.update_layout(bargap=0.2)

#setting up stats test
df_dem_values = df_dem['Total Deportations']
df_rep_values = df_rep['Total Deportations']
statistic, p_value = f_oneway(df_dem_values, df_rep_values)

##########################################################################################################
#streamlit application 

def main():
    st.set_page_config(page_title="US Deportations Visualized",
                       page_icon=":earth_americas:")
    
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.write(css, unsafe_allow_html=True)
    st.title(':earth_americas: US Deportations Visualized')

    text1 = '''
    Undocumented immigration to the US has been a common news headline in national politics. This page clarifies how
    immigration policy is different (or similar) between political parties. 

    The results of the quick analysis show that there is no correlation between political party and number of deportations. 

    The ****Exploratory Analysis**** section will show general trends over time in deportations using two different graphs.

    The **Hypothesis Testing** section uses a statiscal test called ANOVA to look at correlations in categorical data.
    '''    
    st.write(text1)


    st.header("Exploratory Analysis")


    st.plotly_chart(fig,use_container_width=True)
    st.plotly_chart(fig2,use_container_width=True)

    st.header("Hypothesis Testing")

    text2 = '''This dataset qualifies for an ANOVA test since there is over 30 data points in each category with:
     \n - Number of Democrat years in the dataset = 43
     \n - Number of Republican years in the dataset = 39

     \nThe distributions of the deportations per year broken down by political administration is below.
    '''
    st.write(text2)
    st.plotly_chart(fig3,use_container_width=True)
    st.plotly_chart(fig4,use_container_width=True)
    
    alpha = 0.05

    st.write("ANOVA Statistic:",statistic)
    st.write("P-value:",p_value)
    st.write("alpha:",alpha)
    # Check significance
    
    if p_value < alpha:
        st.write("Reject the null hypothesis. There are significant differences between groups.")
    else:
        st.write("Fail to reject the null hypothesis. There are no significant differences between Political Parties in terms of amount of deportation.")

    


if __name__ == '__main__':
    main()
