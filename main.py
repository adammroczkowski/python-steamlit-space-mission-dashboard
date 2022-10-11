import pandas as pd
import plotly.express as px
import streamlit as st
import math

st.set_page_config(page_title='Mission', layout = 'wide')

# df = pd.read_csv('mission_launches.csv')
df = pd.read_excel('mission_launches.xlsx')

df = df.drop_duplicates() 
df = df.dropna()
df = df.drop(df.columns[[0, 1,]], axis=1)
 


# SIDE BAR #

st.sidebar.header('Please filter here:')
organisation = st.sidebar.multiselect(
  'Select the Organisation:',
  options = df['Organisation'].unique(),
  default= df['Organisation'].unique()
)

mission_status = st.sidebar.multiselect(
  'Select the Mission Status:',
  options = df['Mission_Status'].unique(),
  default= df['Mission_Status'].unique()
)




df_selection = df.query(
  'Organisation == @organisation'
)

st.dataframe(df_selection)



