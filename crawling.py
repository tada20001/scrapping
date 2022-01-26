import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import os, requests


### requests
proxies = {
    'http': os.getenv('HTTP_PROXY') # or just type proxy here withoust os
}

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
    'q': 'samsung',
    'hl': "en",
    'start': 0,
    'as_ylo': 2019,  # start year
    'as_yhi': 2021,  # end year
    'as_rr': 1, # only review articles
}

st.title('Google Scholar Explorer')
st.markdown("""***Google Scholar***로부터 데이터 추출합니다.""")

st.sidebar.subheader('User Input Feature')
st.sidebar.write('**1. Select Year range**')
start_year = st.sidebar.number_input('input a starting year', min_value=2000, max_value=2021)
end_year = st.sidebar.number_input('input a ending year', min_value=2000, max_value=2021)


### 1. request Google Scholar
def set_parms(q, start_year, end_year, start=0):
    params = {
    'q': q,
    'hl': "en",
    'start': 0,
    'as_ylo': start_year,  # start year
    'as_yhi': end_year,  # end year
    'as_rr': 1, # only review articles
    }
    return params
proxies = {'http': os.getenv('HTTP_PROXY')}
headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = set_parms('samsung', start_year, end_year)

html = requests.get('https://scholar.google.com/scholar', params=params, headers=headers, proxies=proxies)
soup = BeautifulSoup(html.content, 'html.parser')
st.write(params)
st.write(soup.text)
    





