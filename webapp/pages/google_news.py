import streamlit as st
from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import pandas as pd
import nltk


def app():

    googlenews=GoogleNews(start='05/01/2020',end='05/31/2020')
    googlenews.search('Coronavirus')
    result=googlenews.result()
    df=pd.DataFrame(result)
    print(df.head())
    for i in range(2,20):
        googlenews.getpage(i)
        result=googlenews.result()
        df=pd.DataFrame(result)
    list=[]
    for ind in df.index:
        dict={}
        article = Article(df['link'][ind],config=config)
        article.download()
        article.parse()
        article.nlp()
        dict['Date']=df['date'][ind]
        dict['Media']=df['media'][ind]
        dict['Title']=article.title
        dict['Article']=article.text
        dict['Summary']=article.summary
        list.append(dict)
    news_df=pd.DataFrame(list)
    news_df.to_excel("articles.xlsx")
