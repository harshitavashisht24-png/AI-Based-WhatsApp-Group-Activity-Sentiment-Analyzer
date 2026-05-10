# AI-Powered WhatsApp Chat Analyzer

An AI and NLP based WhatsApp Group Chat Analysis System developed using Python and Streamlit.  
This project analyzes exported WhatsApp group chats and generates meaningful insights, behavioral analytics, sentiment analysis, topic detection, interaction patterns, and community intelligence.

---

# Project Overview

The system processes exported WhatsApp chat files (`.txt`) and performs:

- Group activity analysis
- User interaction analysis
- Sentiment and emotion detection
- Semantic topic modeling
- Narrative/opinion detection
- Community detection
- Hinglish (Hindi + English) text understanding
- AI-generated behavioral summaries
- Interactive dashboard visualization

---

# Features

## Basic Analytics
- Total messages
- Total users
- Most active members
- User-wise activity analysis
- Time-based activity tracking

## AI & NLP Features
- Sentiment Analysis
- Advanced AI Sentiment Detection
- Emotion Detection
- Semantic Topic Modeling
- Narrative Detection
- Community Detection
- Hinglish Text Normalization
- AI-generated Group Summary

## Visualizations
- Active user charts
- Sentiment graphs
- Word cloud generation
- Behavioral analytics dashboard

---

# Technologies Used

- Python
- Streamlit
- Pandas
- NLP
- Machine Learning
- Transformers
- Matplotlib
- Scikit-learn

---

# Project Structure

```text
WhatsApp-Chat-Analyzer/
│
├── backend/
│   ├── parser.py
│   ├── preprocess.py
│   ├── analytics.py
│   ├── interaction_analysis.py
│   └── time_analysis.py
│
├── ai_nlp/
│   ├── ai_pipeline.py
│   ├── advanced_sentiment.py
│   ├── emotion_detection.py
│   ├── semantic_topic_modeling.py
│   ├── narrative_detection.py
│   ├── community_detection.py
│   ├── hinglish_normalizer.py
│   └── ai_summary.py
│
├── frontend/
│   ├── dashboard.py
│   ├── visualize.py
│   └── wordcloud_generator.py
│
├── data/
├── output/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/your-repository-name.git

## Run the Project

python -m streamlit run app.py
```

## Move Into Project Folder

```bash
cd your-repository-name
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run The Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

# Input Format

Export WhatsApp group chats in `.txt` format and place them inside the `data/` folder.

Example:

```text
data/chat.txt
```

---

# Output Generated

The system generates:
- Cleaned datasets
- Sentiment analysis reports
- Word clouds
- User activity charts
- Narrative detection results
- Community analysis
- AI-generated summaries

Outputs are stored inside:

```text
output/
```

---

# Sample Analytics

- Most active users
- Positive vs negative sentiment
- Frequently discussed topics
- Behavioral clusters
- Interaction communities
- Emotional trends

---

# Future Improvements

- Real-time chat analytics
- Deployment on cloud
- Advanced multilingual support
- Improved interaction graph analysis
- Live dashboard updates

---

# Team Contributions

- Backend & Data Processing
- AI/NLP Intelligence Modules
- Frontend & Visualization Dashboard

---

# License

This project is developed for educational and internship purposes.

Live App:
https://harshitavashisht24-png-ai-based-whatsa-frontenddashboard-pelrsh.streamlit.app/
