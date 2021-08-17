import streamlit as st
import pandas as pd
import pickle as pkl
import altair as alt
import numpy as np
from io import BytesIO




with open('project/lfp.pkl', 'rb') as f:
    obj = pkl.load(f, encoding='latin1')

df = pd.DataFrame(obj)

df2 = df.head(10000)

df3 = df.tail(10000)

header = st.container()
dataset = st.container()
uploader = st.container()
compare = st.container()


with header:
    st.title("Title")

with uploader:
    st.header('Imported Data')
    file = st.file_uploader("Upload file", type = ['pkl'])
    show_file = st.empty()
    with open('project/lfp.pkl', 'rb') as f:
        obj2 = pkl.load(f, encoding='latin1')
    df4 = pd.DataFrame(obj2)
    df5 = df4.tail(10000)
    
    interval = alt.selection_interval(encodings = ['x'])
    
    chart = alt.Chart(df5).mark_line().encode(
        x=alt.X('times'),
        y=alt.Y('values')
        )#.add_selection(interval)
    #st.altair_chart(chart, use_container_width=True)
    
    
    base = chart.encode(    
        x=alt.X('times', scale=alt.Scale(domain=interval.ref()))
        ).properties(
        width=800,
        height=300
        )
    
    view = chart.add_selection(
        interval
        ).properties(
        width=800,
        height=50
        )
    st.altair_chart(base & view)
    

    
    

with dataset:
    st.header('Original Data')
    interval = alt.selection_interval(encodings = ['x'])
    
    chart = alt.Chart(df2).mark_line().encode(
        x=alt.X('times'),
        y=alt.Y('values')
        )#.add_selection(interval)
    #st.altair_chart(chart, use_container_width=True)
    
    
    base = chart.encode(    
        x=alt.X('times', scale=alt.Scale(domain=interval.ref()))
        ).properties(
        width=800,
        height=300
        )
    
    view = chart.add_selection(
        interval
        ).properties(
        width=800,
        height=50
        )
    st.altair_chart( base & view)
    
    
with compare:
    mean = np.mean(df2,)
    mean2 = np.mean(df5)
    st.header('original mean')
    st.write(mean)
    st.header('imported mean')
    st.write( mean2)

    
    
    
    
    
    
    
    
    #pairs = pd.crosstab(df2['times'], df2['values'])
    #st.write(pairs)
 




    

   