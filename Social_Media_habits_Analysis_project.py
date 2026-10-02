import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# Page Configration.
st.set_page_config(page_title='Digital Habits Analysis Project',layout='wide')

# Read dataset.

df=pd.read_csv("Cleaned_data.csv",index_col=0)

#side bar design
col1, col2 = st.sidebar.columns([1, 3])
with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/2920/2920329.png", width=55
    )
with col2:
    st.subheader("Digital Habits Analytics Dashboard",)
page=st.sidebar.radio('Take a Tour',['Overview',"Digital Habits vs Productivity Analysis" ,"Digital Habits vs Well-being"])

# Pages Design
if page == 'Overview':
    st.title('Dataset Overview & Key Metrics')
    st.caption("General summary and distributions of the dataset.")
    t1,t2=st.tabs(['General summary','Columns Distributions'])
    with t1:
            m1, m2, m3 = st.columns(3)
            m1.metric("Number of Users", len(df),border=True,icon="👤")
            m2.metric(
                "Avg Productivity Score",
                f"{df['perceived_productivity_score'].mean():.2f}",border=True,icon="📊"
            )
            m3.metric(
                "Avg Social Media Hours", f"{df['daily_social_media_time'].mean():.2f}",border=True,icon='⏰'
            ,
            )
            st.markdown("---")
            st.image(r'D:\Project_Mid\15_thoughts_social_media_0.png')
            st.caption("Sample of Data")
            st.dataframe(df.head(15),use_container_width=True)
            st.markdown("---")
            st.caption("Summary Statistics for Numerical Columns")
            st.dataframe(df.describe())
            st.markdown("---")
    with t2:

        m1, m2, m3 = st.columns(3)
        m1.metric("Number of Users", len(df),border=True,icon="👤")
        m2.metric(
                "Avg Productivity Score",
                f"{df['perceived_productivity_score'].mean():.2f}",border=True,icon="📊"
                     )
        m3.metric(
                "Avg Social Media Hours", f"{df['daily_social_media_time'].mean():.2f}",border=True,icon='⏰'
                ,
                )
        st.markdown("---")
        
        fig=px.histogram(df,x="daily_social_media_time",text_auto=True,nbins=20,color_discrete_sequence=px.colors.sequential.Emrld,title='Distribution of social media usage daily')
        fig.update_layout(
        xaxis_title="Avg Daily Social Media Usage",
        yaxis_title="Count of users",)
        fig
        st.markdown("---")
        
        fig=px.histogram(df,x="perceived_productivity_score",text_auto=True,nbins=20,color_discrete_sequence=px.colors.sequential.Emrld,title="Distribution of precevied productivty score")
        fig.update_layout(
            xaxis_title="Productivity Score",
            yaxis_title="Count of users",
            
            )
        fig

        st.markdown("---")
        fig=px.histogram(df,x="social_platform_preference",text_auto=True,color_discrete_sequence=px.colors.sequential.Emrld,title='Distribution of Social Media Platforms').update_xaxes(categoryorder='max descending')
        fig.update_layout(
            xaxis_title="Social Media Platforms",
            yaxis_title="Count of users",)
        fig
        st.markdown("---")
        fig=px.pie(df,names='gender',title="Gender distribiton by percentage",hole=0.5,color_discrete_sequence=px.colors.sequential.Emrld,)
        fig
        st.markdown("---")
        fig=px.histogram(df,x="sleep_hours",text_auto='True',color_discrete_sequence=px.colors.sequential.Emrld,nbins=10,title='Avg Sleep Hours Per day').update_xaxes(categoryorder='max descending')
        fig.update_layout(

            xaxis_title="Sleep Hours",
            yaxis_title="Count of users",
            )
        fig    
        st.markdown("---")

