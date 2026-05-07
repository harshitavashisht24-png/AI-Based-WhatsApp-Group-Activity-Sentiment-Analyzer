import os

print("Running WhatsApp Chat Analyzer Pipeline...\n")

# Backend Pipeline
os.system("python backend/parser.py")
os.system("python backend/preprocess.py")
os.system("python backend/analytics.py")
os.system("python backend/visualize.py")
os.system("python backend/time_analysis.py")
os.system("python backend/sentiment_analysis.py")
os.system("python backend/interaction_analysis.py")
os.system("python backend/topic_detection.py")
os.system("python backend/wordcloud_generator.py")

# AI/NLP Pipeline
os.system("python nlp_ai/advanced_sentiment.py")
os.system("python nlp_ai/emotion_detection.py")
os.system("python nlp_ai/narrative_detection.py")
os.system("python nlp_ai/community_detection.py")
os.system("python nlp_ai/semantic_topic_modeling.py")
os.system("python nlp_ai/hinglish_normalizer.py")
os.system("python nlp_ai/ai_summary.py")

print("\nPipeline completed successfully!")