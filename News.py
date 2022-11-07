from unicodedata import category
import streamlit
import requests
import pycountry
from api import apiKEY
streamlit.title('News App')

col1, col2 = streamlit.columns([3,1])
with col1:
    user = streamlit.text_input('Enter Country Name')

with col2:
    category = streamlit.radio('Choose A News Category',('Technology','Politics','Sports','Business'))
    btn = streamlit.button('Enter')

if btn:
    country = pycountry.countries.get(name=user).alpha_2
    url = f"https://newsapi.org/v2/everything?q=keyword&apiKey=b96751e8d90b4d8fbdefd6b981a11a7e"
    r = requests.get(url)
    r = r.json()
    articles = r['articles']
    for article in articles:
        streamlit.header(article['title'])
        streamlit.markdown(f"<span style='background-color:blue; padding:10px; border-radius:20px;'> Published At: {article['publishedAt']}</span>", unsafe_allow_html=True)
        if article['author']:
            streamlit.write(article['author'])
        streamlit.write(article['source']['name'])
        streamlit.write(article['description'])
        streamlit.image(article['urlToImage'])