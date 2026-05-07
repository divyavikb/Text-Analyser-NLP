# WhatsApp Chat Analyser

A text analytics and NLP web application that transforms exported WhatsApp chat data into interactive visualisations and behavioural insights. Built with Python and Streamlit.

---

## Overview

This tool parses raw WhatsApp chat exports and performs multi-dimensional text analysis across individual users or the entire group. It surfaces message patterns, word frequencies, emoji usage, and temporal activity trends through an interactive dashboard.

---

## Features

- **Message Statistics** — Total messages, word count, media shared, and links exchanged per user or overall
- **Temporal Analysis** — Monthly and daily message timelines to identify activity trends over time
- **Activity Mapping** — Busiest days of the week, busiest months, and an hour-by-day heatmap showing peak activity windows
- **Word Frequency Analysis** — Most frequently used words with stopword removal, visualised as a bar chart
- **Word Cloud** — Visual representation of dominant vocabulary per user or across the group
- **Emoji Analysis** — Top emojis used with frequency distribution and pie chart breakdown
- **User Comparison** — Identify the most active participants with percentage contribution breakdown

---

## Tech Stack

| Layer | Tools |
|---|---|
| Web Framework | Streamlit |
| Data Processing | Python, Pandas, Regex |
| NLP & Text | WordCloud, NLTK Stopwords, Counter (Collections) |
| Emoji Processing | emoji library |
| URL Extraction | urlextract |
| Visualisation | Matplotlib, Seaborn |

---

## Project Structure

whatsapp-chat-analyser/
│
├── __pycache__/
├── myenv/
├── README.md
├── app.py
├── helper.py
└── preprocessor.py
```

---

## How It Works

### 1. Preprocessing (`preprocessor.py`)
The raw WhatsApp `.txt` export is parsed using a regex pattern that extracts the timestamp, sender name, and message text from each line. The parsed data is loaded into a Pandas DataFrame with engineered time features:

- Date, month, year, hour, minute
- Day name (Monday–Sunday)
- Hour period buckets (e.g. `14-15`) for heatmap rendering

### 2. Analytics (`helper.py`)
A suite of helper functions performs user-level or group-level analysis:

- `fetch_stats()` — message count, word count, media, links
- `monthly_timeline()` / `daily_timeline()` — time series aggregations
- `week_activity_map()` / `month_activity_map()` — activity distributions
- `activity_heatmap()` — pivot table of day × hour message counts
- `word_cloud()` / `most_frequent_words()` — text frequency analysis with stopword filtering
- `emojis_helper()` — emoji extraction and frequency ranking
- `most_busy_users()` — participant ranking by message volume

### 3. Dashboard (`app.py`)
Streamlit renders all analytics as an interactive dashboard. Users select a participant from a sidebar dropdown to filter all views to that individual, or keep "Overall" for group-level analysis.

---

## Getting Started

### Prerequisites
```bash
pip install streamlit pandas matplotlib seaborn wordcloud urlextract emoji
```

### Run the App
```bash
streamlit run app.py
```

### Exporting Your WhatsApp Chat
1. Open any WhatsApp chat (individual or group)
2. Tap ⋮ Menu → More → Export Chat
3. Select **Without Media**
4. Save the `.txt` file and upload it to the app

---

## Sample Insights

- Identify who drives the most conversation in a group
- Spot time-of-day patterns — when is the group most active?
- Track how conversation volume changes month over month
- Discover the most used words and emojis per person

---

## NLP Techniques Applied

- **Regex-based text parsing** — structured extraction from unstructured chat exports
- **Stopword removal** — filtering common words to surface meaningful vocabulary
- **Word frequency analysis** — term counting using Python's `Counter`
- **Word cloud generation** — weighted visual vocabulary representation
- **Emoji tokenisation** — character-level extraction and frequency ranking
- **URL detection** — link identification using `urlextract`

---

## Author

**Divya Balasubramanyam**
[GitHub](https://github.com/divyavikb) • [Substack](https://substack.com/@iyerdivya) • [LinkedIn](https://linkedin.com/in/divya-iyer-217241266)
