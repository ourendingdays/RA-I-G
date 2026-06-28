import streamlit as st

# Define the pages
main_page = st.Page("main_page.py", title="Main Page", icon="🎈")
doc_analysis = st.Page("document_analysis.py", title="Document Analysis", icon="❄️")

# Set up navigation
pg = st.navigation([main_page, doc_analysis])

# Run the selected page
pg.run()