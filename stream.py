import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
import numpy as np
import time

st.title('This is test')
st.header('this is header')
def click_b1():
    st.write('正在上传数据')
tab1,tab2,tab3,tab4,tab5 = st.tabs(['添加数据','删除数据','显示数据','股票代码','退出'])
if st.session_state.get('clickd',False):
    st.write('You clicked the button')
if st.button('添加',on_click = click_b1):
    st.session_state['clicked'] = True
    
df =pd.read_excel('d://newstock//sh//中信证券.xlsx ')
x = df['日期']
y = df['收盘价']

st.dataframe(df)
st.line_chart(y)
#st.area_chart(y)
#st.bar_chart(y)
st.divider()
prompt = st.chat_input('Say something')
if prompt:
    st.write(f'The user has sent:  {prompt}')
with st.chat_message('user'):
    st.write('HELLO') 
    st.line_chart(np.random.randn(30,3))
with st.chat_message('Ai'):
    st.write('I am Ai')
if st.button('Rerun'):
    st.rerun()
def my_generator():
    for i in range(10):
        yield f'{i}'
        time.sleep(0.5)
#st.write_stream(my_generator)
chart_data = pd.DataFrame(np.random.randn(20,3),columns =['a','b','c'])
chart_data
st.link_button('百度','https://www.baidu.com')
st.page_link('d://stream.py',label='Home')
st.page_link('d://pages//profile.py',label =' My profile')
selected = st.checkbox('I agree')
st.write(f'You selected:  {selected}')
activated = st.toggle('Activate')
st.write(f'Activated: {activated}')
choice = st.radio('Pick one',['cats','dogs'])
st.write(f'Your choice: {choice}')

cho = st.selectbox('Pick one',['cats','dogs'])
st.write(f'You picked: {cho}')
choices = st.multiselect('Buy',['milk','apples','potatoes'])
st.write(f'You bought: {choices}')
number = st.slider('Pick a number',0,100)
st.write(f'You selectd {number}')
size = st.select_slider('Pick a size',['S','M','L'])
st.session_state['profile_key']

