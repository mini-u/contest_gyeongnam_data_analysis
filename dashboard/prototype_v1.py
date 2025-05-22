import streamlit as st

st.set_page_config(layout="wide")

# 타이틀
st.title("프로토타입 레이아웃")

# 분할
left_col, right_col = st.columns([2, 3])

# 지도
with left_col:
    st.subheader("지도")
    st.markdown("경남지도표시")

# 데이터
with right_col:
    st.subheader("공급")
    st.markdown("문화시설, 접근성")

    st.divider()

    st.subheader("수요")
    st.markdown("사람, 생활인구, 거주인구 등")

    st.divider()

    st.subheader("전략")
    st.markdown("무슨전략을 제시하지")
