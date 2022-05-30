import streamlit as st
import altair as alt
import pandas as pd
import numpy as np


def main():
    df = load_data()
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])

    if page == "Homepage":
        st.header("Данные для задачи классификации банкнот.")
        st.write("Данные для датасета были извлечены из изображений, снятых с подлинных и поддельных банкнотоподобных образцов. Для оцифровки использовалась промышленная камера, обычно используемая для проверки печати.Инструмент Wavelet Transform использовался для извлечения признаков из изображений.")
        st.write("1) variance of Wavelet Transformed image (дисперсия вейвлет-преобразованного изображения), тип вещественный.")
        st.write("2) skewness of Wavelet Transformed image (асимметрия вейвлет-преобразованного изображения), тип вещественный.")
        st.write("3) curtosis of Wavelet Transformed image (эксцесс преобразованного изображения), тип вещественный.")
        st.write("4) entropy of image (энтропия изображения), тип вещественный.")
        st.write(df)
    elif page == "Exploration":
        st.title("Data Exploration")
        visualize_data(df)

@st.cache
def load_data():
    df = pd.read_csv('preprocessing_data_banknote_authentication.csv')
    return df

def visualize_data(df):
    c = alt.Chart(df).mark_circle().encode(x='variance', y='skewness', size='class',  
                                       color='c')
    st.altair_chart(c, width=-1)

if __name__ == "__main__":
    main()
