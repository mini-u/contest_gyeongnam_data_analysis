import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

# 타이틀
st.title("프로토타입 레이아웃")

# 분할
left_col, right_col = st.columns([2, 3])

# 지도
with left_col:
    st.subheader("지도")
    st.markdown("경남지도표시")
    
    gdf = gpd.read_file(r"D:\MINNIE\contest_gyeongnam_data_analysis\data_for_dashboard\GN_map.geojson")
    
    center = gdf.geometry.union_all().centroid
    m = folium.Map(location=[center.y, center.x], zoom_start=8.5, tiles=None)
    
    # GeoJson 추가
    geojson_layer = folium.GeoJson(
        gdf,
        tooltip=folium.GeoJsonTooltip(fields=["SGG_NM_cleaned"]),
        style_function=lambda x: {
            "fillColor": "white",
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.0
        },
    )
    geojson_layer.add_to(m)

    clicked_area = st_folium(m, width=850, height=650)
    
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
