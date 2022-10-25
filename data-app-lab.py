import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data(1990) by Jiayi Li')
df = pd.read_csv('housing.csv')

house_price_filter = st.slider('Minimum Median House Price', 0, 500001, 200000)

# create a multi select
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique())

# create a checkbox?
income_filter = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High')
)
#filter by House Price
df = df[df.median_house_value >= house_price_filter]

#filter by location
df = df[df.ocean_proximity.isin(location_filter)]

if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income <= 4.5)]
elif income_filter == 'High':
    df = df[df.median_income > 4.5]

# show on map
st.map(df)

# show the hist
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(20, 5))
df.median_house_value.plot.hist(bins = 30)
ax.set_ylabel('')
st.pyplot(fig)