elif page == 'Digital Habits vs Productivity Analysis':
    st.title('Digital Habits vs Productivity Analysis')
    st.markdown("---")
    age_grouped=df.groupby('age_group')['perceived_productivity_score'].mean().reset_index().round(2)

    fig=px.bar(age_grouped,
           x='age_group',
           y='perceived_productivity_score'
           ,
           text_auto='.2f',
           color='perceived_productivity_score',
           color_continuous_scale=px.colors.sequential.Magenta
           ,
           title='Average Productivity Score by Age Group',
           labels={
        "age_group": "Age Group",
        "perceived_productivity_score": "Avg Productivity Score",
    },
           
           ).update_xaxes(categoryorder='max descending')

    fig.update_traces(textposition="outside")
    fig
    st.markdown("---")
    gender_grouped_uasge=df.groupby('gender')[["daily_social_media_time",'perceived_productivity_score']].mean().reset_index()

    fig=px.bar(gender_grouped_uasge,
           x='gender',
           y='daily_social_media_time'
           ,
           text_auto='.2f',
           color_continuous_scale=px.colors.sequential.Magenta
           ,color='perceived_productivity_score',
           title='Average Daily Social Media Usage vs. Productivity Score by Gender',
           barmode='group',
           labels={
        "gender": "Gender",
        "daily_social_media_time": "Avg Daily Social Media Time (Hours)",
        "perceived_productivity_score": "Avg Productivity Score",
    },
           )
    fig.update_traces(textposition="outside")
    fig
    st.markdown("---")
    focus_grouped=df.groupby("uses_focus_apps")['perceived_productivity_score'].mean().round(2).reset_index()
    fig=px.bar(data_frame=focus_grouped,
                    color='perceived_productivity_score',
                    x='uses_focus_apps',
                    y='perceived_productivity_score',
                    color_continuous_scale=px.colors.sequential.Magenta,
                    title='Impact of Focus Apps on Average Productivity Score',
                    text_auto=True,
                    labels={
                            "uses_focus_apps": "Uses Focus Apps",
                            "perceived_productivity_score": "Average Perceived Productivity Score"}
                    )
    fig
    gender_grouped=df.groupby('gender')['perceived_productivity_score'].mean().reset_index()

    fig=px.bar(gender_grouped,
           x='gender',
           y='perceived_productivity_score'
           ,
           color='perceived_productivity_score'
           ,
           text_auto='.2f',
           color_continuous_scale=px.colors.sequential.Magenta
           ,
           title='Average Productivity Score by Gender',
           labels={
        "gender": "Gender",
        "perceived_productivity_score": "Avg Productivity Score",
    },
           
           ).update_xaxes(categoryorder='max descending')
    fig.update_traces(textposition="outside")
    fig
elif page == ('Digital Habits vs Well-being'):
    st.title('Digital Habits vs Well-being')
    st.markdown("---")
    job_grouped=df.groupby('job_type')['daily_social_media_time'].mean().sort_values(ascending=False).reset_index().round(2)
    job_grouped
    fig=px.bar(job_grouped,
           x='job_type',
           y='daily_social_media_time'
           ,
           text_auto='.2f',
           color='daily_social_media_time',
           color_continuous_scale=px.colors.sequential.Aggrnyl_r
           ,
           title='Average Social Media Usage by Status(Job Type)',
           labels={
        "job_type": "Status(Job Type)",
        "daily_social_media_time": "Avg Daily Social Media Time (Hours)",
    },
           
           ).update_xaxes(categoryorder='max descending')

    fig.update_traces(textposition="outside")  
    fig
    st.markdown("---")
    age_grouped_2=df.groupby("age_group")[['screen_time_before_sleep']].mean().reset_index().round(3)
    age_grouped_2
    fig=px.pie(age_grouped_2,names='age_group',values='screen_time_before_sleep',color='age_group',title="Distribution of Screen Time Before Sleep by Age Category",color_discrete_sequence=px.colors.sequential.Aggrnyl_r,)

    fig.update_traces(textinfo="percent+value")
    fig
    st.markdown("---")
    break_grouped = (
    df.groupby(["job_type",])["breaks_during_work"]
    .mean().sort_values(ascending=False)
    .round(2)
    .reset_index()
)
    fig = px.bar(
    break_grouped,
    x="job_type",
    y="breaks_during_work",
    color='breaks_during_work',
    barmode="group",  
    color_continuous_scale=px.colors.sequential.Aggrnyl_r,
    text_auto=".2f",
    title="Average Work Break Duration by Job Type",
    labels={
        "job_type": "Job Type",
        "breaks_during_work": "Total Number of breaks during work hours ",
        
    },
)
    fig

    grouped_age_burnout=df.groupby("age_group")['days_feeling_burnout_per_month'].mean().reset_index().round(2)
    st.markdown("---")
    fig=px.bar(grouped_age_burnout,
           x='age_group',
           y='days_feeling_burnout_per_month'
           ,
           text_auto='.2f',
           color='days_feeling_burnout_per_month',
           color_continuous_scale=px.colors.sequential.Aggrnyl_r
           ,
           title='Average Days Feeling burnout By Age Categories',
           labels={
        "age_group": "Age",
        "days_feeling_burnout_per_month": "Total Days Feeling Burnout per Month ",
    },
           
           ).update_xaxes(categoryorder='max descending')

    fig.update_traces(textposition="outside")
    fig


 










