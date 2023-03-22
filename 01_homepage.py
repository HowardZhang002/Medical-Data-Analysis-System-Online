import streamlit as st

st.set_page_config(
    page_title = "主页",
    page_icon = ":house:",
    layout = "centered",
)

import pandas as pd
# import plotly.express as px
import pyreadstat
import tempfile

st.markdown("""
<style>
.css-14xtw13.e8zbici0
{
    visibility:hidden;
}
.css-1q1n0ol.egzxvld0
{
    visibility:hidden;
}
</style>
""",unsafe_allow_html=True)


session_state = st.session_state



st.title("医学数据分析平台")
st.sidebar.success("选择一个页面")

uploaded_file = st.file_uploader("Upload your .sav file", type=["sav"])
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name
    data, meta = pyreadstat.read_sav(file_path)
    df = pd.DataFrame(data)
    session_state['data_file'] = df
    st.dataframe(st.session_state['data_file'],width=2000)
else:
    if 'data_file' not in session_state.keys():
        st.write("please upload a sav file")
    elif session_state['data_file'] is not None:
        st.dataframe(st.session_state['data_file'],width=2000)


