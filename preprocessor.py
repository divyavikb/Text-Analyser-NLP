import pandas as pd
import re

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

    # Create DataFrame
    df = pd.DataFrame(messages, columns=['DateTime', 'Name', 'Message'])

    # Convert to datetime format
    df['Date'] = pd.to_datetime(df['DateTime'], format="%d/%m/%Y, %H:%M", dayfirst=True)

    # Extract features
    df['month'] = df['Date'].dt.month_name()
    df['day'] = df['Date'].dt.day
    df['year'] = df['Date'].dt.year
    df['hour'] = df['Date'].dt.hour
    df['min'] = df['Date'].dt.minute
    df['day_name']=df['Date'].dt.day_name()

    # Drop intermediate 'Date' column
    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df
