
import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.title("Cross-Country Solar Data Dashboard")

# Load cleaned data
@st.cache_data
def load_data():
    df_benin = pd.read_csv("./data/benin_clean.csv")
    df_benin["Country"] = "Benin"

    df_togo = pd.read_csv("./data/togo_clean.csv")
    df_togo["Country"] = "Togo"

    df_sierra = pd.read_csv("./data/sierraleone_clean.csv")
    df_sierra["Country"] = "Sierra Leone"

    return pd.concat([df_benin, df_togo, df_sierra], ignore_index=True)

df = load_data()

# Sidebar country selector
selected_countries = st.multiselect(
    "Select countries to compare:",
    options=df["Country"].unique(),
    default=list(df["Country"].unique())
)

filtered_df = df[df["Country"].isin(selected_countries)]

st.markdown("---")

# Boxplot of selected metric
st.header("📦 Solar Irradiance Comparison")
metric = st.selectbox("Choose solar metric:", ["GHI", "DNI", "DHI"])

fig = px.box(filtered_df,
        x="Country",
        y=metric,
        color="Country",
        title=f"{metric} Distribution by Country",)
st.plotly_chart(fig, use_container_width=True, theme="streamlit")



# Summary statistics table
st.markdown("---")

summary = filtered_df.groupby("Country")[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"])

st.header("📊 Summary Statistics")
st.subheader("GHI", divider="orange")
        
first_stat = st.container(border=True)
first_stat1, first_stat2, first_stat3 = first_stat.columns(3)

if 'Benin' in summary.index:
    with first_stat1:
        st.subheader("Benin")
        st.metric(label="Mean", value=summary.loc['Benin','GHI'].at['mean'], border=True)
        st.metric(label="Median", value=summary.loc['Benin','GHI'].at['median'], border=True)
        st.metric(label="STD", value=summary.loc['Benin','GHI'].at['std'], border=True)

if 'Sierra Leone' in summary.index:
    with first_stat2:
        st.subheader("Sierra Leone")
        st.metric(label="Mean", value=summary.loc['Sierra Leone','GHI'].at['mean'], border=True)
        st.metric(label="Median", value=summary.loc['Sierra Leone','GHI'].at['median'], border=True)
        st.metric(label="STD", value=summary.loc['Sierra Leone','GHI'].at['std'], border=True)

if 'Togo' in summary.index:
    with first_stat3:
        st.subheader("Togo")
        st.metric(label="Mean", value=summary.loc['Togo','GHI'].at['mean'], border=True)
        st.metric(label="Median", value=summary.loc['Togo','GHI'].at['median'], border=True)
        st.metric(label="STD", value=summary.loc['Togo','GHI'].at['std'], border=True)


st.subheader("DNI", divider="orange")
second_stat = st.container(border=True)
second_stat1, second_stat2, second_stat3 = second_stat.columns(3)

if 'Benin' in summary.index:
    with second_stat1:
        st.subheader("Benin")
        st.metric(label="Mean", value=summary.loc['Benin','DNI'].at['mean'], border=True)
        st.metric(label="Median", value=summary.loc['Benin','DNI'].at['median'], border=True)
        st.metric(label="STD", value=summary.loc['Benin','DNI'].at['std'], border=True)

if 'Sierra Leone' in summary.index:
    with second_stat2:
        st.subheader("Sierra Leone")
        st.metric(label="Mean", value=summary.loc['Sierra Leone','DNI'].at['mean'], border=True)
        st.metric(label="Median", value=summary.loc['Sierra Leone','DNI'].at['median'], border=True)
        st.metric(label="STD", value=summary.loc['Sierra Leone','DNI'].at['std'], border=True)

if 'Togo' in summary.index:
    with second_stat3:
        st.subheader("Togo")
        st.metric(label="Mean", value=summary.loc['Togo','DNI'].at['mean'], border=True)
        st.metric(label="Median", value=summary.loc['Togo','DNI'].at['median'], border=True)
        st.metric(label="STD", value=summary.loc['Togo','DNI'].at['std'], border=True)


st.subheader("DHI", divider="orange")
third_display = st.container(border=True)
third_display1, third_display2, third_display3 = third_display.columns(3)

if 'Benin' in summary.index:
    with third_display1:
        st.subheader("Benin")
        st.metric(label="Mean", value=summary.loc['Benin','DHI'].at['mean'], border=True)
        st.metric(label="Median", value=summary.loc['Benin','DHI'].at['median'], border=True)
        st.metric(label="STD", value=summary.loc['Benin','DHI'].at['std'], border=True)

if 'Sierra Leone' in summary.index:
    with third_display2:
        st.subheader("Sierra Leone")
        st.metric(label="Mean", value=summary.loc['Sierra Leone','DHI'].at['mean'], border=True)
        st.metric(label="Median", value=summary.loc['Sierra Leone','DHI'].at['median'], border=True)
        st.metric(label="STD", value=summary.loc['Sierra Leone','DHI'].at['std'], border=True)

if 'Togo' in summary.index:
    with third_display3:
        st.subheader("Togo")
        st.metric(label="Mean", value=summary.loc['Togo','DHI'].at['mean'], border=True)
        st.metric(label="Median", value=summary.loc['Togo','DHI'].at['median'], border=True)
        st.metric(label="STD", value=summary.loc['Togo','DHI'].at['std'], border=True)

#with st.container():


# Average GHI bar chart
st.markdown("---")
st.header("🏆 Average GHI by Country")
mean_ghi = filtered_df.groupby("Country")["GHI"].mean().sort_values()
st.bar_chart(mean_ghi)

