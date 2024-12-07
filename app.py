import streamlit as st
import spacy

input_text = st.text_area("Enter some text")

nlp = spacy.load("en_core_web_sm")

if not input_text:
    st.stop()

# Number each sentence.
counter = 1
result = ""
doc = nlp(input_text)
for sentence in doc.sents:
    result += f" {{{counter}}} {sentence.text}"
    counter += 1

tabs = st.tabs(["Easy to read", "Easy to copy-paste"])

tabs[0].text(result)
with tabs[1]:
    st.write("Click the Copy button in the top-right corner to copy the text.")
    st.code(result)
