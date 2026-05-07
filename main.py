import os

print("Running WhatsApp Chat Analyzer Pipeline...\n")

os.system("python parser.py")
os.system("python preprocess.py")
os.system("python analytics.py")
os.system("python visualize.py")
os.system("python time_analysis.py")
os.system("python sentiment_analysis.py")
os.system("python interaction_analysis.py")
os.system("python topic_detection.py")
os.system("python wordcloud_generator.py")

print("\nPipeline completed successfully!")