import re
import pandas as pd




def preprocessor(data):
    pattern = r'(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}) - (.*?): '

    # Split and capture
    chunks = re.split(pattern, data)

    # Every message starts from index 1 and appears in triples: [datetime, name, message]
    messages = []
    for i in range(1, len(chunks), 3):
        datetime = chunks[i]
        name = chunks[i+1]
        message = chunks[i+2].strip()
        messages.append((datetime, name, message))
    list1=[]
    list2=[]
    list3=[]
    for i in messages:
        list1.append(i[0])
        list2.append(i[1])
        list3.append(i[2])
    df=pd.DataFrame({'Date':list1,'Name':list2,'Message':list3})
    df['Date'] = pd.to_datetime(df['Date'])
    df['month']=df['Date'].dt.month_name()
    df['day']=df['Date'].dt.day
    df['year']=df['Date'].dt.year
    df['hour']=df['Date'].dt.hour
    df['min']=df['min'].dt.hour
    df.drop('Date',axis=1,inplace=True)
    return df