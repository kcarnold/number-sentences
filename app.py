import streamlit as st
import spacy

input_text = st.text_area("Enter some text")

nlp = spacy.load("en_core_web_sm")

if not input_text:
    st.stop()

# Split text into lines and process bullets separately
lines = input_text.split('\n')
result = []
counter = 1

for line in lines:
    # Preserve original indentation
    indent = len(line) - len(line.lstrip())
    indentation = line[:indent]
    stripped_line = line[indent:].strip()
    
    # Check if line is a bullet point after removing indentation
    if stripped_line.startswith(('*', '-', '·')):
        marker = stripped_line[0]  # Get the bullet marker (*, -, or ·)
        content = stripped_line[1:].strip()  # Get rest of line without marker
        result.append(f"{indentation}{marker} {{{counter}}} {content}")
        counter += 1
    else:
        # Process regular text with spaCy
        doc = nlp(stripped_line)
        for sentence in doc.sents:
            result.append(f"{indentation}{{{counter}}} {sentence.text}")
            counter += 1

# Join with newlines to preserve formatting
result = '\n'.join(result)

tabs = st.tabs(["Easy to read", "Easy to copy-paste"])

tabs[0].text(result)
with tabs[1]:
    st.write("Click the Copy button in the top-right corner to copy the text.")
    st.code(result)
