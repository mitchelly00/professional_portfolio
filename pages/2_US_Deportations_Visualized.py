import streamlit as st
from htmlTemplates import css, bot_template, user_template, hide_streamlit_style
import pandas as pd
import matplotlib as plt
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

# adding data
df_visual = pd.read_csv("df_visual.csv")
df_visual_recent = df_visual[df_visual['Year']>1940]

#######################################################################################
# fig showing the political parties
fig = px.bar(df_visual_recent, x='Year', y='Total Deportations',color='Political Party',title='Deportations in the US from Government Fiscal Year 1982-2022', color_discrete_sequence=['indianred','blue'])

#####################################################################################
# fig showing the categories of deportations

fig2 = go.Figure(data=[
    go.Bar(name="Removals", x=df_visual_recent['Year'].values, y=df_visual_recent['Removals'].values,marker_color='steelblue'),
    go.Bar(name="Administrative Returns", x=df_visual_recent['Year'].values, y=df_visual_recent['Administrative Returns'].values,marker_color='blue'),
    go.Bar(name="Enforcement Returns", x=df_visual_recent['Year'].values, y=df_visual_recent['Enforcement Returns'].values,marker_color='DarkSlateGrey'),
    go.Bar(name="Expulsions", x=df_visual_recent['Year'].values, y=df_visual_recent['Expulsions'].values,marker_color="LightSkyBlue")
])


#### Change the bar mode
fig2.update_layout(
    title = {
        'text': "US Deportations by Type Government Fiscal Year 1971-2022",
        'y':0.9,
        'x':0.4,
        'xanchor': 'right',
        'yanchor': 'top'},
    xaxis_title="Year",
    yaxis_title="Number of Deportations",
    legend_title = {
        'text':"Type of Deportation"
        # 'y':0.9,
        # 'x':0.4,
        # 'xanchor': 'right',
        # 'yanchor': 'top'
    },
    font=dict(
        family="Calibri",
        size=18
    ),
    barmode='stack')

###################################################################
#Hypothesis testing

#dem distributions
df_dem = df_visual[df_visual['Political Party']=='Democrat']


fig3 = px.histogram(df_dem, x="Total Deportations",nbins=10,title="Distribution of the number of deportations a year per Democrat presidential administration")

fig3.update_layout(bargap=0.2)

#republican distribtuion 

df_rep = df_visual[df_visual['Political Party']=='Republican']

fig4 = px.histogram(df_rep, x="Total Deportations",nbins=10,
                    title="Distribution of the number of deportations a year per Republican presidential administration",
                    color_discrete_sequence=['indianred'])

fig4.update_layout(bargap=0.2)

##########################################################################################################
#streamlit application 

def main():
    st.set_page_config(page_title="US Deportations Visualized",
                       page_icon=":earth_americas:")
    
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.write(css, unsafe_allow_html=True)
    st.title(':earth_americas: US Deportations Visualized')

    st.header("Exploratory Analysis")
    

    st.plotly_chart(fig,use_container_width=True)
    st.plotly_chart(fig2,use_container_width=True)

    st.header("Hypothesis Testing")
    st.plotly_chart(fig3,use_container_width=True)

    st.plotly_chart(fig4,use_container_width=True)
    


if __name__ == '__main__':
    main()
