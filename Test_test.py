import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
st.write("Предобработка данных по липидомике")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_excel(uploaded_file)
    st.write('Загруженный файл')
    st.write(dataframe.head())
    dataframe['peptide+product'] = dataframe['Peptide']+' ' + dataframe['Product Mz'].astype(str)
    pivoted = dataframe.pivot_table(index="Replicate", columns="peptide+product", values="Area")
    st.write('Трансформированный файл')
    st.write(pivoted.head())
    st.write('Скачать трансформированный файл')
    st.download_button('Download file',data=pd.DataFrame.to_csv(pivoted,index=True), mime='text/csv')

    