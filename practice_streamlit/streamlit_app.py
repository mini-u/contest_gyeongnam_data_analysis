# streamlit_app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Iris 데이터셋 시각화")

# 데이터
df = sns.load_dataset("iris")

# 선택 옵션
columns = df.columns[:-1]  # 마지막 column은 species
x_axis = st.selectbox("X축 변수 선택", columns)
y_axis = st.selectbox("Y축 변수 선택", columns, index=1)

# 그래프 출력
st.subheader(f"{x_axis} vs {y_axis} 산점도 (품종별 색상)")

fig, ax = plt.subplots()
sns.scatterplot(data=df, x=x_axis, y=y_axis, hue="species", ax=ax)
st.pyplot(fig) 