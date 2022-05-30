import streamlit as st
import altair as alt
import pandas as pd

def main():
    df = load_data()
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])

    if page == "Homepage":
        st.header("Данные для задачи классификации банкнот.")
        st.write("Данные для датасета были извлечены из изображений, снятых с подлинных и поддельных банкнотоподобных образцов. Для оцифровки использовалась промышленная камера, обычно используемая для проверки печати.Инструмент Wavelet Transform использовался для извлечения признаков из изображений.")
        st.write("variance of Wavelet Transformed image (дисперсия вейвлет-преобразованного изображения), тип вещественный.")
        st.write("skewness of Wavelet Transformed image (асимметрия вейвлет-преобразованного изображения), тип вещественный.")
        st.write("curtosis of Wavelet Transformed image (эксцесс преобразованного изображения), тип вещественный.")
        st.write("entropy of image (энтропия изображения), тип вещественный.")
        st.write(df)
    elif page == "Exploration":
        st.title("Data Exploration")
        x_axis = st.selectbox("Choose a variable for the x-axis", df.columns, index=0)
        y_axis = st.selectbox("Choose a variable for the y-axis", df.columns, index=1)
        visualize_data(df, x_axis, y_axis)

@st.cache
def load_data():
    df = pd.read_csv('preprocessing_data_banknote_authentication.csv')
    return df

def visualize_data(df, x_axis, y_axis):
    graph = alt.Chart(df).mark_circle(size=60).encode(
        x=x_axis,
        y=y_axis,
        color='Origin',
        tooltip=["variance","skewness",	"curtosis",	"entropy","class"]
    ).interactive()

    st.write(graph)

if __name__ == "__main__":
    main()
