import streamlit as st
import pandas as pd
import pickle as pkl
import altair as alt
import numpy as np
import pynput
from pynput.mouse import Listener



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
        upld = pkl.load(f, encoding='latin1')
    up = pd.DataFrame(upld)
    up2 = up.tail(10000)
    
    interval = alt.selection_interval(encodings = ['x'])
    
    chart = alt.Chart(up2).mark_line().encode(
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
        )
    
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
    
    result = st.button("Highlights!")
    
    st.write(result)
    
    if result == True:
        def on_click(x, y, button, pressed):
            if pressed == True:
                global x2
                x2 = x
        def on_move(x, y):
            return
        with Listener(
            on_move = on_move,
            on_click = on_click
                ) as listener:
            listener.join()

    else:
        st.write('nice')



with compare:
    mean = np.mean(df2,)
    mean2 = np.mean(up2)
    st.header('original mean')
    st.write(mean)
    st.header('imported mean')
    st.write( mean2)

    
    
    
    
    
    
    
    



    

   