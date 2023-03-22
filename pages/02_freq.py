import streamlit as st
import pandas as pd

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

def calculate_freq_statistics(df, mean=False, median=False, mode=False, sum=False,
                          std=False, var=False, range=False, min=False, max=False,
                          sem=False, q1=False, q2=False, q3=False, skewness=False,
                          kurtosis=False):
    # 计算集中趋势
    statistics = pd.DataFrame()
    if mean:
        statistics['平均值'] = df.mean()
    if median:
        statistics['中位数'] = df.median()
    if mode:
        statistics['众数'] = df.mode().iloc[0, :].values
    if sum:
        statistics['总和'] = df.sum()

    # 计算离散特征
    if std:
        statistics['标准差'] = df.std()
    if var:
        statistics['方差'] = df.var()
    if range:
        statistics['范围'] = df.max() - df.min()
    if min:
        statistics['最小值'] = df.min()
    if max:
        statistics['最大值'] = df.max()
    if sem:
        statistics['标准差平均值'] = df.sem()

    # 计算百分位值
    if q1:
        statistics['Q1'] = df.quantile(0.25)
    if q2:
        statistics['Q2'] = df.quantile(0.5)
    if q3:
        statistics['Q3'] = df.quantile(0.75)

    # 计算后验分布
    if skewness:
        statistics['偏度'] = df.skew()
    if kurtosis:
        statistics['峰度'] = df.kurtosis()

    return statistics

def select_columns_iloc(df, columns):
    new_df = df.iloc[:, columns]
    return new_df

def select_columns_loc(df, loc):
    new_df = df.loc[:, loc]
    return new_df

st.title("freq")
variable_set = ["mean", "median", "mode", "sum", "std", "var", "range", "min", "max", "sem", "q1", "q2", "q3",
                "skewness", "kurtosis"]
if "data_file" not in st.session_state.keys() or st.session_state['data_file'] is None:
    st.write("please upload a sav file")
else:
    st.dataframe(st.session_state['data_file'], width=2000)
    data_file = st.session_state['data_file']
    columns_all = data_file.columns
    columns_selected = st.multiselect("please select the columns you want to analyse:",options=columns_all)
    variable_selected = st.multiselect("please select the variable you want to analyse:",options=["mean", "median",\
                                                                                                "mode", "sum", "std",\
                                                                                                "var", "range", "min", \
                                                                                                "max", "sem", "q1", "q2",\
                                                                                                "q3", "skewness","kurtosis"])

    variable_selected_x = [int(word in variable_selected) for word in variable_set]

    if len(columns_selected) != 0 and sum(variable_selected_x) != 0:
        st.subheader("calculate freq features:")
        # data_freq = calculate_freq_statistics(select_columns_loc(st.session_state['data_file'], columns_selected),
        #                                       mean=True, median=True, mode=True, sum=True,
        #                                       std=True, var=True, range=True, min=True, max=True,
        #                                       sem=True, skewness=True,
        #                                       kurtosis=True)
        data_freq = calculate_freq_statistics(select_columns_loc(st.session_state['data_file'], columns_selected),
                                              *variable_selected_x)
        st.dataframe(data_freq)




