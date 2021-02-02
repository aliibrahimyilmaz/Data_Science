import streamlit as st
import os

import spacy
from textblob import TextBlob
from gensim.summarization import summarize
#from sumy.parsers.plaintext import PlaintextParser
#from sumy.nlp.tokenizers import Tokenizer
#from sumy.summarizers.lex_rank import LexRankSummarizer

def tokenizer(my_text):
    nlp=spacy.load('en')
    docx=nlp(my_text)
    #tokens=[token.text for token in docx]
    #lemma=[token.text for token in docx]
    token_and_lemma=[('"Tokens":{}, "Lemma":{}'.format(token.text, token.lemma_)) for token in docx]
    return  token_and_lemma

def entity_extracter(my_text):
    nlp=spacy.load('en')
    docx=nlp(my_text)
    entities=[(entity.text, entity.label_) for entity in docx.ents]
    return entities
    

def main():
#title
    st.title("NLP with Streamlit")
    st.subheader("Natural Language Processing On the Go..")
    st.markdown("""
    	#### Description
    	+ This is a Natural Language Processing(NLP) Based App useful for basic NLP task
    	Tokenization,NER,Sentiment,Summarization
    	""")    
    
    #Tokenization
    if st.checkbox("Show Tokens and Lemma"):
        st.subheader("Tokenize Your Text")
        message = st.text_area("Enter Your Text ")
        if st.button("Analyze"):
            nlp_result = tokenizer(message)
            st.json(nlp_result)

    #Name Entity
    if st.checkbox("Show Named Entities"):
        st.subheader("Extract Entities From Your Text")
        message = st.text_area("Enter Your Text")
        if st.button("Extract"):
            nlp_result = entity_extracter(message)
            st.json(nlp_result)

    #Sentiment Analysis
    if st.checkbox("Show Sentiment Analysis"):
        st.subheader("Sentiment of Your Test")
        message = st.text_area("Enter Your Text  ")
        if st.button("analyze"):
            blob=TextBlob(message)
            result_sentiment=blob.sentiment
            st.success(result_sentiment)
            
    #Text Summarization
    if st.checkbox("Show Text Summarization"):
        st.subheader("Summarize Your Test")
        message = st.text_area("Enter Your Text    ")
        if st.button("Summarize"):
            st.text("Using Gensim Summarizer ..")
            summary_result=summarize(message)
            st.success(summary_result)    
                
st.sidebar.subheader("About App")
st.sidebar.info("NLP App with Streamlit. Clarusway proudly presents.")
                
    
    
if __name__ == '__main__':
    main()