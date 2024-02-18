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



###################################################################
#Hypothesis testing

#dem distributions
df_dem = df_visual_recent[df_visual_recent['Political Party']=='Democrat']


fig3 = px.histogram(df_dem, x="Total Deportations",nbins=10,title="Distribution of the number of deportations a year per Democrat presidential administration",
                    color_discrete_sequence=['blue'])

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

#####################################################################################
# fig showing the total deportations by political party

# initialize list of lists
data_party = [['Democrat', np.sum(df_dem_values)], ['Republican', np.sum(df_rep_values)]]

# Create the pandas DataFrame
df_totals = pd.DataFrame(data_party, columns=['Party', 'Total Deportations'])



fig2 = px.bar(df_totals, x='Party', y='Total Deportations',
              color='Party',title='Total deportations by political parties in the US from Government Fiscal Year 1940-2022',
              color_discrete_sequence=['blue','indianred'])



##########################################################################################################
#streamlit application 

def main():
    st.set_page_config(page_title="US Deportations Visualized",
                       page_icon="pics/logo_imm.png",
                       layout="wide")
    
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.write(css, unsafe_allow_html=True)
    st.image('pics/immigration.png')

    st.header("Abstract")
    text1 = '''
    \n Undocumented immigration to the US has been a common news headline in national politics. This page asks if there is a difference between 
    undocumented immigration rates between presidential political parties. 
    
    \n The results of the quick analysis show that there is ****no correlation** between political party and number of deportations.** 
    '''    
    st.write(text1)

    st.header("Exploratory Analysis")

    text_ea = '''This section will show general trends over time in deportations using two different graphs.
    '''
    st.write(text_ea)
    
    # st.plotly_chart(fig3,use_container_width=True)
    # st.plotly_chart(fig4,use_container_width=True)

    st.plotly_chart(fig,use_container_width=True)
    st.plotly_chart(fig2,use_container_width=True)

    st.header("Hypothesis Testing")

    text2 = '''
    This sections uses a statiscal test called ANOVA to look at correlations in categorical data.
    \n**Hypothesis**
    \n - Null Hypothesis = there is no difference in deportations between Republican and Democratic presidential administrations
    \n - Alternate Hypothesis = there is a difference between Republican and Democratic presidental administrations in terms of numbers of deportations
    '''
    st.write(text2)

    
    alpha = 0.05

    st.header("Statistical Test")
    text_stat = '''
    \n **Test Qualifications**
    \n This dataset qualifies for an ANOVA test since there is over 30 data points in each category with:
    \n - Number of Democrat years in the dataset = 43
    \n - Number of Republican years in the dataset = 39
    \n
    \n**Results**
    \n
    '''

    st.write(text_stat)

    st.write("\n- ANOVA Statistic:",statistic)
    st.write("\n- P-value:",p_value)
    st.write("\n- alpha:",alpha)

    text3 = '''
    Now, to interpret these results:
    \n - The ANOVA statistic (F-value) compares the variability between groups to the variability within groups. A larger F-value indicates greater differences between group means relative to differences within groups. It generally takes a F value greater than 2.5 to be statistically signifigant
    \n - Since the p-value (0.2526) is greater than the alpha level (0.05), we fail to reject the null hypothesis.
    \n - The null hypothesis in ANOVA states that there are no significant differences among the group means. Therefore, in this case, we do not have sufficient evidence to conclude that there are significant differences among the group means.
    \n In summary, based on these results, there is insufficient evidence to reject the null hypothesis. This suggests that there are no significant differences between political parties in terms of amount of deportation.
    '''

    st.write(text3)
    # Check significance


if __name__ == '__main__':
    main()
