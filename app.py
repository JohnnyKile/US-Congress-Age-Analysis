import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import dataprep

st.title('Legislators Project')

data = dataprep.df

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)



# data_grouped_party = data.groupby(['year','party']).agg({'age' : 'median'})
# data_grouped_party = data_grouped_party.reset_index()
# data_grouped_party
# filtered_data = data_grouped_party[data_grouped_party['party'] == party_to_filter]

party_to_filter = st.radio("Select party to filter", ["All", "Democrat", "Republican", "Independent"])
data_grouped_party = data.groupby(['year','party']).agg({'age' : 'median'})
data_grouped_party = data_grouped_party.reset_index()
if party_to_filter == 'All':
    data_grouped_party
else:
    filtered_data = data_grouped_party[data_grouped_party['party'] == party_to_filter]
    st.line_chart(data=filtered_data, x='year', y='age')

st.write('RDATA')

# def separate_parties(df, party_list):
#     for party in party_list


# party_list = ['Democrat', 'Republican', 'Independent']
# i = 0
# for party in party_list:
#     if i == 0:
#         party_data = data_grouped_party[data_grouped_party['party'] == party]
#         r_data.rename(columns = {'age':'age_Republicans'}, inplace = True)


r_data = data_grouped_party[data_grouped_party['party'] == 'Republican'][['year','age']]
r_data.rename(columns = {'age':'age_Republicans'}, inplace = True)
r_data
d_data = data_grouped_party[data_grouped_party['party'] == 'Democrat'][['year','age']]
d_data.rename(columns = {'age':'age_Democrats'}, inplace = True)
d_data 
i_data = data_grouped_party[data_grouped_party['party'] == 'Independent'][['year','age']]
i_data.rename(columns = {'age':'age_Independent'}, inplace = True)
i_data 

st.write('JOINED')

joined = d_data.join(r_data.set_index('year'), on='year').join(i_data.set_index('year'), on='year')
joined

st.line_chart(joined, x='year')


i_data = data_grouped_party[data_grouped_party['party'] == 'Independent'] 

joined = d_data.join(r_data.set_index('year'), on='year')
joined


# chartdata = pd.DataFrame(
#     ,
#     columns=['a', 'b', 'c'])
# r_data

fig, ax = plt.subplots()
ax.plot(r_data['year'], r_data['age'], color='red', label='Republicans')
ax.plot(d_data['year'], d_data['age'], color='blue', label='Democrats')
ax.plot(i_data['year'], i_data['age'], color='black', label='Independents')
ax.legend()
st.pyplot(fig)

# i_data
# republican
# democrat
# ind

# grouped_multiple = data.groupby(['year', 'party']).agg({'age': ['mean', 'min', 'max']})
# grouped_multiple.columns = ['age_mean', 'age_min', 'age_max']
# grouped_multiple = grouped_multiple.reset_index()
# grouped_multiple

data_grouped = data.groupby('year')
# data_grouped_party = data.groupby(['year','party'])
# data_grouped_party.get_group(('Republican'))

st.line_chart(data=data_grouped['year','age'].median(), x='year', y='age')
st.line_chart(data=data_grouped['year','age'].median(), x='year', y='age')

def plot():

    plist = ["Democrat", "Republican", "Independent"]

    parties = st.multiselect("Select party", plist)
    st.header("You selected: {}".format(", ".join(parties)))

    data_grouped_party = data.groupby(['year','party']).agg({'age' : 'median'})
    data_grouped_party = data_grouped_party.reset_index()
    filtered_data = data_grouped_party[data_grouped_party['party'] == party_to_filter]

    fig = go.Figure()
    fig = fig.add_trace(go.Scatter(x=filtered_data["year"], y=filtered_data["age"], name=party))

    st.plotly_chart(fig)

plot()


    # data_grouped_party = data.groupby(['year','party']).agg({'age' : 'median'})
    
    
    # dfs = {party: df[df["party"] == party] for party in plist}

    # fig = go.Figure()
    # for party, df in dfs.items():
    #     fig = fig.add_trace(go.Scatter(x=df["year"], y=df["age"], name=party))

    # st.plotly_chart(fig)

fig, ax = plt.subplots()
ax.plot(r_data)
st.pyplot(fig)




# party_to_filter = st.radio("Select party to filter", ["All", "Democrat", "Republican", "Independent"])
# data_grouped_party = data.groupby(['year','party']).agg({'age' : 'median'})
# data_grouped_party = data_grouped_party.reset_index()
# if party_to_filter == 'All':
#     data_grouped_party
# else:
#     filtered_data = data_grouped_party[data_grouped_party['party'] == party_to_filter]
#     st.line_chart(data=filtered_data, x='year', y='age')