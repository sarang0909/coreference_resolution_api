"""A main script to run streamlit application.

"""
import streamlit as st
from src.utility.loggers import logger
from src.inference.coreference_resolution import get_coref_resolution


st.title("Entity Coreference Resolution")
form = st.form(key="my-form")
input_data = form.text_area("Enter text for Entity Coreference Resolution")

submit = form.form_submit_button("Submit")

if submit:
    try:
        output = get_coref_resolution(input_data)
        st.write("model_output:")
        st.write(output)
    except Exception as error:
        message = "Error while creating output"
        logger.error(message, str(error))
