import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import platform

# 데이터
df = sns.load_dataset("iris")

st.title("🌼")

# 2단
col1, col2 = st.columns(2)

# ----------------- 왼쪽 영역 -----------------
with col1:
    st.header("설정 및 필터")
    
    # 품종 선택
    species_list = df['species'].unique().tolist()
    selected_species = st.multiselect("품종 선택", species_list, default=species_list)
    filtered_df = df[df['species'].isin(selected_species)]

    # 변수 선택
    numeric_columns = df.columns[:-1]
    x_var = st.selectbox("X축 변수", numeric_columns)
    y_var = st.selectbox("Y축 변수", numeric_columns, index=1)

    # 그래프 종류
    chart_type = st.radio("그래프 종류", ["산점도", "박스플롯", "히스토그램"])

    # 기초 통계
    st.subheader("기초 통계 요약")
    st.dataframe(filtered_df.describe())

# ----------------- 오른쪽 영역 -----------------
with col2:
    st.header("시각화 결과")

    fig, ax = plt.subplots()
    if chart_type == "산점도":
        sns.scatterplot(data=filtered_df, x=x_var, y=y_var, hue="species", ax=ax)
    elif chart_type == "박스플롯":
        sns.boxplot(data=filtered_df, x="species", y=y_var, ax=ax)
    elif chart_type == "히스토그램":
        for s in selected_species:
            sns.histplot(data=filtered_df[filtered_df['species'] == s], x=x_var, label=s, kde=True, ax=ax)
        ax.legend(title="품종")
    
    st.pyplot(fig)


# # iris_dashboard.py

# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # 데이터
# df = sns.load_dataset("iris")

# st.title("🌼 dashboard 🌼")

# # 데이터표시
# if st.checkbox("데이터 미리보기"):
#     st.write(df)

# # 품종필터링
# species_list = df['species'].unique().tolist()
# selected_species = st.multiselect("품종 선택", species_list, default=species_list)

# filtered_df = df[df['species'].isin(selected_species)]

# # X/Y축 선택
# numeric_columns = df.columns[:-1]
# x_var = st.selectbox("X축 변수", numeric_columns)
# y_var = st.selectbox("Y축 변수", numeric_columns, index=1)

# # 그래프종류 선택
# chart_type = st.radio("그래프 종류", ["산점도", "박스플롯", "히스토그램"])

# # 그래프 출력
# st.subheader("그래프")

# fig, ax = plt.subplots()
# if chart_type == "산점도":
#     sns.scatterplot(data=filtered_df, x=x_var, y=y_var, hue="species", ax=ax)
# elif chart_type == "박스플롯":
#     sns.boxplot(data=filtered_df, x="species", y=y_var, ax=ax)
# elif chart_type == "히스토그램":
#     for s in selected_species:
#         sns.histplot(data=filtered_df[filtered_df['species'] == s], x=x_var, label=s, kde=True, ax=ax)
#     ax.legend(title="품종")

# st.pyplot(fig)

# # 기초 통계량
# st.subheader("기초 통계량 요약")
# st.write(filtered_df.describe())