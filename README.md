# 📱 WhatsApp Chat Analyzer

A Python-based AI/NLP project that analyzes exported WhatsApp group chats and generates meaningful insights, analytics, sentiment analysis, interaction patterns, topic detection, and visualizations.

---

# 🚀 Project Overview

This project is designed to analyze WhatsApp group chats exported in `.txt` format.  
The system processes chat data and generates useful insights about:

- Group activity
- User behavior
- Sentiment trends
- Interaction patterns
- Discussion topics
- AI/NLP-based analysis

The project is divided into:
- Backend & Data Processing
- AI/NLP Analysis
- Frontend Dashboard (future scope)

---

# ✨ Features

## 🔹 Backend & Data Processing
- WhatsApp chat parsing
- Data cleaning and preprocessing
- CSV dataset generation
- Automated processing pipeline

## 🔹 Analytics
- Most active users
- Total message count
- Most used words
- Time-based activity analysis
- Hourly activity trends

## 🔹 AI/NLP Features
- Sentiment analysis
- Topic detection
- Interaction analysis
- Narrative detection
- Emotion detection
- Hinglish normalization
- Community/cluster detection
- AI-generated summaries

## 🔹 Visualizations
- User activity charts
- Word clouds
- Sentiment graphs
- Time analysis graphs
- Streamlit dashboard integration

---

# 🛠️ Tech Stack

- Python
- Pandas
- Matplotlib
- Streamlit
- TextBlob
- WordCloud
- NLP Libraries

---

# 📂 Project Structure

```plaintext
whatsapp-chat-analyzer/
│
├── backend/
│   ├── analytics.py
│   ├── interaction_analysis.py
│   ├── parser.py
│   ├── preprocess.py
│   ├── sentiment_analysis.py
│   ├── time_analysis.py
│   ├── topic_detection.py
│   ├── visualize.py
│   └── wordcloud_generator.py
│
├── nlp_ai/
│   ├── advanced_sentiment.py
│   ├── ai_pipeline.py
│   ├── ai_summary.py
│   ├── community_detection.py
│   ├── emotion_detection.py
│   ├── hinglish_normalizer.py
│   ├── narrative_detection.py
│   └── semantic_topic_modeling.py
│
├── data/
│   └── sample_chat.txt
│
├── output/
│   ├── active_users.png
│   ├── chat_data.csv
│   ├── clean_chat_data.csv
│   ├── final_chat_data.csv
│   ├── hourly_activity.png
│   ├── sentiment_analysis.png
│   ├── top_words.png
│   └── wordcloud.png
│
├── app.py
├── main.py
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/harshitavashisht24-png/whatsapp-chat-analyzer.git
```

## 2️⃣ Move to Project Directory

```bash
cd whatsapp-chat-analyzer
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

## Run Complete Backend + AI/NLP Pipeline

```bash
python main.py
```

This will:
- Parse chat data
- Preprocess messages
- Generate analytics
- Perform sentiment analysis
- Generate visualizations
- Run AI/NLP modules

---

## Run Streamlit Dashboard

```bash
python -m streamlit run app.py
```

---

# 📥 Input Format

1. Export WhatsApp group chat in `.txt` format
2. Place the exported file inside the `data/` folder
3. Run the pipeline

---

# 📊 Output Generated

The project generates:
- CSV datasets
- User analytics
- Sentiment analysis
- Word clouds
- Charts and graphs
- AI/NLP insights

All generated files are stored inside the `output/` folder.

---

# 🔮 Future Improvements

- Better Hindi + English mixed language understanding
- Transformer-based sentiment analysis
- Advanced narrative detection
- Real-time dashboard updates
- Improved UI/UX
- Network graph visualizations
- Frontend integration

---

# 👥 Team Contributions

## 👨‍💻 Person 1 — Backend & Data Processing
- Chat parsing
- Data preprocessing
- Analytics generation
- Backend pipeline integration

## 🤖 Person 2 — AI/NLP Module
- Sentiment enhancement
- Narrative detection
- Community detection
- Hinglish processing
- AI-based insights

## 🎨 Person 3 — Frontend & Dashboard
- Streamlit dashboard
- UI improvements
- Interactive visualizations
- User experience enhancements

---

# 📌 Repository

GitHub Repository:  
https://github.com/harshitavashisht24-png/whatsapp-chat-analyzer

---

# ⭐ Conclusion

This project demonstrates the use of:
- Data Processing
- Natural Language Processing (NLP)
- AI-based Analytics
- Data Visualization
- Streamlit Dashboard Development

to generate meaningful insights from WhatsApp group conversations.