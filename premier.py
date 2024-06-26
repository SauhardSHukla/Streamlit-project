import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide",
                   page_title="Premier League Dashboard",
                   page_icon=":soccer:")


@st.cache_data
def load():
    return pd.read_csv('PremierLeague.csv')

#main code starts here
df =load()
st.image('download.png',use_column_width=True)
st.title('Preimer League Dashboard')
with st.expander("View raw preimer League Data"):
    st.dataframe(df.sample(1000)) #random Records

rows,columns =df.shape

numeric_df = df.select_dtypes(include="number")
cats_df = df.select_dtypes(exclude='number')
with st.expander('Columns Name'):
    st.markdown(f'Columns with Number:{", ".join(numeric_df)}')
    st.markdown(f'Columns without Number:{", ".join(cats_df)}')

c1,c2 = st.columns(2)
c1.markdown(f'### total  rows: {rows}')
c2.markdown(f'### total columns:{columns}')

# visualization

c1,c2 = st.columns([1,3])
xcol = c1.selectbox("Choose a columnns for the x-axis ",numeric_df.columns)
ycol = c2.selectbox("Choose a columnns for the y-axis ",numeric_df.columns)
zcol = c2.selectbox("Choose a columnns for the z-axis ",numeric_df.columns)
colours = c1.selectbox("Choose a columnns for the colour ",cats_df.columns)
fig = px.scatter_3d(df,x=xcol,y=ycol,z=zcol,color=colours)
c2.plotly_chart(fig,use_container_width=True)

st.title("What is Premier League")
c1,c2=st.columns(2)
c1.video("https://www.youtube.com/watch?v=wao8uhVnOGc&pp=ygUOcHJlbWllciBsZWFndWU%3D")
c2.markdown('''
#ENGLISH PREMIER LEAGUE
    The Premier League is the highest level of the English football league system. Contested by 20 clubs, it operates on a system of promotion and relegation with the English Football League (EFL). Seasons typically run from August to May, with each team playing 38 matches against all other teams, both home and away.[1] Most games are played on Saturday and Sunday afternoons, with occasional weekday evening fixtures.[2]

The competition was founded as the FA Premier League on 20 February 1992 following the decision of First Division (top-tier league from 1888 until 1992) clubs to break away from the English Football League. However, teams may still be relegated to and promoted from the EFL Championship. The Premier League takes advantage of a £5 billion television rights deal, with Sky and BT Group securing the domestic rights to broadcast 128 and 32 games, respectively.[3][4] This deal will rise to £6.7 billion for the four seasons from 2025 to 2029.[5] The league is projected to earn $7.2bn in overseas TV rights from 2022 to 2025.[6] The Premier League is a corporation managed by a chief executive, with member clubs acting as shareholders.[7] Clubs were apportioned central payment revenues of £2.4 billion in 2016–17, with a further £343 million in solidarity payments to EFL clubs.[8]

The Premier League is the most-watched sports league in the world, broadcast in 212 territories to 643 million homes, with a potential TV audience of 4.7 billion people.[9][10] For the 2018–19 season, the average Premier League match attendance was at 38,181,[11] second to the German Bundesliga's 43,500,[12] while aggregated attendance across all matches was the highest of any association football league at 14,508,981,[13] and most stadium occupancies are near capacity.[14] As of 2023, the Premier League is ranked first in the UEFA coefficient rankings based on performances in European competitions over the past five seasons, ahead of Spain's La Liga.[15] The English top-flight has produced the second-highest number of European Cup / UEFA Champions League titles, with a record six English clubs having won fifteen European championships in total.[16]        
            ''')

st.title("Premier League Clubs")
clubs = df['HomeTeam'].unique() + df["AwayTeam"].unique()
clubs = sorted(set(clubs))
st.info(", ".join(clubs))
