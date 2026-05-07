
from urlextract import URLExtract
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from collections import Counter
import pandas as pd
import re
import emoji
extract=URLExtract()

def fetch_stats(selected_user,df):
    l=[]
    if selected_user !="Overall":
        df=df[df['Name']==selected_user]
    for  message in df['Message'].tolist():
        l.extend(message.split(" "))
    count_of_media=df[df['Message'] == '<Media omitted>'].shape[0]

    links=[]

    for message in df['Message']:
        links.extend(extract.find_urls(message))
    return df.shape[0],len(l),count_of_media,len(links)
    

def most_busy_users(df):
    x=df['Name'].value_counts().head()
    vis_df=(df['Name'].value_counts(normalize=True)*100).reset_index().rename(columns={'index':'Name','Name':'Percentage'})
    return x,vis_df

def word_cloud(df,selected_user):
    if selected_user !="Overall":
        df=df[df['Name']==selected_user]
    wc=WordCloud(width=400,height=400,background_color='white',min_font_size=3)
    text = df['Message'].str.cat().lower()
    text = re.sub(r'[^A-Za-z\s]', '', text)
    stopwords = set(STOPWORDS)
    text = ' '.join(word for word in text.split() if word not in stopwords)
    wordlist=[]
    for texts in text.split(" "):
        if texts not in wordlist:
            wordlist.append(texts)
    wordlist=' '.join(wordlist)
    df_wc=wc.generate(wordlist)
    return df_wc


def most_frequent_words(df,selected_user):
    if selected_user !="Overall":
        df=df[df['Name']==selected_user]
    
    new_df=df[df['Message']!='<Media omitted>']
    str1 = new_df['Message'].str.cat().lower()
    str1 = re.sub(r'[^A-Za-z\s]', '', str1)
    list2 = []
    stopwords = set(STOPWORDS)
    words=[words for words in str1.split() if words not in stopwords]
    Counter(words).most_common()
    word_df=pd.DataFrame(Counter(words).most_common()).rename(columns={0:'Words',1:'Frequency'}).head(50).sort_values('Frequency')
    return word_df


def emojis_helper(df,selected_user):
    if selected_user !="Overall":
        df=df[df['Name']==selected_user]

    emojis=[]
    for message in df['Message']:
        emojis.extend([c for c in message if  emoji.is_emoji(c)])
    emoji_df=pd.DataFrame(Counter(emojis).most_common()).rename(columns={0:'Emoji',1:'Frequency'}).head(10).sort_values('Frequency',ascending=False)
    return emoji_df



def monthly_timeline(df,selected_user):
    if selected_user !="Overall":
        df=df[df['Name']==selected_user]

    timeline_df=df.groupby(['year','month'])['Message'].count().reset_index()

    col=[]
    for i in range(timeline_df.shape[0]):
        col.append(str(timeline_df.iloc[i]['year'])+'-'+ timeline_df.iloc[i]['month'])
    timeline_df['timeline']=col
    return timeline_df

def daily_timeline(df,selected_user):
    if selected_user !="Overall":
        df=df[df['Name']==selected_user]

    df['Only_date']=df['Date'].dt.date

    daily_timeline=df.groupby('Only_date')['Message'].count().reset_index()

    return daily_timeline


def week_activity_map(df,selected_user):
    if selected_user !="Overall":
        df=df[df['Name']==selected_user]

    return df['day_name'].value_counts()


def month_activity_map(df,selected_user):
    if selected_user !="Overall":
        df=df[df['Name']==selected_user]

    return df['month'].value_counts()


def activity_heatmap(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['Name'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='Message', aggfunc='count').fillna(0)

    return user_heatmap




   

    


    
    
    
    

        
        


