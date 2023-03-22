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

def calculate_disc_statistics(df, mean=False, sum=False, std=False, min=False, var=False,
                          max=False, range=False, sem=False, kurtosis=False, skewness=False,
                          std_err=False):
    # 计算描述统计特征
    statistics = pd.DataFrame()
    if mean:
        statistics['mean'] = df.mean()
    if sum:
        statistics['sum'] = df.sum()
    if std:
        statistics['std'] = df.std()
    if min:
        statistics['min'] = df.min()
    if var:
        statistics['var'] = df.var()
    if max:
        statistics['max'] = df.max()
    if range:
        statistics['range'] = df.max() - df.min()
    if sem:
        statistics['sem'] = df.sem()
    if kurtosis:
        statistics['kurtosis'] = df.kurtosis()
    if skewness:
        statistics['skewness'] = df.skew()

    # 计算标准差
    if std_err:
        std_df = pd.DataFrame({'mean': df.mean(), 'kurtosis': df.kurtosis(), 'skewness': df.skew()})
        std_df_sem = std_df.sem()
        std_mean_value = f"{std_df_sem['mean']:.3f}, {std_df_sem['kurtosis']:.3f}, {std_df_sem['skewness']:.3f}"
        statistics['std_mean'] = std_mean_value

    return statistics


def select_columns_iloc(df, columns):
    new_df = df.iloc[:, columns]
    return new_df

def select_columns_loc(df, loc):
    new_df = df.loc[:, loc]
    return new_df

st.title("disc")
variable_set = ["mean", "sum", "std", "min", "var", "max", "range", "sem", "kurtosis", "skewness", "std_err"]
if "data_file" not in st.session_state.keys() or st.session_state['data_file'] is None:
    st.write("please upload a sav file")
else:
    st.dataframe(st.session_state['data_file'], width=2000)
    data_file = st.session_state['data_file']
    columns_all = data_file.columns
    columns_selected = st.multiselect("please select the columns you want to analyse:",options=columns_all)
    variable_selected = st.multiselect("please select the variable you want to analyse:",options=["mean", "sum",\
                                                                                                "std", "min", "var",\
                                                                                                "max", "range", "sem", \
                                                                                                "kurtosis", "skewness", "std_err"])

    variable_selected_x = [int(word in variable_selected) for word in variable_set]
    if len(columns_selected) != 0 and sum(variable_selected_x) != 0:
        st.subheader("calculate disc features:")
        # data_disc = calculate_disc_statistics(select_columns_loc(data_file, columns_selected),
        #                           mean=True, sum=True, std=True, min=True, var=True,
        #                           max=True, range=True, sem=True, kurtosis=True, skewness=True,
        #                           std_err=False)
        data_freq = calculate_disc_statistics(select_columns_loc(st.session_state['data_file'], columns_selected),
                                              *variable_selected_x)
        st.dataframe(data_freq)