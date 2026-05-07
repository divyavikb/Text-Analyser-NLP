import streamlit as st
import preprocessor
import pandas as pd
import helper
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

st.sidebar.title('Whatsapp test Analyser')

Uploaded_file=st.sidebar.file_uploader('Upload a file')
if Uploaded_file is not None:
    bytes_data= Uploaded_file.getvalue()
    data=bytes_data.decode('utf-8')
    df=preprocessor.preprocessor(data)
    
    user_list=df['Name'].unique().tolist()
    user_list.insert(0,"Overall")
    user_list.sort()
    
    selected_user=st.sidebar.selectbox("Show analysis wrt",user_list)

    st.dataframe(df)

    st.title("Monthly Timeline")
    timeline_df=helper.monthly_timeline(df,selected_user)
    fig,axes=plt.subplots()
    axes.plot(timeline_df['timeline'],timeline_df['Message'])
    plt.xticks(rotation=90)
    st.pyplot(fig)


    st.title("Daily Timeline")
    daily_timeline=helper.daily_timeline(df,selected_user)
    fig,axes=plt.subplots()
    axes.plot(daily_timeline['Only_date'],daily_timeline['Message'])
    plt.xticks(rotation=90)
    st.pyplot(fig)


    st.title("Activity Map")
    col1,col2=st.columns(2)

    with col1:
        st.header("Most Busy Day")
        busy_day=helper.week_activity_map(df,selected_user)
        fig,axes=plt.subplots()
        axes.bar(busy_day.index,busy_day.values)
        plt.xticks(rotation=90)
        st.pyplot(fig)

    with col2:
        st.header("Most Busy Month")
        busy_month=helper.month_activity_map(df,selected_user)
        fig,axes=plt.subplots()
        axes.bar(busy_month.index,busy_month.values)
        plt.xticks(rotation=90)
        st.pyplot(fig)

    st.title("Weekly Activity Map")
    user_heatmap = helper.activity_heatmap(selected_user,df)
    fig,ax = plt.subplots()
    ax = sns.heatmap(user_heatmap)
    st.pyplot(fig)


    if st.sidebar.button("Show analysis"):
        num_messages,total_words,count_of_media,num_links=helper.fetch_stats(selected_user,df)


        st.title("Total Statistics")
       
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total words")
            st.title(total_words)
        with col3:
            st.header("Total media shared")
            st.title(count_of_media)
        with col4:
            st.header("Total links shared")
            st.title(num_links)

    if selected_user=='Overall':
        st.header("Most Busy Users")
        x,vis_df=helper.most_busy_users(df)
        col1,col2 =st.columns(2)
        fig,axes=plt.subplots()
        with col1:
            axes.bar(x.index,x.values,color='pink')
            plt.xticks(rotation=90)
            st.pyplot(fig)
        with col2:
            st.dataframe(vis_df)

    
    st.header("Wordcloud")
    df_wc=helper.word_cloud(df,selected_user)
    fig,axes=plt.subplots()
    axes.imshow(df_wc)
    st.pyplot(fig)

    st.header("Most Frequent Words")
    word_df=helper.most_frequent_words(df,selected_user)
    fig,axes=plt.subplots()
    axes.barh(word_df['Words'],word_df['Frequency'],color='pink')
    plt.xticks(rotation=90)
    st.pyplot(fig)

    st.header("Analysis of Emojis")
    emoji_df=helper.emojis_helper(df,selected_user)
    col1,col2 =st.columns(2)
    with col1:
        fig,axes=plt.subplots()
        axes.pie(emoji_df['Frequency'],labels=emoji_df['Emoji'])
        st.pyplot(fig)
    with col2:
        st.dataframe(emoji_df)
            

    
